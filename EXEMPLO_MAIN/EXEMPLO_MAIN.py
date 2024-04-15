import numpy as np

# QUESTAO 1
musicas = []
nome = ""
ano = ""
cont = 0

while True:
    nome = input("Entre com o nome da musica: ")
    ano = input("Entre com o ano da musica: ")
    infos = {"nome" : nome, "ano" : ano}
    musicas.insert(cont, infos)
    cont += 1
    flag = int(input("Entre com 1 para adicionar mais musicas ou 0 para sair: "))
    if flag == 0:
        break

musicas = np.array(musicas)

print("")
print("Questão 1")

# 1A
print("")
print(f"Número de músicas adicionadas: {len(musicas)}")

# 1B
menor = musicas[0]
for aux in musicas:
    if aux["ano"] < menor["ano"]:
        menor = aux

print("")
print(f"Informações da música mais antiga: {menor}")

# QUESTAO 2
# 2A
nomes1 = np.array(["Lucas", "Bruno", "Allan", "Savio"])
nomes2 = np.array(["Thiago", "Fernando", "Guilherme", "Ian"])

# 2B
nomes = np.concatenate([nomes1, nomes2])

# 2C
nomes = nomes.reshape(2, 4)

# 2D
nomes = nomes.reshape(1, 8)
nomes = np.sort(nomes)
nomes = np.flip(nomes)
nomes = nomes.reshape(2, 4)

print(f"\n")
print("Questão 2")
print("")
print("Nomes em ordem decrescente:")
print(nomes)

# QUESTAO 3
colors = [
    {"color":"black","type":"primary","code":{"rgba":[255,255,255,1],"hex":"#000"}}, 
    {"color":"green","type":"secondary","code":{"rgba":[0,255,0,0.1],"hex":"#0F0"}}, 
    {"color":"yellow","type":"primary","code":{"rgba":[255,255,0,0.7],"hex":"#FF0"}}, 
    {"color":"blue","type":"primary","code":{"rgba":[0,0,255,1],"hex":"#00F"}}
]

print(f"\n")
print("Questão 3")

# 3A
print("")
print("Nome das cores primárias:")
for aux in colors:
    if aux["type"] == "primary":
        print(aux["color"])

# 3B
print("")
print("Códigos hexadecimais das cores com B == 255:")
for aux in colors:
    if aux["code"]["rgba"][2] == 255:
        print(aux["code"]["hex"])

# 3C
arr = []
for aux in colors:
    arr.append(aux["color"])
    arr.append(aux["code"]["hex"])

arr = np.array(arr)

# 3D
arr = arr.reshape(4,2)

# 3E
arr = np.char.replace(arr, "black", "preto")
arr = np.char.replace(arr, "green", "verde")
arr = np.char.replace(arr, "yellow", "amarelo")
arr = np.char.replace(arr, "blue", "azul")

print("")
print("Cores traduzidas para o Português:")
print(arr)
