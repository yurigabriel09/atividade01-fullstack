from models.model import usuarios

def usuario(dados):

    usuarios.append(dados)

    return usuarios


def getUser(cpf):

    for user in usuarios:
        if user['cpf'] == cpf:
            return user
        
    
    return "Usuario nao encontrado!"


def deleteUser(cpf):

    usuario = getUser(cpf)

    for user in usuarios:
        if user == usuario:
            usuarios.remove(user)
            return "Usuario deletado!"
        
    return "Usuario nao encontrado!"