from flask import Flask, jsonify, request
from flask import Blueprint

pruebas_api = Blueprint ('pruebas_api', __name__)

@pruebas_api.route("/")
def prueba ():
    return "prueba"

@pruebas_api.route("/usuarios")
def prueba2 ():
    return "esta es la ventana de usuarios, SI"

@pruebas_api.route("/json")
def prueba3 ():
    prueba = {
        "nombre" : "api-restaaaa"
    }
    return jsonify(prueba)

