import numpy as np

# Carregando dataset
arr = np.loadtxt('C:/Users/luiza/PycharmProjects/ProjetoC11B/EXER ENTREGUES/exer cap4 parte 3/space.csv', delimiter=';', dtype=str, encoding='utf-8')

# Pular a primeira linha (cabeçalho)
data = arr[1:]

# Filtrar missões realizadas pela SpaceX
spacex_missions = data[data[:, 1] == 'SpaceX']

# Encontrar a missão mais cara
max_cost_index = np.argmax(spacex_missions[:, 6].astype(float))
most_expensive_mission = spacex_missions[max_cost_index]

print("A missao mais cara da SpaceX foi:", most_expensive_mission)