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
#     print(f'O valor disponível convertido em dólar é: US${conversao}')
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
#     reajuste: float = produto - (produto * 0.05)
#     print(f'O preço reajustado do produto é: {reajuste}')
# except ValueError as e:
#     print(e)

# 13 - Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salario com 15% de aumento

# try:
#     salario: float = float(input("Digite seu salarío: "))
#     nome: str = input("Insira seu nome: ")
#     reajuste: float = salario + (salario * 0.15)
#     print(f'{nome} o seu salário reajustado em 15% é: {reajuste}')
# except ValueError as o:
#     print(o)

# 14 - Converta uma temperatura informada em celsius para Fahrenhait

# try:
#     c: float = float(input("Insira a temperatura atual em °C: "))
#     f: float = (c * 1.8) + 32
#     print(f'A temperatura de {c}°C convertida para Fahrenheit é: {f:.2f}°F')
# except ValueError as i:
#     print(i)

# 15 - Calcule o preço a pagar por um carro alugado, sabendo que o aluguel diário custa 60 reais por dia e a quantidade de km 
# percorrida 0,15 centavos por km rodado.

# VALOR_DIA: int = 60
# VALOR_KM: float = 0.15

# try:
#     dias: int = int(input("Insira a quantidade de dias de locação: "))
#     km: float = float(input("Insira o total de km percorridos: "))
#     custo: float = (dias * VALOR_DIA) + (km * VALOR_KM)
#     print(f'O valor total a pagar pelo aluguel do veículo foi de: R${custo}')
# except ValueError as a:
#     print(a)

# 16 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

# import math

# try:
#     numero: float = float(input("Insira o numero real: "))
#     print(f'A porção inteira do número real {numero} é: {math.trunc(numero)}')
# except ValueError as msg:
#     print(msg)

# 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
# e mostre o comprimento da hipotenusa

# import math

# cateto_1: float = float(input("Insira aqui o cateto oposto: "))
# cateto_2: float = float(input("Insira aqui o cateto adjacente: "))
# hipotenusa: float = math.hypot(cateto_1, cateto_2)
# print(f'A hipotenusa dos catetos {cateto_1} e {cateto_2} é : {hipotenusa:.2f}')


# 18 - Faça um programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno e tangente

# import math

# angulo: float = float(input("Insira o valor do ângulo: "))
# seno: float = math.sin(math.radians(angulo))
# cosseno: float = math.cos(math.radians(angulo))
# tangente: float = math.tan(math.radians(angulo))
# print(f'O ângulo informado {angulo} possui como: \nSeno: {seno}cm \nCosseno: {cosseno}cm \nTangente: {tangente}cm')


# 19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome escolhido

# import random

# try:
#     aluno_1: str = input("Qual o nome do primeiro aluno? ")
#     aluno_2: str = input("Qual o nome do primeiro aluno? ")
#     aluno_3: str = input("Qual o nome do primeiro aluno? ")
#     aluno_4: str = input("Qual o nome do primeiro aluno? ")
#     turma: list = [aluno_1, aluno_2, aluno_3, aluno_4]
#     escolhido: str = random.choice(turma)
#     print(f'O aluno escolhido para apagar o quadro foi: {escolhido}.')
# except ValueError as d:
#     print(d)

# 20 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça
# um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# import random

# try:
#     aluno_1: str = input("Qual o nome do primeiro aluno? ")
#     aluno_2: str = input("Qual o nome do primeiro aluno? ")
#     aluno_3: str = input("Qual o nome do primeiro aluno? ")
#     aluno_4: str = input("Qual o nome do primeiro aluno? ")
#     turma: list = [aluno_1, aluno_2, aluno_3, aluno_4]
#     escolhido: str = random.shuffle(turma)

#     for i, aluno in enumerate(turma, start=1):
#         print(f"{i}. {aluno}")

