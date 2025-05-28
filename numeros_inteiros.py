# Crie um programa que solicite números inteiros ao usuário.

# Regras:
# Continuar pedindo números até que o usuário digite 'fim'.
# Informar se o número é par ou ímpar.
# Se não for um número inteiro, informar o erro e continuar.
# # Ao final, mostrar a quantidade total de números pares e ímpares inseridos.


contador_par = 0
contador_impar = 0

while True:

    numero = input("Insira um numero inteiro: ")
    
    if numero.lower() == "sair":
            break

    try: 
        inteiro = int(numero)
        
        if int(numero) % 2 == 0:
                print(f"Número {numero} é par. ")
                contador_par += 1
        else:
                print(f"Número {numero} é impar. ")
                contador_impar += 1
        
        
    except ValueError:
            print("Por favor digite um número inteiro.")

        

print(f"Total de números pares: {contador_par}")
print(f"Total de números pares: {contador_impar}")