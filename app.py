from flask import Flask, request
from simplekv.memory.redisstore import RedisStore
import redis

store = RedisStore(redis.StrictRedis())
app = Flask(__name__)


@app.route('/keys', methods=['GET', 'DELETE', 'PUT'])
def keys():
    if request.method == 'PUT':
        ttl = request.args.get('expire_in')
        # TODO: add/update a value
        item = [(item[0], item[1]) for item in request.args.items() if item[0] != 'expire_in'][0]
        return 'success', 200
    elif request.method == 'GET':
        filter_expression = request.args.get('filter')
        # TODO: get all keys and values
        raise NotImplementedError
    elif request.method == 'DELETE':
        # TODO: delete  all values
        raise NotImplementedError


@app.route('/keys/<string:key_id>', methods=['GET', 'DELETE'])
def keys2(key_id):
    if request.method == 'HEAD':
        # TODO: check if a value exists
        raise NotImplementedError
    elif request.method == 'GET':
        # TODO: get a value
        raise NotImplementedError
    elif request.method == 'DELETE':
        # TODO: delete a value
        raise NotImplementedError


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
