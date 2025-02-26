from flask import Flask, jsonify, request
from pruebas import pruebas_api

app = Flask(__name__)


app.register_blueprint(pruebas_api)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
