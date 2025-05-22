# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# * Valor em reais: R$ 100.00
# * Taxa do dólar: R$ 5.20
# * Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

valor_real = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

moeda = input("Insira a moeda que deseja converter: ")

if moeda == "dolar":
    conversao = valor_real / taxa_dolar
    print(f"Valor convertido: {conversao:.2f} ")
elif moeda == "euro":
    conversao = valor_real / taxa_euro
    print(f"Valor convertido: {conversao:.2f} ")
else:
    print("Insira uma moeda válida.")