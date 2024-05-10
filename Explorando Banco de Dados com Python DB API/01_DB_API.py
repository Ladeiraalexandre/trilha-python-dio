import sqlite3
from pathlib import Path

#colocar o nome do banco a ser criado... um padrão que utilizam tbem é cliente.sqlite... db acho melhor
#ele cria um arquivo na raiz do projeto
'''con = sqlite3.connect("cliente.db")
print(con);'''

#para criar no caminho raiz do diretorio do projeto, utilizar :
ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "cliente.db")
cursor = conexao.cursor()

def cria_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, NOME varchar(100), email VARCHAR(150))"
    )

#EXEMPLO A SEGUIR, PODE GERAR UM SQL iNJECTION, colocando um codigo dentro de uma inserção/atualização de valor
'''
nome = "Alexandre"
email = "testes@gmail.com 1=1 drop table clientes" #exmeplo de injeção
cursor.execute(f"INSERT INTO clientes (nome, email) VALUES ('{nome}','{email}');")
#o problema de utilizar passando as variavesi no parametro'''

#como fazer para evitar sql injection no Python: querys preparadas 
def insere_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()
#colocamos ?, o que significa que vc ira passar uma tupla de parametros, aqui chamei de data

def atualiza_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes set nome=?, email=? WHERE id=?;", data)
    conexao.commit()
    
def deleta_registro(conexao, cursor, id):
    data = (id,) #tupla de um unico valor, tem que colocar uma virgula
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()

def insere_varios(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
    conexao.commit()                   


dados = [
    ('Ale', 'xandre@gmail.com'),
    ('Alee', 'xan@gmail.com'),
    ('Lucao', 'lucas@gmail.com'),
]

def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes;")
    #return cursor.fetchall()
    
#utilizando row_factory... tem uma saida interessante
def recuperar_cliente2(cursor, id):
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()
       
#atualiza_registro(conexao, cursor, "Alexandre L", "testes@gmail.com", 1)
#insere_registro(conexao, cursor, "Euclydes", "junior@gmail.com")
#deleta_registro(conexao, cursor, 9)
#insere_varios(conexao, cursor, dados)
'''cliente = recuperar_cliente(cursor, 2)
print(cliente)'''


'''cliente2 = recuperar_cliente2(cursor, 2)
print(dict(cliente2))
'''

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)