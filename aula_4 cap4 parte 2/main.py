import numpy as np

#Numeros aleatorios usanmos (random)

# np.random.seed(10)#gerar os mesmos numeros aleatorios de outras maquinas
# arr = np.random.randint(10, 20, 5) #gerando 5 numeros aleatorios de 10 a 20
# print(arr)

#elementos unicos
# np.random.seed(5)
# arr = np.random.randint(0, 10, 15)
# print(arr)
# print(np.unique(arr))
# print(set(arr))

#Operação em matizes
# np.random.seed(10)
# mtz = np.random.randint(1, 11, 9).reshape(3, 3) #gerando um vetor / tranfromando em uma matriz
# print(mtz)# mtz = np.random.randint(1, 11, 9).reshape(3, 3) #gerando um vetor / tranfromando em uma matriz
# # print(mtz)
#coluna
# print(mtz.sum(axis=0)) #somando todas as colunas
# print(mtz.sum(axis=0)[0]) #somando so a primeira coluna
# #linha
# print(mtz.sum(axis=1)) #somando todas as linha
# print(mtz.sum(axis=1)[1]) #somando so a segunda linha
# #media
# print(mtz.mean(axis=0)[1]) #somando so a segunda coluna
# #multiplicando por dpos(broadcasting)
# print(mtz*2)

#CONDICIONAIS
#CRIANDO MATRIZ
np.random.seed(10)
mtz = np.random.randint(1, 11, 9).reshape(3, 3) #gerando um vetor / tranfromando em uma matriz
print(mtz)
#VERIFICAR ELEMNTOS PARES

arr = mtz[mtz%2==0]
print(arr)

# #verificar media/ depois saber qual elemntos da matiz e maior que a media
# cond = mtz[mtz>mtz.mean()]
# print(cond)

#trabalhando com textos (usamos char)
arr = np.array(['Gionani', 'Isaque', 'Luiza', 'Raissa']) #criando array de nomes
print(np.char.find(arr,'s')) #Buscando nomes com a letra S
arr2 = arr[np.char.find(arr,'s')>=0]#passando a condicionar para sair com os nomes
print(arr2)