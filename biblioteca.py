import sqlite3

def connect(pdb):
    '''Conectar ao DB.
    param db: Nome do arqivo DB.'''
    return sqlite3.connect(pdb)

# Verificar se o DB já esta criado
try:
    conn = connect('biblioteca.db')
except:
    print('Erro ao se conectar ao DB')
finally:
    conn.close()

# Verificar se as tabelas estão criadas
try:
    # Conectar ao DB
    conn = connect('biblioteca.db')
    # Criar um cursor ao DB
    cursor = conn.cursor()
    # Criando a tabela de Livros
    cursor.execute("""CREATE TABLE IF NOT EXISTS livros (
        id_livro INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome_livro VARCHAR(255) NOT NULL,
        categoria VARCHAR(50) NOT NULL,
        cod_livro varchar(10) NOT NULL,
        qntd INTEGER NOT NULL);""")
    # Criando a tabela de Usuários
    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
        id_user INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50) NOT NULL,
        sobrenome VARCHAR(50) NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        email VARCHAR(60) NOT NULL);""")
    # Criando a tabela de Livros emprestados
    cursor.execute("""CREATE TABLE IF NOT EXISTS emprestimos (
        cpf INTEGER NOT NULL PRIMARY KEY,
        livro1 VARCHAR(255) NOT NULL,
        livro2 VARCHAR(255) NOT NULL,
        livro3 VARCHAR(255) NOT NULL
    );""")
    # Criando a tabela de categorias dos livros
    cursor.execute("""CREATE TABLE IF NOT EXISTS categorias (
        id_cat INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome_cat VARCHAR(255) NOT NULL
    );""")
except:
    print('Erro ao criar as tabelas')
finally:
    conn.close()

conn = connect('biblioteca.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO categorias (nome_cat) VALUES ('Ficção científica')")
conn.commit()
conn.close()