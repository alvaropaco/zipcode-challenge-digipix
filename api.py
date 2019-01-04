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


manager.add_command('runserver', CustomServer())

manager.run()
