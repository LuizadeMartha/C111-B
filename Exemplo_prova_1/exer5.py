import  numpy as np

#Encontre qual país da América do Sul e Caribe (LATIN AMER. & CARIB) possui a maior renda per capita (GDP ($ per capita));

# CARREGANDO UM DATASET
dataset = np.loadtxt('paises.csv', delimiter = ';', dtype = str, encoding='utf-8', skiprows = 1)
stripped_regions = np.char.strip(dataset[:, 1])

america_sul_caribe = dataset[stripped_regions == 'LATIN AMER. & CARIB']
gdp = america_sul_caribe[:, 8].astype(float)
max_gdp = np.argmax(gdp)
pais = america_sul_caribe[max_gdp, 0]
print(pais)