from subprocess import call

from flask import Flask, request, jsonify
from flask_script import Manager, Server
from flasgger import Swagger
from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__)
manager = Manager(app)
Swagger(app)
CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost:5672"}


def zipcode_service():
    pass


class CustomServer(Server):
    def __call__(self, app, *args, **kwargs):
        zipcode_service()

        return Server.__call__(self, app, *args, **kwargs)


@app.route('/zipcode', methods=['GET'])
def zipcode():
    """
    Micro Service Based Compute and Mail API
    This API is made with Flask, Flasgger and Nameko
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: data
          properties:
            operation:
              type: string
              enum:
                - sum
                - mul
                - sub
                - div
            email:
              type: string
            value:
              type: integer
            other:
              type: integer
    responses:
      200:
        description: Please wait the calculation, you'll receive an email with results
    """
    with ClusterRpcProxy(CONFIG) as rpc:
        result = rpc.zipcode.getZipcode("13560044")
        return jsonify(result), 200


manager.add_command('runserver', CustomServer())

manager.run()
