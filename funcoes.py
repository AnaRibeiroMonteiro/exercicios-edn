# 1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, 
# baseada no valor total da conta e na porcentagem de gorjeta desejada.​

#Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.​

# Parâmetros:​

#valor_conta (float): O valor total da conta​
#porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)​
#Retorna:​ float: O valor da gorjeta calculada

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    total_gorjeta =  valor_conta * (porcentagem_gorjeta / 100)
    return total_gorjeta
                                  
gorjeta = calcular_gorjeta(343, 15)
print(f"O valor da gorjeta é: R$ {gorjeta:.2f}")                                 
                                  

# 2- : Crie uma função que verifique se uma palavra ou frase é um palíndromo 
# (lê-se igual de trás para frente, ignorando espaços e pontuação).​
# Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”                                 

def palavra(palavra):
    if palavra == palavra[::-1]:
        return "Sim"
    else:
        return "Não"

resultado = palavra("arara")
print(f"a palavra é um palindro? {resultado}")

# 3- Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

def calculo_idade(ano_nascimento, ano_atual):
    total_dias = (ano_atual - ano_nascimento) * 365
    return total_dias

resultado = calculo_idade(1996, 2025)
print(f"Você tem {resultado} dias de vida.")


