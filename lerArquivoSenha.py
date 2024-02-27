import os

os.system('cls' if os.name == 'nt' else 'clear')

# with open("config.txt", "r") as file:
#     user = file.readline().strip()
#     pwd = file.readline().strip()

dict_config = {}

arquivo = open("config.txt", "r")
linha = arquivo.readline()
while linha != "":
    chave, conteudo = linha.split(":")
    dict_config[chave] = conteudo
    linha = arquivo.readline()
arquivo.close()   
print(dict_config["una"])
print(dict_config["linha02"])
