import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from apps.pessoas.models import Pessoa, Endereco
from apps.pessoas.api.serializers import PessoaSerializer, EnderecoSerializer

class PessoaViewSet(ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    def list(self, request, *args, **Kwargs):
        return super().list(request, *args, **Kwargs)
    
    #def create(self, request, *args, **Kwargs):
    #    return super().create(request, *args, **Kwargs)
    
    #def retrieve(self, request, *args, **Kwargs):
    #    return super().retrieve(request, *args, **Kwargs)
    
    #def destroy(self, request, *args, **Kwargs):
    #    return super().destroy(request, *args, **Kwargs)

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    def create(self, request, *args, **Kwargs):
        cep = request.data.get('cep')
        requisicao = requests.get(f'viacep.com.br/ws/{cep}/json/')

        endereco_salvo = Endereco.objects.create(
            cep = requisicao['cep'],
            bairro = requisicao['bairro'],
            logradouro = requisicao['logradouro']
        )

        return Response({"Success":"endereco salvo"}, status=status.HTTP_201_CREATED)