from flask import Flask, jsonify, request
from flask_restx import Api
from pruebas import api as pruebas_ns

app = Flask(__name__)

api = Api(app, title="Mi API", version="1.0", description="Documentación de mi API con Swagger")


api.add_namespace(pruebas_ns, path="/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
