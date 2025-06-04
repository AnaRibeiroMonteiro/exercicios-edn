# 3- Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário,
# utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes 
# ao CEP consultado.

import requests



     

def consultar_endereco():
    cep = input("Insira o CEP: ")
            
    url = f'https://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()

    logradouro = dados.get('logradouro')
    bairro = dados.get('bairro')
    cidade = dados.get('localidade')
    estado = dados.get('uf')
            
    return {
            'logradouro': logradouro,
            'bairro': bairro,
            'cidade': cidade,
            'estado': estado
            }
    

endereco = consultar_endereco()
print(endereco)