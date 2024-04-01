import numpy as np

# mostre quais são as diferentes Regiões do planeta segundo este dataset;

# CARREGANDO UM DATASET
dataset = np.loadtxt('paises.csv', delimiter = ';', dtype = str, encoding='utf-8', skiprows = 1)

regions = np.unique(dataset[:, 1])
print(regions)