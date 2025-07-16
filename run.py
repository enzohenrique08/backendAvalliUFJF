from app import create_app, login

app = create_app()
app.add_url_rule('/usuario',view_func=login.Login.autenticar)

if __name__ == "__main__":
    app.run(debug=True)