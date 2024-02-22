#colecoes
from typing import List

#tuplas
# # É uma colecao imutavel

#nomes = ('Goku', 'Vegeta', 'trunks', 'Gohan')
#print(nomes)
#nomes[0] = 'Picolo'
#Slicing de dados
# print(nomes[0])
# print(nomes[:2])
# print(nomes[1:3])
# print(nomes[-2])

#Lista
#coleção mutavel
# nomes = ['Goku','Vegeta','Trunks','Gohan']
# #ADD
# nomes.append('Picolo')
# #UPDATE
# nomes[0] = 'Bulma'
# #DELETE
# nomes.remove("Trunks") #remoção por valor
# del nomes[1] #remocao pot indice
# #SELECT
# print(nomes)

#CONJUNTO
#Não guada ordem dos elementos
#Não guarda elementos repetidos
#N TEM UPDATE
# nomes = {'Goku','Vegeta','Trunks','Gohan'}
# #ADD
# nomes.add('Bulma')
# nomes.add('Goku')
# #SELECT
# print(nomes)
# #DELETE
# nomes.remove('Trunks')
# #UPDATE (N TEM)


#DICIONARIO
#USA INDICES CUSTOMIZADOS
pessoa = {
    'nome': 'Goku',
    'idade': 42
}

#ADD
pessoa['sexo'] = 'M'
#DELETE
del pessoa['sexo']
#UPDATE
pessoa['nome'] = 'Gohan', pessoa['idade']
print(pessoa)



pessoa2 = {
    'nome': 'Bulma',
    'idade': 32
}

#colecao dentro de colecao
# pessoas = [pessoa, pessoa2]
# print(pessoas[0]['nome'])
# print(pessoas[0]['idade'])
# print(pessoas[1]['nome'])