# except ValueError as d:
#     print(d)

    
# 21 -  Faça um program em python que abra e reproduza um audio de um arquivo mp3.
# uso pygame


# 22 - Crie um programa que leia o nome completo de uma pessoa e monstre:
# O nome com todas as letras maiúsculas, o nome com todas as letras minúsculas, quantas letras ao todo sem considerar espaços e quantas letras tem o primeiro nome

# try:
#     nome: str = str(input("Insira o nome completo: "))
#     print("Analisando seu nome...")
#     print(f'Seu nome em maiúsculas é: {nome.upper()}')
#     print(f'Seu nome em minúsculas é: {nome.lower()}')
#     print(f'Seu nome tem ao todo {len(nome)-nome.count(' ')}')
#     print(f'Seu primeiro nome é {:nome} e ele tem {len(:nome)}')
# except ValueError as e:
#     print(e)

# 23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados. Ex: 1834 = 4, 3, 8, 1

# try:
#     numero: str = str(input("Insira o número desejado: "))
#     lista: list = []
#     for i in numero:
#         l = i.split()[0]
#         lista.append(l)
#     print("Realizando separação...")
#     print(f'O numero separado é {lista}')
# except ValueError as msg:
#     print(msg)

# 24 - Crie um programa se ela começa ou não com a palavra "SANTO"

# try:
#     nome: str = str(input("Insira o nome da cidade em que nasceu: ")).strip()
#     formatado: str = nome.title()
#     if formatado.startswith("Santo"):
#         print("O nome começa com Santo")
#     else:
#         print("Não começa com Santo")
# except ValueError as msg:
#     print(msg)

# 25 - Crie um programa que leia o nome de uma pessoa e diga se possui "SILVA" no nome

# try:
#     nome: str = str(input("Insira seu nome completo: ")).strip()
#     formatado: str = nome.title()
#     if formatado.__contains__("Silva"):
#         print("Seu nome contém Silva")
#     else:
#         print("Seu nome não contém Silva")
# except ValueError as msg:
#     print(msg)

# 26 - Leia uma frase e diga  quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição aparece a última

# try:
#     frase: str = str(input("Insira sua frase: ")).strip()
#     print(f'A letra "A" aparece {frase.lower().count('a')} vezes')
#     print(f'A primeira letra "A" encontra-se na posição {frase.lower().find('a')+1}')
#     print(f'A última letra "A" encontra-se na posição {frase.lower().rfind('a')+1}')
# except ValueError as msg:
#     print(msg)

# 27 - Crie um programa que leia o nome inteiro de uma pessoa e mostre o primeiro e ultimo nome: Ex: Italo Eduardo de Oliveira Teixeira = 1: Italo U: teixeira

# try:
#     nome: str = str(input("Insira seu nome completo: ")).strip()
#     inicio: str = nome.split()[0]
#     final: str = nome.split()[-1]
#     print("Muito prazer em te conhecer!!")
#     print(f'Seu primeiro nome é {inicio}.')
#     print(f'Seu último nome é {final}.')
# except ValueError as m:
#     print(m)

# 28 - Escreve um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa
# deverá escrever na tela se o usuário venceu ou perdeu

# import random
# from time import sleep
# numero: int = random.randint(0, 5)
# print("-=-" * 20)
# print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
# print("-=-" * 20)
# adivinha: int = int(input("Em que número eu pensei? "))
# print("PROCESSANDO...")
# sleep(3)
# if adivinha == numero:
#     print("Parabéns, você conseguiu me vencer!!")
# else:
#     print(f'GANHEI! Eu pensei no número {numero} e não no {adivinha}!')

# 29 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre
# uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite

# from time import sleep

# limite: int = 80
# velocidade: int = int(input("Insira a velocidade do carro: "))
# multa: int = (velocidade - limite) * 7
# if velocidade > limite:
#     print("Você foi MULTADO!!")
#     print("-=-" * 20)
#     print("Calculando o valor de sua multa...")
#     print("-=-" * 20)
#     sleep(2)
#     print(f'O valor de sua multa é R${multa}. Favor emitir guia de pagamento e regularizar.')
# else:
#     print("Você não foi multado. Velocidade dentro do permitido para a via.")


