# 3- Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

temperatura = float(input("Insira a temperatura: "))
unidade_origem = input("Insira a unidade de origem: ")
unidade_conversao = input("Insira a unidade de conversão: ")

if unidade_origem == "celsius" and unidade_conversao == "fahrenheit":
    calculo_fahrenheit = ( temperatura * 9/5) + 32
    print(f"Temperatura de Celsius para Fahrenheit: {calculo_fahrenheit} ")

elif unidade_origem == "fahrenheit" and  unidade_conversao == "celsius":
    calculo_celsius = ( temperatura - 32) * 5/9
    print(f"Temperatura de Fahrenheit para Celsius: {calculo_celsius} ")

elif unidade_origem == "celsius" and unidade_conversao == "kelvin":
    calculo_kelvin = temperatura + 273.15
    print(f"Temperatura de Celsius para Kelvin: {calculo_kelvin} ")

elif unidade_origem == "kelvin" and unidade_conversao == "celsius":
    calculo_celsius_2 = temperatura - 273.15
    print(f"Temperatura de  Kelvin para Celsius: {calculo_celsius_2} ")

elif unidade_origem == "fahrenheit" and unidade_conversao == "kelvin":
    calculo_kelvin_2 = (temperatura - 32) * 5/9 + 273.15
    print(f"Temperatura de Fahrenheit para Kelvin: {calculo_kelvin_2} ")

elif unidade_origem == "kelvin" and unidade_conversao == "fahrenheit":
    calculo_fahrenheit_2 = (temperatura - 273.15 ) * 9/5 + 32
    print(f"Temperatura de Kelvin  para Fahrenheit: {calculo_fahrenheit_2} ")

