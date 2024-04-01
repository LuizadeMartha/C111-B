import numpy as np

# Mostre qual a taxa média de alfabetização (Literacy (%)) do planeta segundo este dataset;

# CARREGANDO UM DATASET
dataset = np.loadtxt('paises.csv', delimiter = ';', dtype = str, encoding='utf-8', skiprows = 1)

literacy = np.array(dataset[1:, 9], dtype=float)
print(round(np.mean(literacy), 2))