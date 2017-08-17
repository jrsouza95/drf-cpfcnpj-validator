# -*- coding: utf-8 -*-

from rest_framework import serializers
from utils import Utils
from exception import ExceptionMessage


def cpf_validator(value):
    if len(value) != 11 or len(set(value)) == 1:
        raise serializers.ValidationError(ExceptionMessage.invalid_cpf())

    first_cpf_weight = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    second_cpf_weight = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    first_part = value[:9]
    first_digit = value[9]
    second_digit = value[10]

    if not ((first_digit == Utils.get_first_digit(number=first_part, weight=first_cpf_weight)
             and second_digit == Utils.get_second_digit(updated_number=value[:10], weight=second_cpf_weight))):
        raise serializers.ValidationError(ExceptionMessage.invalid_cpf())


def cnpj_validator(value):
    if len(value) != 14 or len(set(value)) == 1:
        raise serializers.ValidationError(ExceptionMessage.invalid_cnpj())

    first_cnpj_weight = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    second_cnpj_weight = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    first_part = value[:12]
    first_digit = value[12]
    second_digit = value[13]

    if not (first_digit == Utils.get_first_digit(number=first_part, weight=first_cnpj_weight)
            and second_digit == Utils.get_second_digit(updated_number=value[:13], weight=second_cnpj_weight)):
        raise serializers.ValidationError(ExceptionMessage.invalid_cnpj())
