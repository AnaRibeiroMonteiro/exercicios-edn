# Desenvolva uma calculadora que realize as quatro operações básicas (+, -, *, /) entre dois números.

# Regras:
# Solicitar ao usuário dois números e a operação.
# Repetir até que uma operação válida seja concluída.
# Tratar os seguintes erros:
# Entrada não numérica.
# Divisão por zero.
# Operação inválida.
# Mostrar o resultado e encerrar.

while True:
    try:
        num1 = int(input("Insira o primeiro numero: "))
        num2 = int(input("Insira o segundo numero: "))
        break
    except ValueError:
        print("Insira um valor válido.")   

    

while True:

    operacao = input("Escolha uma Operação: Adição, Subtração, Multiplicação ou Divisão.").lower()

    if operacao == "adição":
            resultado = num1 + num2
            print(f"O resultado da soma entre {num1} + {num2} = {resultado} ")
            break

    elif operacao == "subtração":
            resultado = num1 - num2
            print(f"O resultado da subtração entre {num1} - {num2} = {resultado} ")
            break

    elif operacao == "multiplicação":
            resultado = num1 * num2
            print(f"O resultado da multiplicação entre {num1} * {num2} = {resultado} ")
            break

    elif operacao == "divisão":
        try:
            resultado = num1 / num2
            print(f"O resultado da divisão entre {num1} / {num2} = {resultado} ")
            break
        except ZeroDivisionError:
            print("Insira um valor maior que zero.")
            

    else:
        print("Insira uma operação válida.")
        