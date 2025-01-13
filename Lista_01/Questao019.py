numeros = []

while True:
    entrada = input("Digite um número (ou 'sair' para finalizar): ")
    
    if entrada.lower() == 'sair':
        break
    
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número válido.")

produto = 1
for numero in numeros:
    produto *= numero

print("O produto dos números fornecidos é:", produto)
