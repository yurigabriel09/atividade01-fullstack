from flask import request, jsonify
from service.service import usuario


def createUser():

    dados = request.get_json()

    lista_usuarios = usuario(dados)

    return lista_usuarios