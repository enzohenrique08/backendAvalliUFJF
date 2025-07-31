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
    
    @staticmethod
    def BuscarAvaliacaoGeralProfessor():
        professor_id = request.args.get('professor_id')
        avaliacoes_professor = schema.Avaliacao.query.filter_by(professor_id=professor_id).all()
        notas1 = 0
        notas2 =0
        notas3 =0
        comentarios=[]
        for avaliacao in avaliacoes_professor:
            notas1+=avaliacao.nota1
            notas2+=avaliacao.nota2
            notas3+=avaliacao.nota3
            if avaliacao.comentario:
                comentarios.append(avaliacao.comentario)
        medianota1 = int(notas1)/len(avaliacoes_professor)
        medianota2 = int(notas2)/len(avaliacoes_professor)
        medianota3 = int(notas3)/len(avaliacoes_professor)

        return jsonify({"medianotas1":medianota1,
                        "mediasnota2":medianota2,"medianota3":medianota3,"comentarios":comentarios})

    