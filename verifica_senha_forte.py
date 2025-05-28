# Crie um programa que verifique se a senha é forte.

# Regras:
# Senha forte: pelo menos 8 caracteres e pelo menos um número.
# Continuar pedindo senha até que uma válida seja inserida ou o usuário digite 'sair'.

while True:
    senha = input("Digite sua senha: ")
    if senha.lower() == "sair":
        break
    else:
        if len(senha) < 8:
            print("Sua senha tem menos de 8 caracteres, por favor ajuste-a")
        elif not any(char.isdigit() for char in senha):
            print("Sua senha deve conter pelo menos um número")
