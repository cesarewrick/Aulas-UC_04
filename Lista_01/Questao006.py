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