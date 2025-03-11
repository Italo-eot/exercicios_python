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

# variavel: any = input("Inserir aqui seus dados: ")
# tipo: any = type(variavel)
# tamanho: int = len(variavel)
# print(f'Nossa variável é do tipo {tipo}, possui um tamanho de {tamanho} e o conteúdo inserido foi: {variavel}')

# 05 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

# try:
#     numero: int = int(input("Insira o número desejado: "))
#     antecessor: int = numero - 1
#     sucessor: int = numero + 1
#     print(f'O número inserido foi {numero}. Seu antecessor é {antecessor} e sucessor é {sucessor}')
# except ValueError as e:
#     print(e)

# 06 - Crie um algoritimo que leia um número inteiro e mostre seu dobro, triplo e raiz quadrada
# import math

# try:
#     numero: int = int(input("Insira o número desejado: "))
#     print(f'O número inserido foi {numero}. Seu dobro é {numero * 2}, seu triplo é {numero * 3} e sua raiz quadrada é {math.sqrt(numero)}')
# except ValueError as e:
#     print(e)

# 07 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

# import statistics

# try:
#     n_1: float = float(input("Insira a primeira nota: "))
#     n_2: float = float(input("Insira a segunda nota: "))
#     print(f'Nota do primeiro semestre foi {n_1} e segundo semestre {n_2}. Média do aluno é {statistics.median([n_1, n_2])}')
# except ValueError as e:
#     print(e)

# 08 - Escreva um programa que leia um valor em metros, exiba convertido em centimetros e milimetros

# try:
#     medida: float = float(input("Insira a medida do local: "))
#     print(f'Sua medida em metros é {medida}. Sua conversão em cm {medida * 1000} e mm {medida * 10000}')
# except ValueError as a:
#     print(a)

# 09 - Faça um programa que leia um numero inteiro qualquer e mostre sua tabuada

# try:
#     numero: int = int(input("Insira seu número: "))
#     for i in range(1, 11):
#         tabuada = i * numero
#         print(f'A multiplicação de {numero} por {i} é: {tabuada}')
# except ValueError as a:
#     print(a)

# 10 - Crie um programa que leia quanto dinheiro a pessoa tem na carteira e quantos dólares ela pode comprar

# try:
#     real: float = float(input("Insira o valor disponível: "))
#     dolar: float = float(input("Insira a cotação atual: "))
#     conversao: float = real / dolar
#     print(f'O valor disponível convertido em dólar é: {conversao}')
# except ValueError as e:
#     print(e)


# 11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e quantidade de tinta necessária para pinta-la, 
# sabendo que cada litro de tinta pinta 2m2

# try:
#     largura: float =  float(input("Insira a largura da parede, Iasmin: "))
#     altura: float  =  float(input("Insira a altura da parede, Iasmin: "))
#     area: float = altura * largura
#     tinta: float  = area / 2
#     print(f'O que que acontece...a área total da parede é {area}m². A quantidade de tinta necessária {tinta}')
# except ValueError as a:
#     print(a)

# 12 - Faça um algoritmo que leia o preco de um produto e mostre seu novo preço com 5% de desconto

# try:
#     produto: float = float(input("Insira o preço do produto: "))
#     reajuste: float = produto + (produto * 0.05)
#     print(f'O preço reajustado do produto é: {reajuste}')
# except ValueError as e:
#     print(e)

# 13 - Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salario com 15% de aumento

try:
    salario: float = float(input("Digite seu salarío: "))
    nome: str = input("Insira seu nome: ")
    reajuste: float = salario + (salario * 0.15)
    print(f'{nome} o seu salário reajustado em 15% é: {reajuste}')
except ValueError as o:
    print(o)