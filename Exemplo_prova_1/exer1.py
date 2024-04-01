import numpy as np

#exer 1
#Faça um slicing no dataset para mostrar apenas o País (Country),
# Região (Region), População (Population) e Area (Area (sq. mi.)) dos países contidos nele;


# CARREGANDO UM DATASET
dataset = np.loadtxt('paises.csv', delimiter = ';', dtype = str, encoding='utf-8')
arr = dataset[:, [0,1,2,3]]
print(arr)



