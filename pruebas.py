from flask import jsonify
from flask_restx import Namespace, Resource

api = Namespace("pruebas", description="Rutas de prueba")

@api.route("/")
class Prueba(Resource):
    def get(self):
        """Devuelve un mensaje de prueba"""
        return "prueba"

@api.route("/usuarios")
class Usuarios(Resource):
    def get(self):
        """Devuelve un mensaje de usuarios"""
        return "esta es la ventana de usuarios"

@api.route("/json")
class JsonTest(Resource):
    def get(self):
        """Devuelve un JSON de prueba"""
        return jsonify({"nombre": "api-rest"})
