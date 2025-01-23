from flask import Flask

app = Flask(__name__)

@app.route("/", method=["POST"])
def inicial():
    return "Olá Web"


if __name__ == '__main__':
    app.run(debug=True)
