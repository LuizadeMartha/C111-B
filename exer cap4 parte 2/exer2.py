import numpy as np

# Define semente (seed)
np.random.seed(10)

# matiz de numeros inteiros entre 1 50
mtz = np.random.randint(1, 50, 16)  # 16 numeros aleatorios entre 1 e 50
mtz = mtz.reshape(4, 4)  # transformando em uma matriz 4x4
print(mtz)

