from rest_framework import serializers
from apps.pessoas.models import Pessoa, Endereco


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = [
            'id',
            'nome',
            'sobrenome',
        ]

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = [
            'cep',
            'bairro',
            'logradouro'
        ]
