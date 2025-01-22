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
        ProdutoView.listar_produto(self.__produtos)
        
    def atualizar_produto(self, id, nome=None, preco=None):
        for produto in self.__produtos:
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

    def buscar_por_nome(self, nome):
        for produto in self.__produtos:
            if produto.nome.lower() == nome.lower():
                ProdutoView.mensagem("Produto encontrado com sucesso!")
                ProdutoView.mostrar_produto(produto)
                return
        ProdutoView.mensagem ("Erro: Produto não encontrado.")

    def buscar_produto_preco(self, inicio, fim):
        cont = 0
        for produto in self.__produtos:
            if produto.preco >= inicio and produto.preco <= fim:
                cont +=1
                ProdutoView.mostrar_produto(produto)
        if cont == 0:         
            ProdutoView.mensagem("Erro. Nenhum produto com essa faixa de preço. ")
            return