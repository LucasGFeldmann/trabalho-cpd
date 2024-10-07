from mergesort import File, MSE
import json
import json
from datetime import datetime


def data_emissao(json_data):
    data = json.loads(json_data)

    # Acessar o campo "emissao"
    emissao = data['info']['emissao']

    # Remover a parte " - Via Consumidor 2"
    emissao_data = emissao.split(' - ')[0]

    # Converter a string para datetime
    data_hora_emissao = datetime.strptime(emissao_data, '%d/%m/%Y %H:%M:%S')

    # Exibir o resultado
    return data_hora_emissao


def valor_total(json_data):
    data = json.loads(json_data)

    # Acessar o campo "emissao"
    emissao = data['resumo']['Valor a pagar R$:']

    # Remover a parte " - Via Consumidor 2"
    emissao_data = float(emissao.replace(',', '.'))

    return emissao_data

def cnpj(json_data):
    data = json.loads(json_data)

    # Acessar o campo "emissao"
    emissao = data['emissor']['cnpj']

    return emissao


file = File('resultado.txt')

sort = MSE(file)
sort.filter = valor_total
result = open(sort.sort(), 'r')



numeros = []

for linha in result:
    numeros.append(json.loads(linha.rstrip()))

print(json.dumps(numeros))