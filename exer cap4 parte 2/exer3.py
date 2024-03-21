import numpy as np

# Define semente (seed)
np.random.seed(10)

# matiz de numeros inteiros entre 1 50
mtz = np.random.randint(1, 50, 16)  # 16 numeros aleatorios entre 1 e 50
mtz = mtz.reshape(4, 4)  # transformando em uma matriz 4x4
print("Matriz:")
print(mtz)

# Calcula a média das linhas e colunas
print("media da coluna: ")
media_coluna =np.mean(mtz, axis =0)
print(media_coluna)
print("media da linha: ")
media_linha =np.mean(mtz, axis =1)
print(media_linha)

# Encontra o maior valor entre as médias das linhas e das colunas
maior_mediaC = np.max(media_coluna)
print("Maior valor da coluna:")
print(maior_mediaC)
print("Maior media da linha")
maior_mediaL = np.max(media_linha)
print(maior_mediaL)
