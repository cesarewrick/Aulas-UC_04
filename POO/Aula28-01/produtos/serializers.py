from rest_framework import serializers
from .models import Produto
from .models import Fornecedor

class ProdutoSerializer(serializers.ModelSerializer):
    fornecedor_nome = serializers.ReadOnlyField(source='fornecedor.nome')
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'estoque', 'fornecedor', 'fornecedor_nome']

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'