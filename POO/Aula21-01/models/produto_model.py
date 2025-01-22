# CRUD

# CREATE   
# READ
# UPDATE
# DELETE


class Produto:
    def __init__(self, id, nome, preco):
        self.__id = id # atributo privado
        self.__nome = nome # atributo privado
        self.__preco = preco # atributo privado

    # Getter e Setter para o ID
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, novoID):
        self.__id = novoID

    # Getter e Setter para o nome
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome

    # Getter e Setter para o preço
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novoPreco):
        self.__preco = novoPreco


    def __str__(self):
        return f"ID: {self.__id}, Nome: {self.__nome}, Preço: R$ {self.__preco}"