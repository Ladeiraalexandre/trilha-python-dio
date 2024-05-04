arquivo = open(r"C:\Users\User\Downloads\BootCamp_Vivo\Python\Manipulando arquivos em Python\arquivoGerado.txt", "w")

arquivo.write('Escrevendo dados em um novo arquivo') #esceve todo texto de uma só vez
arquivo.writelines("Python") #escreve um caracter por vez... itera sobre o conteudo
arquivo.close()