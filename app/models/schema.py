from app import db
from werkzeug.security import generate_password_hash, check_password_hash

# Classe base para usuários (abstrata)
class Usuario(db.Model):
    def __init__(self):
        self.email = 'a'
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)
    tipo = db.Column(db.String(50))  # 'aluno' ou 'administrador'

    __mapper_args__ = {
        'polymorphic_identity': 'usuario',
        'polymorphic_on': tipo
    }

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_senha(senha):
        return check_password_hash(password=senha,pwhash=generate_password_hash(senha))

# Classe Aluno (herda de Usuario)
class Aluno(Usuario):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    curso = db.Column(db.String(100))

    avaliacoes = db.relationship('Avaliacao', backref='aluno', lazy=True)

    __mapper_args__ = {
        'polymorphic_identity': 'aluno',
    }

# Classe Administrador (herda de Usuario)
class Administrador(Usuario):
    __tablename__ = 'administradores'

    id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'administrador',
    }

# Classe Professor
class Professor(db.Model):
    __tablename__ = 'professores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    avaliacoes = db.relationship('Avaliacao', backref='professor', lazy=True)
    disciplinas = db.relationship('DisciplinaProfessor', back_populates='professor')

# Classe Disciplina
class Disciplina(db.Model):
    __tablename__ = 'disciplinas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    professores = db.relationship('DisciplinaProfessor', back_populates='disciplina')

# Tabela associativa entre Professor e Disciplina (N:N)
class DisciplinaProfessor(db.Model):
    __tablename__ = 'disciplina_professor'

    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), primary_key=True)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'), primary_key=True)

    professor = db.relationship('Professor', back_populates='disciplinas')
    disciplina = db.relationship('Disciplina', back_populates='professores')

# Classe Avaliacao
class Avaliacao(db.Model):
    __tablename__ = 'avaliacoes'

    id = db.Column(db.Integer, primary_key=True)
    nota1 = db.Column(db.Integer, nullable=False)
    nota2 = db.Column(db.Integer, nullable=False)
    nota3 = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.Text)
    
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'), nullable=False)

    def media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3
