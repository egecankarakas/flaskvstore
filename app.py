import json
import logging
import re
import sys

import redis
from flask import Flask, request
from simplekv.memory.redisstore import RedisStore

REDIS_HOST = 'YOUR_REDIS_HOST'

HTTP_SUCCESS = 200
HTTP_ERROR = 400
HTTP_NOT_FOUND = 404

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
store = RedisStore(redis.StrictRedis(host=REDIS_HOST))
application = Flask(__name__)
logger = logging.getLogger('flaskvstore')


@application.route('/keys', methods=['GET', 'DELETE', 'PUT'])
def route_keys():
    if request.method == 'PUT':
        try:
            ttl = request.args.get('expire_in')
            if ttl:
                ttl = int(ttl)
        except Exception as e:
            logger.error(e, exc_info=True)
            return 'Bad TTL Parameter', HTTP_ERROR
        item = [(item[0], item[1]) for item in request.args.items() if item[0] != 'expire_in'][0]
        store.put(item[0], bytes(item[1], 'utf-8'), ttl_secs=ttl)
        logger.info(f'Item : {item} added/updated.')
        return 'success', HTTP_SUCCESS
    elif request.method == 'GET':
        message = 'KEY-VALUE Store Scanned'
        filter_expression = request.args.get('filter')
        keys = store.keys()
        if filter_expression:
            pattern = re.compile(filter_expression.replace('$', '.'))
            message += f' with pattern {pattern}'
            keys = [key for key in keys if pattern.match(key)]
        result = [{key: store.get(key).decode('utf-8')} for key in keys]
        logger.info(message)
        return json.dumps(result), HTTP_SUCCESS
    elif request.method == 'DELETE':
        keys = store.keys()
        for key in keys:
            store.delete(key)
        message = 'KEY-VALUE Store Cleared'
        logger.info(message)
        return message, HTTP_SUCCESS


@application.route('/keys/<string:key_id>', methods=['GET', 'DELETE'])
def route_specific_key(key_id):
    if request.method == 'HEAD':
        if key_id not in store.keys():
            message = f'Key : {key_id} not found'
            logger.debug(message)
            return 'false', HTTP_NOT_FOUND
        message = f'Key : {key_id} checked'
        logger.debug(message)
        return 'true', HTTP_SUCCESS
    elif request.method == 'GET':
        try:
            message = f'Key : {key_id} accessed'
            logger.debug(message)
            return json.dumps({key_id: store.get(key_id).decode('utf-8')}), HTTP_SUCCESS
        except Exception as e:
            logger.error(e, exc_info=True)
            return 'Key Error', HTTP_ERROR
    elif request.method == 'DELETE':
        try:
            store.delete(key_id)
            message = f'Key : {key_id} deleted'
            logger.info(message)
            return message, HTTP_SUCCESS
        except Exception as e:
            logger.error(e, exc_info=True)
            return 'Key Error', HTTP_ERROR


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
