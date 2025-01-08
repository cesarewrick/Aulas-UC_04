produtos = []
while True:
    entrada = input("Nome do produto: ")
    if entrada == 'sair':
        break
    entrada2 = float(input("Preço: "))
    entrada3 = int(input("Quantidade: "))
    
    produtos.append({"nome":entrada, "Preço": entrada2, "Quantidade":entrada3})
print (produtos)