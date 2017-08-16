# DJANGO REST CNPJ OR CPF VALIDATOR
A small and quick validation plugin for CPF or CNPJ in django rest framework!


#### Usage:

from rest_framework import serializers 

from drf_cpfcnpj_validator.validadors import cpf_validator, cnpj_validator


class PersonSerializer(serializers.ModelSerializer):
    cpf = serializers.Charfield(validators=[cpf_validator])