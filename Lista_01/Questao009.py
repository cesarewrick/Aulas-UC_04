idade_soma = 0
while True:
    idade = int(input("Digite sua idade: "))
    if idade == 0:
        break
    idade_soma+=idade
print (idade_soma)