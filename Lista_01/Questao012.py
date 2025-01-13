cpf = input("Digite o CPF (apenas números): ")

if len(cpf) != 11:
    print("CPF inválido. O CPF deve ter exatamente 11 dígitos e conter apenas números.")
elif not cpf.isdigit():
    print("CPF inválido. O CPF deve ter exatamente 11 dígitos e conter apenas números.")
else:
    print("CPF válido!")


