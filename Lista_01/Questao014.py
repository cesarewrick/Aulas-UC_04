import random

nomes = []

while True:
    nome = input("Digite um nome (ou 'sair' para finalizar):")

    if nome.lower() == 'sair':
        break

    nomes.append(nome)

if nomes:
    nome_sorteado = random.choice(nomes)
    print("O nome sorteado foi:", nome_sorteado)
else:
    print("Nenhum nome foi fornecido para o sorteio.")