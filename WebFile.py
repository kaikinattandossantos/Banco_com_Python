from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicial():
    return "Olá Web"

@app.route("/contatos/<nome>")
def página_de_contatos(nome):
    return f"<h1> Seu contato: {nome}<h1>" 

if __name__ == '__main__':
    app.run(debug=True)
