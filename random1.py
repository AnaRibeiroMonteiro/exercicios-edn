# 1- Crie um programa que gera uma senha aleatória com o módulo random, 
# utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de 
# caracteres dessa senha aleatória.

import random
import string



while True:

    try:
        qtde_caracteres = int(input("Insira a quantidade de caracteres desejadas: "))
        break
    except ValueError:
        print("Por favor insira um número válido")

caracteres = string.punctuation

senha = ''.join(random.choices(caracteres, k=qtde_caracteres))

print(f"Senha gerada: {senha}")
