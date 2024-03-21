import numpy as np

#Definimos a semente (seed)
np.random.seed(5)
#criar um array de 10 nº aleatoios para ente 0 e 1 (positivo e negativo)
arr = (np.random.rand(10) - 0.5) * 2

#multiplicar os valores por 100
arr *=100
print(arr)

#criando uma parte inteira apenas com a parte inteira
arr_int =  np.floor(arr).astype(int)
print("Array de inteiros:")
print(arr_int)
