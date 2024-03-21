import numpy as np

# Define semente (seed)
np.random.seed(10)

# matiz de numeros inteiros entre 1 50
mtz = np.random.randint(1, 50, 16)  # 16 numeros aleatorios entre 1 e 50
mtz = mtz.reshape(4, 4)  # transformando em uma matriz 4x4
print(mtz)

# #qtd de vezes que cada numero aparece
unique_num, counts = np.unique(mtz, return_counts=True)
print(unique_num)

# Mostra a quantidade de aparições de cada número
for num, count in zip(unique_num, counts):
    print(f"Numero {num} aparece {count} vezes")

# Mostra apenas os números que aparecem duas vezes
print("\nNumeros que aparecem duas vezes:")
for num, count in zip(unique_num, counts):
    if count == 2:
        print(num)
