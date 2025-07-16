import app
from app.models import schema
from flask import Flask, request, jsonify

class Login:
    @staticmethod
    def autenticar():
        email = request.args.get('email')
        senha = request.args.get('senha')
        usuario = schema.Usuario.query.filter_by(email=email,senha_hash=schema.Usuario.check_senha(senha)).first()
        if usuario:
            print("Encontrado")
        else:
            print("Usuário não encontrado")
        return jsonify({'mensagem':'Sucesso'})