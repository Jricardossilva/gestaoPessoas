from django.urls import path, include
from rest_framework import routers

from apps.pessoas.api.viewsets import PessoaViewSet, EnderecoViewSet

router = routers.DefaultRouter()
router.register(r'', PessoaViewSet, basename='pessoas')
router.register(r'enderecos', EnderecoViewSet, basename='enderecos')

urlpatterns = [
    path('dados/', include(router.urls))
]
