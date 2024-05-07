import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

COLUNA_ID = 0
COLUNA_NOME = 1

try:
    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as csvFile:
        escritor = csv.writer(csvFile) #le o arquivo como um dicionário
        escritor.writerow(["id", "nome"])
        escritor.writerow(["1", "Maria"])
        escritor.writerow(["2", "João"])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")
    
# try:
#     with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as csvFile:
#         leitor = csv.reader(csvFile) #le o arquivo como um dicionário
#         for idx, row in enumerate(leitor):
#             if idx == 0:
#                 continue
#             print(f"ID: {row[COLUNA_ID]}")
#             print(f"Nome: {row[COLUNA_NOME]}")
# except IOError as exc:
#     print(f"Erro ao criar o arquivo. {exc}")
try:
     with open(ROOT_PATH / "usuarios.csv", newline="") as csvFile:
         reader = csv.DictReader(csvFile) #le o arquivo como um dicionário
         for row in reader:
             print(f"ID: {row['id']}")
             print(f"Nome: {row['nome']}")
except IOError as exc:
     print(f"Erro ao criar o arquivo. {exc}")