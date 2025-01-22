from models.produto_model import Produto
from views.produto_views import ProdutoView

class ProdutoController:
    def __init__(self):
        self.__produtos = [] # Atributo encapsulado (Produtos)

    def criar_produto(self, id, nome, preco):
        if any(produto.id == id for produto in self.__produtos):
            ProdutoView.mensagem("Erro: Ja existe um produto com esse ID.")
            return
        novo_produto = Produto(id, nome, preco)
        self.__produtos.append(novo_produto)
        ProdutoView.mensagem ("Produto criado com Sucesso.")

        def listar_produtos(self):
            ProdutoView.listar_produto
        
        def atualizar_produto(self, id, nome=None, preco=None):
            for produto in self.__produts:
                if produto.id == id:
                    if nome:
                        produto.nome = nome # Setter de nome é chamado
                    if preco:
                        produto.preco = preco # Setter de preço é chamado
                    ProdutoView.mensagem ("Poduto Atualizado com Sucesso!")
                    return
                ProdutoView.mensagem ("Erro: Produto não encontrado.")

        def deletar_produto(self, id):
            for produto in self.__produtos:
                if produto.id == id:
                    self.__produtos.remove(produto)
                    ProdutoView.mensagem ("Produto deletado com Sucesso!")
                    return
                ProdutoView.mensagem ("Erro: Produto não encontrado.")