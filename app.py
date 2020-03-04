from flask import Flask, request

app = Flask(__name__)


@app.route('/keys', methods=['GET', 'DELETE'])
def keys():
    if request.method == 'GET':
        filter_expression = request.args.get('filter')
        # TODO: get all keys and values
        raise NotImplementedError
    elif request.method == 'DELETE':
        # TODO: delete  all values
        raise NotImplementedError


@app.route('/keys/<string:key_id>', methods=['GET', 'DELETE', 'PUT'])
def keys2(key_id):
    if request.method == 'HEAD':
        # TODO: check if a value exists
        raise NotImplementedError
    elif request.method == 'GET':
        # TODO: get a value
        raise NotImplementedError
    elif request.method == 'PUT':
        ttl = request.args.get('expire_in')
        # TODO: add/update a value
        raise NotImplementedError
    elif request.method == 'DELETE':
        # TODO: delete a value
        raise NotImplementedError


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
