#Criando um dicionario para armazenar os dados
alunos = {}

while True:
    #Entrando com as infos
    nome = input("Entre com o nome do aluno, ou digite 1 para encerrar.")
    # Verificando se o usuário deseja encerrar a entrada de dados
    if nome.lower()== "1":
        break

    # Entrando com a média do aluno
    media = float(input("Ente com a média do aluno:"))

    # Determinando se o aluno foi aprovado ou reprovado
    final = "AP" if media >= 60 else 'RP'

    # Armazenando as informações do aluno no dicionário
    alunos[nome] = {"media": media,"final": final}

# Exibindo as informações dos alunos
print("\nInformações dos Alunos: ")
for  nome, dados in alunos.items():
    print(f"Nome do Aluno: {nome}, Média: {dados['media']}, Final: {dados['final']}")


