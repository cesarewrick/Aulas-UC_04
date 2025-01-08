#Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7. Construa um programa que leia um número inteiro positivo e determine se ele é primo ou não.  
 
numero = int(input("Digite o número inteiro: "))
contador = 0
 
for i in range (1,numero+1):
    if (numero % i == 0):
        contador = contador+1
    print(i)
if(contador==2):    
    print (f'O número {numero} é primo')
else:
    print(f'O número {numero} não é primo')