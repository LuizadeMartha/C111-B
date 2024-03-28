import numpy as np

# Carregando dataset
arr = np.loadtxt('C:/Users/luiza/PycharmProjects/ProjetoC11B/EXER ENTREGUES/exer cap4 parte 3/space.csv', delimiter=';', dtype=str, encoding='utf-8')


#mostrar quantas missoes deram certo
sucesso = arr[arr[:, 7] == 'Success']
print(sucesso.shape[0])