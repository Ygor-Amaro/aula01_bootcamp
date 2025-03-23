#Exercício 01 - Crie programa que o usuário digita o seu nome e retorna o número de caracteres

print(len(input("digite o seu nome: ")))

#Exercício 02 - Criar um programa onde o usuário digite dois valores e apareça a soma

print(int(input("Digite o primeiro número: ")) + int(input("Digite o segundo número: ")))

#Exercício 03 - Declaração e atribuições de variavéis

nome = str(input("digite o seu nome: "))
num_nome = len(nome)

print(num_nome)


#Exercício 04 - Declaração e atribuições de variavéis
nome_usuario = str(input("Digite o seu nome: "))
salario_usuario = float(input("Digite o valor do seu salário: "))
bonus_usuário = float(input("Digite o valor percentual do seu bonûs: "))
extra = int(1000)

calculo_bonus = (salario_usuario * bonus_usuário)

print(f"Olá {nome_usuario}, o valor do seu bonûs foi de: {calculo_bonus}")
