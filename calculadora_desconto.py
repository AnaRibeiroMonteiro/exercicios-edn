# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

produto = "camisa"
preco = 50.00
desconto = 20

total_desconto = (preco * desconto) / 100
total = preco - total_desconto
print(f"O preço total do produto {produto} é {total}")