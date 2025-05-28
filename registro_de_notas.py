# Crie um programa para o professor registrar as notas da turma.

# Regras:
# Continuar solicitando notas até que o professor digite 'fim'.
# Aceitar apenas notas entre 0 e 10.
# Ignorar notas inválidas e continuar solicitando.
# Ao final, mostrar a média da turma.

nota_turma = 0
contador = 0

while True:
    
    notas = input("Digite a nota: ")
    if notas.lower() == "fim":
        break
    
    
    else:
        notas = float(notas)
        if notas <0 or notas > 10:
            print("Insira um valor entre 0 e 10")
        else:
            contador += 1
            nota_turma += notas
    

media = nota_turma / contador
print(f"A média da turma é: {media}")