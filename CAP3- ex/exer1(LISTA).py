#lista

lista = ['Real Madrid','Milan','Bayern','Barcelona','Inter de Milão']
#Letra a
print(lista[:3])

#letra b
print(lista[3:5])

#letr c
lista_ordenada = sorted(lista)
print(lista_ordenada)

#letra d
time = 'Barcelona'
posicao = lista.index(time)
print("O Barcelona está na posição: ", posicao)