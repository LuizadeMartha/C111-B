import np
import numpy as np

#Conte quantos países são da América do Norte (NORTHERN AMERICA) segundo este dataset;

# CARREGANDO UM DATASET
dataset = np.loadtxt('paises.csv', delimiter = ';', dtype = str, encoding='utf-8', skiprows = 1)

stripped_regions = np.char.strip(dataset[:, 1])

america_norte = np.count_nonzero(stripped_regions == 'NORTHERN AMERICA')

print(america_norte)