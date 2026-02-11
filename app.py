from flask import Flask, request, jsonify
from controller.app import createUser
from service.service import getUser, deleteUser
from models.model import usuarios

app = Flask(__name__)

@app.route('/criar', methods=['POST'])
def criarUsuario():
    
    lista_usuarios = createUser()

    return "Usuário cadastrado!"


@app.route('/listar')
def listarUsuarios():

    return usuarios


@app.route('/listar/<int:cpf>')
def listarUsuario(cpf):

    usuario = getUser(cpf)

    return usuario


@app.route('/deletar/<int:cpf>', methods=['DELETE'])
def deletarUsuario(cpf):

    usuario = deleteUser(cpf)

    return usuario