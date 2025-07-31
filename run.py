from app import create_app, login

app = create_app()
app.add_url_rule('/login',view_func=login.Login.autenticar,methods=['POST'])
app.add_url_rule('/criar-usuario',view_func=login.Login.criarUsuario,methods=['POST'])


if __name__ == "__main__":
    app.run(debug=True)