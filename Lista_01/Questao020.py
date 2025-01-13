lista_presenca = []

while True:
    nome = input("Digite um nome (ou 'sair' para finalizar): ")
    
    if nome.lower() == 'sair':
        break
    
    lista_presenca.append(nome)

palavra_busca = input("Digite a palavra a ser buscada: ").lower()

nomes_encontrados = []

for nome in lista_presenca:
    if palavra_busca in nome.lower():
        nomes_encontrados.append(nome)

if nomes_encontrados:
    print("Os nomes que contêm a palavra '{}' são:".format(palavra_busca))
    for nome in nomes_encontrados:
      print(nome)

else:
    print("Nenhum nome contém a palavra '{}'.".format(palavra_busca))
