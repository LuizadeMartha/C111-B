# NumPy
import numpy as np
'''
#criando um NumPy Array
# 1-Dimensão
arr = np.array([1,2,3,4])
print(arr) #mostrar numero da lista
print(type(arr)) #mostrar oq ele entendeu, se realmente é um Numpy


# 2 - dimensões
mtz = np.array([[1,2], [3,4]])
print(mtz)

# Estruturando NumPy Arrays Automaticamente
mtz = np.ones(9). reshape(3,3) #criabdo um vetor com 9 um. tranformando em uma matriz 3:3
print(mtz)

#zeros
#arange
mtz = np.arange(9) # de zero ate 8
print(mtz)

mtz = np.arange(10, 20, 2) # 10 á 20 pulando de 2 em 2
print(mtz)

'''

#Operando Elemento a elemento
arr1 = np.arange(10, 20, 1)
arr2 = np.arange(30, 40, 1)

print(arr1)
print(arr2)
print(arr1+arr2)#somando os dois Arrays
print(np.concatenate([arr1, arr2])) #juntando os dois

#Propriedades de um numpyArray
#Tamanho
print(arr1.size)
#dimensão
print(arr1.ndim)
#formato
print(arr1.shape)

