from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicial():
    return "Olá Web"

if __name__ == '__main__':
    app.run(debug=True)
