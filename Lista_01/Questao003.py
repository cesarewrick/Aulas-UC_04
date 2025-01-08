#Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

valorA = int(input("Digite o valor A:"))
valorB = int(input("Digite o valor B:"))
if(valorA%valorB==0) or (valorB%valorA==0):
    print(f"Os valores {valorA} e {valorB} são múltiplos. ")
else:
    print(f"Os valores {valorA} e {valorB} não são múltiplos. ")