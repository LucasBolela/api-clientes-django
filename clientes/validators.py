import re
from validate_docbr import CPF

def cpf_valido(cpf):
    cpf_validation = CPF()
    return cpf_validation.validate(cpf)

def nome_valido(nome):
    return nome.replace(' ', '').isalpha()

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    """Verifica se o celular é válido"""
    modelo = '([0-9]{2,3})?([0-9]{2}) ([0-9]{4,5})-([0-9]{4})'
    resposta = re.findall(modelo, celular)
    return resposta