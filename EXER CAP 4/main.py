# NumPy Array
import numpy as np

# 1
arr = np.linspace(0, 1, 21)
print(arr)
print(type(arr))

#2
arr1 = np.arange(0, 51, 2) # 0 á 51 pulando de 2 em 2
arr2 = np.arange(100, 50, -2) # 100 á 50 pulando de 2 em 2
concatenated_array = np.concatenate([arr1, arr2])  # Juntando os dois arrays
sorted_array = np.sort(concatenated_array)  # Ordenando em ordem crescente

print(arr1)
print(arr2)
print(concatenated_array)

#3

sorted_array = np.sort(concatenated_array)   # Ordenando em ordem crescente
print(sorted_array)

#4
arr = np.ones([3,4])
print(arr)
arr_res = arr.reshape(1,12)
print(arr_res)

#5

lenLines = np.random.randint(1, 5)
lenColumns = np.random.randint(1, 5)
arr = np.random.rand(lenLines, lenColumns)

arrShape = arr.shape
print(arrShape)
arrMult = arrShape[0] * arrShape[1]

if arrMult % 2 == 0:
    print("Vetor de tamanho par")
else:
    print("Vetor de tamanho ímpar")