from rest_framework import serializers
from .models import Aluno

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['nome', 'description', 'telefone', 'email', 'data_nascimento','user']