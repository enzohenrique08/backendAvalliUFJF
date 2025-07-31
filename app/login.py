import app
from app.models import schema
from flask import Flask, request, jsonify

class Login:
    @staticmethod
    def autenticar():
        email = request.args.get('email')
        senha = request.args.get('senha')
        usuario = schema.Usuario.query.filter_by(email=email).first()
        if usuario:
            print("Encontrado")
            if usuario.check_senha(senha):
                return jsonify({'mensagem':'Sucesso'})
            return jsonify({'mensagem':'erro'})
        else:
            print("Usuário não encontrado")
            return jsonify({'mensagem':'erro'})
