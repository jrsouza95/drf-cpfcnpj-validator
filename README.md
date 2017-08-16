# DJANGO REST CNPJ OR CPF VALIDATOR
A small and quick validation plugin for CPF or CNPJ in django rest framework!


#### Examples:


> CPF
``` python
from rest_framework import serializers 
from drf_cpfcnpj_validator.validadors import cpf_validator


class PersonSerializer(serializers.ModelSerializer):
    cpf = serializers.Charfield(validators=[cpf_validator])

```




> CNPJ
``` python
from rest_framework import serializers 
from drf_cpfcnpj_validator.validadors import cnpj_validator


class CompanySerializer(serializers.ModelSerializer):
    cnpj = serializers.Charfield(validators=[cnpj_validator])

```
