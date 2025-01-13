soma_pares = 0


while True:
    num = int(input("Digite um numeros inteiro (0 para parar): "))

    if num == 0 :
        break
    if num %2 == 0:
        soma_pares += num

print("A soma dos números digitados é:", soma_pares)