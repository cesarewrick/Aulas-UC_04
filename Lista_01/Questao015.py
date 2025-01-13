senha = input("Digite a senha: ")

if len(senha) < 8:
    print("Senha inválida! A senha deve ter pelo menos 8 caracteres.")

else:
    if any(char.isdigit() for char in senha):
        print("Senha válida!")

    else:
        print("Senha inválida. Deve conter as menos um número.")