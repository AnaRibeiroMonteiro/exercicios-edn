# 2- Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. 
# O programa deve exibir o nome, email e país do usuário gerado."


import requests

def gerar_perfil():
    try:
        resposta = requests.get('https://randomuser.me/api/')
        resposta.raise_for_status()  # Verificar se houve erro na requisição

        dados = resposta.json()

        # Extrair informações
        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException as erro:
        print("Erro ao acessar a API:", erro)



gerar_perfil()
