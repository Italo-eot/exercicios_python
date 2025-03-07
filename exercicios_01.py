# 01 - Crie um programa que imprima uma frase inserida pelo próprio usuário.

# try:
#     frase: str = input("Insira aqui sua frase: ")
#     if any(char.isdigit() for char in frase):
#         raise ValueError("Solicitamos uma frase, não um número.")
#     else:
#         print(frase)
# except TypeError as e:
#     print(e)

# 02 - Solicite o nome do usuário e posteriormente mande uma saudação.

# try:
#     nome: str = input("Insira o seu nome, por gentileza: ")
#     if len(nome) == 0:
#         raise ValueError("O nome não pode estar vazio!")
#     elif any(char.isdigit() for char in nome):
#         raise ValueError("Solicitamos uma nome, não um número.")
#     else:
#         print(f'Olá, {nome}!')
# except ValueError as e:
#     print(e)

# 03 - Crie um programa que leia dois números e mostre a soma entre eles (tipo primitivo INT)

# numero_01: int = int(input("Insira o primeiro número: "))
# numero_02: int = int(input("Insira o segundo número: "))
# soma: int = numero_01 + numero_02
# print(f'A soma dos dois números inseridos é: {soma}')

# 04 - Faça um programa que leia algo pelo teclado e mostre o tipo deles:

variavel: any = input("Inserir aqui seus dados: ")
tipo: any = type(variavel)
print(f'Nossa variável é do tipo {tipo} e o conteúdo inserido foi: {variavel}')

