from pathlib import Path

ROOT_PATH = Path(__file__).parent

#exemplo onde vc deve fechar o arquivo de forma manual, com o close()
try:
    arquivo = open(ROOT_PATH / "lorem.txt", "r")
    arquivo.close()
    print(arquivo.read())
except ValueError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")


#quando usado o with, ele faz o close do arquivo quando caso ocorra algum erro na leitura e quando terminar de realizar a leitura/gravação
with open(ROOT_PATH / "lorem.txt", "r") as arquivo: 
    print(arquivo.read())
    

#tratamento ao criar um arquivo
try:
    with open(ROOT_PATH / "arquivo.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Aprendendo a manipular aquivos em Python") 
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")