import numpy as np

# Carregando dataset
arr = np.loadtxt('C:/Users/luiza/PycharmProjects/ProjetoC11B/EXER ENTREGUES/exer cap4 parte 3/space.csv', delimiter=';', dtype=str, encoding='utf-8')


# Pular a primeira linha (cabeçalho)
data = arr[1:]

# Converter a coluna "cost" em um array de floats
costs = data[:, 6].astype(float)

# Filtrar valores maiores que zero
positive_costs = costs[costs > 0]

# Calcular a média dos valores positivos de "cost"
media_cost = np.mean(positive_costs)

print("Media de 'cost' para missoes com valores > 0:", media_cost)