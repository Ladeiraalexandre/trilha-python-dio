from pathlib import Path
ROOT_PATH = Path(__file__).parent #pega a raiz do caminho do arquivo

try:
    arquivo = open(ROOT_PATH / "novo_diretorio" / "meu_arquivo.txt", "r")
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc)
except  IsADirectoryError as exc:
    print(f"Diretorio não encontrado: {exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    print(f"Algum problem ocorreu ao tentar abrir o arquivo: {exc}")
