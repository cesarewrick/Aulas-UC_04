from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, FornecedorViewSet

router = DefaultRouter()
router.register(r'produtos',ProdutoViewSet, basename='produto')
router.register(r'fornecedor', FornecedorViewSet, basename='fornecedor')

urlpatterns = [
    path('', include(router.urls)),
]