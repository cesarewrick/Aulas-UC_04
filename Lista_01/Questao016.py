notas = []

while True:
    nota = input("Digite a nota do aluno (ou 'sair' para finalizar): ")
    
    if nota.lower() == 'sair':
        break
    
    try:
        nota_float = float(nota)
        notas.append(nota_float)
    except ValueError:
        print("Por favor, digite um número válido.")

if notas:
    media = sum(notas) / len(notas)
    print("A média da turma é:", media)
else:
    print("Nenhuma nota foi registrada.")
