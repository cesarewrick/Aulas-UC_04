class ProdutoView:
    @staticmethod
    def mostrar_produto(produto):
        print(produto)

    @staticmethod
    def listar_produto(produtos):
        if produtos:
            print("Lista de Produtos: ")
            for produto in produtos:
                print(produto)

        else:
            print("Nenhum produto encontrado.")

    @staticmethod
    def mensagem(msg):
        print(msg)