# 30 - Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar

# numero: int = int(input("Insira o número desejado: "))
# verifica: float = numero % 2
# if verifica == 0:
#     print("O número informado é PAR!!")
# else:
#     print("O número informado é ímpar!!")

# 31 - Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da 
# passagem, cobrando R$ 0,50 por km para viagens até 200km e R$ 0,45 para viagens mais longas.

# while True:
#     try:
#         distancia = int(input("Insira a distância calculada para a viagem: "))
#         if distancia < 0:
#             print("Insira uma distância positiva.")
#             continue
#         break  # Sai do loop quando a entrada for válida
#     except ValueError:
#         print("Entrada inválida para distância. Por favor, digite um número válido.")

# if distancia <= 200:
#     passagem = distancia * 0.50
# else:
#     passagem = distancia * 0.45

# print(f'O preço da sua passagem para a viagem informada é: R${passagem:.2f}.')

# 32 - Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

# while True:
#     try:
#         ano: int = int(input("Insira o ano desejado: "))
#         if ano < 0:
#             print("Inserir ano válido.")
#             continue
#         break
#     except ValueError as m:
#         print("Insira um ano contendo a formatação válida!")

# if ano % 400 == 0:
#     print("O ano informado é BISSEXTO!")
# elif ano % 4 == 0 and ano % 100 != 0:
#     print("O ano informado é BISSEXTO!")
# else:
#     print("O ano informado não é BISSEXTO!")
    

# 33 - Faça um programa que leia três numeros e mostre qual é o maior e qual é o menor

# while True:
#     try:
#         numero_1: int = int(input("Insira o primeiro número: "))
#         numero_2: int = int(input("Insira o segundo número: "))
#         numero_3: int = int(input("Insira o terceiro número: "))
#         if numero_1 < 0 or numero_2 < 0 or numero_3 < 0:
#             print("Inserir um número maior que 0.")
#             continue
#         break
#     except ValueError as m:
#         print("Inserir a formatação correta, por gentileza.")
# lista: list = [numero_1, numero_2, numero_3]
# print(f'O maior número digitado foi {max(lista)} e o menor número foi {min(lista)}')

# 34 - Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, 
# o aumento é de 15%.

while True:
    try:
        salario: float = float(input("Inserir o respectivo salário: "))
        if salario < 0:
            print("Por favor, insira um valor positivo/válido para o salário.")
            continue
        break
    except ValueError as m:
        print("Inserir um valor/formatação válida para o salário!")

try:
    if salario > 1250:
        aumento: float = salario * 0.10
        print(f'O valor do seu reajuste é de R${aumento}. Seu salário total é de R${salario + aumento}')
    else:
        aumento: float = salario * 0.15
        print(f'O valor do seu reajuste é de R${aumento}. Seu salário total é de R${salario + aumento}')
except ValueError as m:
    print("Erro de formato")

# 35 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triângulo.

# try:
#     x: float = float(input("Insira o primeiro lado: "))
#     y: float = float(input("Insira o segundo lado: "))
#     z: float = float(input("Insira o terceiro lado: "))

#     if x + y > z and x + z > y and y + z > x:
#         print("As retas informadas formam um triângulo!")
#         if x == y == z:
#             print("-=-" * 20)
#             print("Seu triângulo é equilátero!")
#             print("-=-" * 20)
#         elif x != y != z:
#             print("-=-" * 20)
#             print("Seu triângulo é escaleno!")
#             print("-=-" * 20)
#         else:
#             print("-=-" * 20)
#             print("Seu triângulo é isósceles!")
#             print("-=-" * 20)
#     else:
#         print("As retas informadas não formam um triângulo.")
# except ValueError as m:
#     print(m)