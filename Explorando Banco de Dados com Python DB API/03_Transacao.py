import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "cliente.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", ("Teste3", "teste3@gmail.com"))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)", (2, "Teste4", "teste4@gmail.com"))
    cursor.execute("DELETE FROM clientes WHERE id = 1")
    conexao.commit()
except Exception as exc:
    print(f"Ops! um erro ocorreu! {exc}" )
    conexao.rollback()