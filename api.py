from flask import Flask, request, jsonify
from flasgger import Swagger
from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__)
Swagger(app)
CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost:5672"}


@app.route('/zipcode', methods=['GET'])
def zipcode():
    """
    Micro Service Based Compute and Mail API
    This API is made with Flask, Flasgger and Nameko
    ---
    parameters:
      - name: zipcode
        in: path
        required: true
        schema:
          type: integer
        description: location ZipCode
    responses:
      200:
        description: Location data
    """
    with ClusterRpcProxy(CONFIG) as rpc:
        result = rpc.zipcode.getZipcode(request.args.get('code'))
        return jsonify(result), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
