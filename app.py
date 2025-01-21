import sqlite3

# Conectando ao banco de dados
Banquinho = sqlite3.connect('meu_banco.db')
cursor = Banquinho.cursor()

# Criar tabela
def criar_tabela(Banquinho, cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL
    );
    ''')
    Banquinho.commit()

# Inserir dado
def inserir_dado(Banquinho, cursor, nome, id):
    data = (id, nome)
    cursor.execute('INSERT INTO clientes (id, nome) VALUES (?, ?);', data)
    Banquinho.commit()

# Alterar registro
def alterar_registro(Banquinho, cursor, nome, id):
    data = (nome, id)
    cursor.execute('UPDATE clientes SET nome=? WHERE id=?;', data)
    Banquinho.commit()

# Excluir registro
def excluir_registro(Banquinho, cursor, id):
    data = (id,)
    cursor.execute('DELETE FROM clientes WHERE id=?;', data)
    Banquinho.commit()

# Chamando as funções para testar
criar_tabela(Banquinho, cursor)  # Cria a tabela se não existir
inserir_dado(Banquinho, cursor, "João", 1)  # Insere um cliente
alterar_registro(Banquinho, cursor, "Maria", 1)  # Altera o nome do cliente
excluir_registro(Banquinho, cursor, 1)  # Exclui o cliente
