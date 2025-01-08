#Elabore um programa que, dado um valor de temperatura (em graus Celsius), informe se o clima é "frio" (abaixo de 15°C), "ameno" (entre 15°C e 30°C, inclusive) ou "quente" (acima de 30°C).
# Entrada: Um valor numérico representando a temperatura.
# Saída: Uma mensagem classificando o clima como "frio", "ameno" ou "quente".
 
numero = float(input('Digite a temperatura:'))
if (numero<15):
    print(f'Clima Frio {numero}')
elif(numero>=15 and numero<=30):
    print(f'Clima Ameno {numero}')
else:
    print(f'Clima Quente {numero}')