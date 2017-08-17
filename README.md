# DJANGO REST CNPJ OR CPF VALIDATOR
> A small and quick validation plugin for CPF or CNPJ in django rest framework!  


#### Examples:

``` python
from rest_framework import serializers 
from drf_cpfcnpj_validator.validadors import cpf_validator, cnpj_validator


class PersonSerializer(serializers.ModelSerializer):
    cpf = serializers.Charfield(validators=[cpf_validator])


class CompanySerializer(serializers.ModelSerializer):
    cnpj = serializers.Charfield(validators=[cnpj_validator])

```


#### Translations:

This plugin translate the messages from your LANGUAGE_CODE, located in settings.py.  

* **Avaliable translations:**  


  - en-US  
  - pt-BR  
  - es-ES  
