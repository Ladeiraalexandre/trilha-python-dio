'''Usar barras invertidas cruas (raw strings): Adicionar um r antes das aspas de abertura do caminho do arquivo
faz com que o Python interprete o caminho como uma "string bruta", 
o que significa que os caracteres de escape não são processados. Por exemplo:'''
arquivo = open (r"C:\Users\User\Downloads\BootCamp_Vivo\Python\Manipulando arquivos em Python\lorem.txt", "r")

print(arquivo.read()) #le todo o conteudo de uma vez só
print(arquivo.readline()) #le linha a linha
print(arquivo.readlines()) #le carrega numa lista
arquivo.close()