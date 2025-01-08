#Faça um programa em Python que  calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.
 
idade = int(input('Digite sua idade: '))
ano_atual = int(input('Digite o ano atual: '))
resposta = ano_atual - idade
print (f'Seu ano de nascimento é {resposta}.')