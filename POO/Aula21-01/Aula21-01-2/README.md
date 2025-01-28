Sistema de Gerenciamento de Produtos


Este é um projeto simples de CRUD (Create, Read, Update, Delete) de produtos, desenvolvido em Python como parte de uma aula prática. O sistema permite criar, listar, atualizar, deletar e buscar produtos, com foco no aprendizado de POO (Programação Orientada a Objetos).

Funcionalidades

Criar produtos: Insere um novo produto com ID, nome e preço.
Listar produtos: Mostra todos os produtos cadastrados.
Atualizar produtos: Permite alterar nome ou preço de um produto existente.
Deletar produtos: Remove um produto pelo ID.
Buscar por nome: Procura produtos com base no nome.
Filtrar por preço: Lista produtos dentro de uma faixa de preço definida.


Estrutura do Projeto
css
Copiar
Editar
├── controllers/
│   └── produto_controller.py
├── models/
│   └── produto_model.py
├── views/
│   └── produto_views.py
├── main.py
└── README.md


controllers: Contém a lógica principal do sistema.

models: Define a estrutura dos dados (classe Produto).

views: Controla a exibição de mensagens e dados para o usuário.

main.py: Arquivo principal para executar o programa.

Tecnologias Utilizadas


Linguagem: Python 3.10+
Paradigma: POO (Programação Orientada a Objetos)
Como Executar o Projeto
Pré-requisitos: Certifique-se de que o Python está instalado em sua máquina.

Clone o repositório para sua máquina local e execute o arquivo main.py:
bash
Copiar
Editar

git clone https://github.com/seuusuario/nome-do-repositorio.git
cd nome-do-repositorio
python main.py


O Que Foi Aprendido
Durante o desenvolvimento deste projeto, foram abordados os seguintes conceitos:

Encapsulamento: Uso de atributos privados e métodos acessores (getters e setters).

Estrutura MVC: Organização do código em Model, View e Controller.

Manipulação de listas: Uso de listas para armazenar objetos.

Lógica de filtros e buscas: Implementação de métodos para localizar produtos com base em critérios.

Tratamento de erros: Exibição de mensagens informativas ao usuário.