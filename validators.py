from rest_framework import serializers
from utils import firstDigit, secondDigit

def cpf_validator(value):
    if (len(value) != 11 or len(set(value)) == 1):
        raise serializers.ValidationError('CPF inválido')

    first_cpf_weighs = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    second_cpf_weighs = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    first_part = value[:9]
    first_digit = value[9]
    second_digit = value[10]

    if not (first_digit == firstDigit(first_part, first_cpf_weighs) and second_digit == secondDigit(
            value[:10], second_cpf_weighs)):
        raise serializers.ValidationError('CPF inválido')

def cnpj_validator(value):
    if (len(value) != 14 or len(set(value)) == 1):
        raise serializers.ValidationError('CNPJ inválido')

    first_cnpj_weighs = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    second_cnpj_weighs = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    first_part = value[:12]
    first_digit = value[12]
    second_digit = value[13]

    if not (first_digit == firstDigit(first_part, first_cnpj_weighs) and second_digit == secondDigit(value[:13],
            second_cnpj_weighs)):
        raise serializers.ValidationError('CNPJ inválido')
