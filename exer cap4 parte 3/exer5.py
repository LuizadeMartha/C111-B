import numpy as np

# Carregando dataset
arr = np.loadtxt('C:/Users/luiza/PycharmProjects/ProjetoC11B/EXER ENTREGUES/exer cap4 parte 3/space.csv', delimiter=';', dtype=str, encoding='utf-8')

# Pular a primeira linha (cabeçalho)
data = arr[1:]

# Criar um dicionário para armazenar as contagens de missões por empresa
contagem_missões_por_empresa = {}

# Iterar pelos dados e contar as missões por empresa
for linha in data:
    empresa = linha[1]  # A empresa está na coluna de índice 1
    if empresa in contagem_missões_por_empresa:
        contagem_missões_por_empresa[empresa] += 1
    else:
        contagem_missões_por_empresa[empresa] = 1

# Mostrar as informações
for empresa, quantidade in contagem_missões_por_empresa.items():
    print(f"A empresa '{empresa}' realizou {quantidade} missioes espaciais.")