from controllers.produto_controller import ProdutoController

def menu():
    print("\n--- CRUD de Produtos ---")
    print("1. Criar produto")
    print("2. Listar produto")
    print("3. Atualizar produto")
    print("4. Deletar produto")
    print("5. Buscar produto por nome")
    print("6. Buscar produto por faixa de preço")
    print("7. Ordenar produtos")
    print("0. Sair")
    return input ("Escolha uma opção: ")

if __name__ == "__main__":
    controller = ProdutoController()

    while True:
        opcao = menu()
        if opcao == "1":
            id = int(input("Digite o ID do Produto: "))
            nome = input("Digite o nome do Produto: ")
            preco = float(input("Digite o preco do Produto: "))
            controller.criar_produto(id, nome, preco)

        elif opcao == "2":
            controller.listar_produtos()

        elif opcao == "3":
            id = int(input("ID do Produto que deseja atualizar: "))
            nome = input("Digite o novo nome (ou deixe em branco): ")
            preco = float(input('Dgite o novo preço (ou deixe em branco):'))

            nome = nome if nome else None
            preco = float(preco) if preco else None
            controller.atualizar_produto(id, nome, preco)

        elif opcao == "4":
            id = int(input("Digite o ID do produto á ser deletado: "))
            controller.deletar_produto(id)

        elif opcao == "5":
            nome = input("Digite o nome do produto: ")
            controller.buscar_por_nome(nome)

        elif opcao == "6":
            inicio = float(input("Digite o preço inicial: "))
            fim = float(input("Digite o preço final: "))
            controller.ordenar_produtos(inicio,fim)

        elif opcao == "7":
            print("Escolha um critério de ordenação: 'id', 'nome', 'preco' ou 'todos'")
            criterio = input("Ceitério: ").lower()
            controller.ordenar_produtos(criterio)


        elif opcao == "0":
            print("Encerrando...")
            break
        
        else:
            print("Opção Invalida!")