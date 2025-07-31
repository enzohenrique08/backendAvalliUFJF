from flask import jsonify, request
from app.models import schema
class Avaliacao:
    @staticmethod
    def Avaliar():
        nota1=request.form.get('nota1')
        nota2=request.form.get('nota2')
        nota3=request.form.get('nota3')
        aluno_id =  request.form.get('aluno_id')
        professor_id = request.form.get('professor_id')
        disciplina_id = request.form.get('disciplina_id')

        comentario = request.form.get('comentario')
        avaliacao = schema.Avaliacao(nota1=nota1,nota2=nota2,nota3=nota3,comentario=comentario,disciplina_id=disciplina_id,aluno_id=aluno_id,professor_id=professor_id)
        avaliacao.salvar()
        return jsonify({'mensagem':'Sucesso'})
