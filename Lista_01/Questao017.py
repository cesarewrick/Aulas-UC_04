palavra = input("Digite uma palavra: ").lower()

vogais = "aeiou"

contador_vogais = 0

for letra in palavra:
    if letra in vogais:
        contador_vogais += 1

print("O número de vogais na palavra é:", contador_vogais)
