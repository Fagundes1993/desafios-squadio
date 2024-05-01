# Desafio
# Você é um intrépido explorador em uma jornada por uma terra desconhecida repleta de desafios emocionantes.
# Ao se deparar com uma floresta misteriosa, você percebe que a única maneira de atravessá-la é desvendando seus caminhos por meio de um código em Python.
# Prepare-se para a "Aventura do Explorador"!

# Entrada
# Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo, representando a quantidade de passos que o explorador deve dar na floresta. .

# Saída
# O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta.
# Utilize um laço de repetição para simular os passos do explorador.
# A cada passo, imprima uma mensagem informando a distância percorrida até o momento.

# Exemplos
#Entrada: 2

#Saída:

# Explorador: 1 passo
# Explorador: 2 passos

# Entrada
quantidade_passos = int(input())

#Teste
if quantidade_passos <= 0:
    print("Nenhum passo dado na floresta.")
else:
    # Loop para simular os passos do explorador
    print(f"Explorador: 1 passo")
    for i in range(2, quantidade_passos + 1):
        print(f"Explorador: {i} passos")