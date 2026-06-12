from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "bienvenido al sistema ";

@app.route("/saludo")
def saludo():
    return "hola aprendiz ADSO"

@app.route("/inventario")
def inventario():
    return "sistema inventario activo"

@app.route("/usuarios")
def usuarios():
    return "sistema usuarios activo"

app.run(debug=True)