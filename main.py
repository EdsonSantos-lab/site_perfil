from flask import Flask, render_template, url_for

app = Flask(__name__)
lista_usuarios = 'são', 'pf', 'nanfo', 'pufu', 'carlos',

@app.route("/")
def capa():
    return render_template('capa.html')
@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')


if __name__ == '__main__':
    app.run(debug=True)