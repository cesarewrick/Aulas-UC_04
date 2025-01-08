# Faça um programa em Python que  calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.
 
# idade = int(input('Digite sua idade: '))
# ano_atual = int(input('Digite o ano atual: '))
# resposta = ano_atual - idade
# print (f'Seu ano de nascimento é {resposta}.')
 
# Crie um programa que receba um número inteiro digitado pelo usuário e informe se ele é par ou ímpar.
# num1 = int(input('informe um numero inteiro de sua preferencia: '))
# if (num1%2==0):
#     print('o numero é par')
# else:
#     print('o numero é impar')
 
# Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.
# valorA = int(input("Digite o valor A:"))
# valorB = int(input("Digite o valor B:"))
# if(valorA%valorB==0) or (valorB%valorA==0):
#     print(f"Os valores {valorA} e {valorB} são múltiplos. ")
# else:
#     print(f"Os valores {valorA} e {valorB} não são múltiplos. ")
 
#Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7. Construa um programa que leia um número inteiro positivo e determine se ele é primo ou não.  
 
# numero = int(input("Digite o número inteiro: "))
# contador = 0
 
# for i in range (1,numero+1):
#     if (numero % i == 0):
#         contador = contador+1
#     print(i)
# if(contador==2):    
#     print (f'O número {numero} é primo')
# else:
#     print(f'O número {numero} não é primo')
 
#Elabore um programa que, dado um valor de temperatura (em graus Celsius), informe se o clima é "frio" (abaixo de 15°C), "ameno" (entre 15°C e 30°C, inclusive) ou "quente" (acima de 30°C).
# Entrada: Um valor numérico representando a temperatura.
# Saída: Uma mensagem classificando o clima como "frio", "ameno" ou "quente".
 
# numero = float(input('Digite a temperatura:'))
# if (numero<15):
#     print(f'Clima Frio {numero}')
# elif(numero>=15 and numero<=30):
#     print(f'Clima Ameno {numero}')
# else:
#     print(f'Clima Quente {numero}')
 
# Escreva um programa que calcule o valor final de uma compra, aplicando um desconto de 10% caso o valor da compra seja maior que R$100.
# Entrada: O valor total da compra antes do desconto.
# Saída: O valor final da compra, formatado com duas casas decimais.
 
valorCompra = float(input('Digite o valor total da compra: '))
if(valorCompra>100):
    #novoValor = valorCompra - valorCompra*0.1
    valorCompra*=0.9
    print(f'Novo Valor com desconto = {valorCompra}')
else:
    print(f'O desconto não pode ser aplicado. Total = {valorCompra}') 