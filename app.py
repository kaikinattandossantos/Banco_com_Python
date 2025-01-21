import sqlite3
Banquinho = sqlite3.connect('meu_banco.db')

cursor = Banquinho.cursor()

def criar_tabela(Banquinho, cursor):
    cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR (50))')

def inserir_registro(Banquinho, cursor, nome, id):
    data = ("Kaiki",)
    cursor.execute('INSERT INTO clientes (nome) VALUES (?);', data)
    #não concatenar, mas usar comandos preparados

def alterar_registro(Banquinho, cursor, nome, id):
    data = ("Jesus",)
    cursor.execute('UPDATE clientes SET nome=? WHERE id=?;', data)

alterar_registro(Banquinho, cursor, "Jesus", 1)

Banquinho.commit()