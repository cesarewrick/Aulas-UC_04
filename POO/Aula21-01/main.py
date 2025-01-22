from controllers.produto_controller import ProdutoController

def menu():
    print("\n--- CRUD de Produtos ---")
    print("1. Criar produto")
    print("2. Listar produto")
    print("3. Atualizar produto")
    print("4. Deletar produto")
    print("0. Sair")
    return input ("ESscolha uma opção: ")

if __name__ == "__main__":
    controller = ProdutoController()

while True:
    opcao = menu()
    if opcao == "1":
        id = int(input("Digite o ID do Produto: "))
        nome = input("Digite o nome do Produto")
        preco = float(input("Digite o preco do Produto"))
        controller.criar_produto(id, nome, preco)
    elif opcao == "2":
        controller.listar_produtos()
    elif opcao == "0":
        print("Encerramento")
        break