from flask import jsonify, request
from app.models import schema
class Professores:
    @staticmethod
    def listar_professores():
        professores = schema.Professor.query.all()
        nomes = []
        for nome in professores:
            nomes.append(nome.nome)
        return jsonify({"professores":nomes}) 
    @staticmethod
    def list_professores_por_nome():
        professor_nome = request.args.get('professor_nome')
        professores = schema.Professor.query.filter(schema.Professor.nome.like('%'+professor_nome+'%')).all()
        nomes = []
        for nome in professores:
            nomes.append(nome.nome)
        return jsonify({"professores":nomes})         