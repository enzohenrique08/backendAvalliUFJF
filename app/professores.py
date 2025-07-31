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
        professores = schema.Professor.query.filter(schema.Professor.nome.ilike('%'+professor_nome+'%')).all()
        nomes = []
        for nome in professores:
            nomes.append(nome.nome)
        return jsonify({"professores":nomes})    
    @staticmethod
    def rejeitar_professor():
        professor_id = request.form.get('professor_id')
        aluno_id = request.form.get('aluno_id')
        if not professor_id or not aluno_id:
            return jsonify({'mensagem':'erro'})
        docente_sem_vinculo = schema.Docentesemvinculo(aluno_id,professor_id)
        docente_sem_vinculo.salvar()
        return jsonify({'mensagem':'Sucesso'})
    @staticmethod
    def buscar_cards_professor():
        aluno_id = request.args.get('aluno_id')
        curso = request.args.get('curso')
        lista_professores = schema.Professor.query.filter_by(curso=curso).all()
        Docentesemvinculo = schema.Docentesemvinculo.query.with_entities(schema.Docentesemvinculo.professor_id).filter_by(aluno_id=aluno_id).all()
        ids_docentes_sem_vinculo = [doc.professor_id for doc in Docentesemvinculo]
        lista_professores_filtrada = [prof for prof in lista_professores if prof.id not in ids_docentes_sem_vinculo]
        professores_json = [
    {
        'id': prof.id,
        'nome': prof.nome
    }
    for prof in lista_professores_filtrada
]
        return jsonify({'professores':professores_json})



