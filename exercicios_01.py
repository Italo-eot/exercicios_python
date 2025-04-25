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

# while True:
#     try:
#         salario: float = float(input("Inserir o respectivo salário: "))
#         if salario < 0:
#             print("Por favor, insira um valor positivo/válido para o salário.")
#             continue
#         break
#     except ValueError as m:
#         print("Inserir um valor/formatação válida para o salário!")

# try:
#     if salario > 1250:
#         aumento: float = salario * 0.10
#         print(f'O valor do seu reajuste é de R${aumento}. Seu salário total é de R${salario + aumento}')
#     else:
#         aumento: float = salario * 0.15
#         print(f'O valor do seu reajuste é de R${aumento}. Seu salário total é de R${salario + aumento}')
# except ValueError as m:
#     print("Erro de formato")

# 35 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triângulo.

# try:
#     x: float = float(input("Insira o primeiro lado (x): "))
#     y: float = float(input("Insira o segundo lado (y): "))
#     z: float = float(input("Insira o terceiro lado (z): "))

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

# 36 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal,sabendo que ele não pode exceder 30% do salário ou entao o empréstimo será negado

# try:
#     valor: float = float(input("Gentileza informar o valor do imóvel: "))
#     salario: float = float(input("Informe a renda líquida: "))
#     ano: int = int(input("Inserir a quantidade de anos para quitação: "))
#     meses: int = ano * 12
#     prestacao: float = valor / meses
#     print(f'Para pagar R$ {valor:.2f} em {ano} anos. A prestação será de R$ {prestacao:.2f} por mês.') 
# except ValueError:
#     print("Inserir os valores conforme solicitado")

# if prestacao > (salario * 0.30):
#     print("Empréstimo negado. Valor da prestação excede o limite maximo de 30% para o salário informado.")
# else:
#     print(f'Empréstimo aprovado! Gentileza providenciar documentação conforme lista informada pelo seu gerente.')


# 37 - Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 binario, 2 octal e 3 hexadecimal

# try:
#     numero: int = int(input("Digite um número inteiro: "))
#     print("*****" * 20)
#     print("Escolha uma das bases para conversão: ")
#     print("[ 1 ] converter para BINÁRIO")
#     print("[ 2 ] converter para OCTAL")
#     print("[ 3 ] converter para HEXADECIMAL")
#     print("*****" * 20)
# except ValueError:
#     print("Inserir número inteiro.")

# while True:
#     try:
#         opcao: int = int(input("Sua opção: "))
#         if opcao < 0:
#             print("Inserir número válido!")
#             continue
#         break
#     except ValueError:
#         print("Inserir valor correto conforme acima.")
        
# if opcao == 1:
#     print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}.')
# elif opcao == 2:
#     print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}.')
# else:
#     print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}.')


# 38 - Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela a mensagem:
# O primeiro valor é maior
# O segundo valor é maior 
# nao existe valor maior, os dois são iguais.

# while True:

#     try:
#         numero01: int = int(input("Insira o primeiro número: "))
#         numero02: int = int(input("Insira o segundo número: "))

#         if numero01 < 0 or numero02 < 0:
#             print("Números negativos não são válidos.")
#             continue
#         break

#     except ValueError:
#         print("Inserir números válidos.")

# if numero01 > numero02:
#     print("O primeiro número é maior que o segundo!")
# elif numero02 > numero01:
#     print("O segundo número é maior que o primeiro!")
# else:
#     print("Ambos os números são iguais!")

# 39 - Crie um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar 
# Se já passou do tempo de alistamento
# O programa deve apresentar o tempo que falta e/ou o que passou do prazo

# from datetime import datetime

# nome: str = input("Insira o seu nome: ")

# while True:
#     try:
#         ano: int = int(input("Insira o ano de nascimento: "))
#         if ano < 0:
#             print("Inserir ano válido.")
#             continue
#         break
#     except ValueError:
#         print("Insira os dados corretamente.")

# atual: int = datetime.now().year
# diferenca: int = atual - ano
# if diferenca < 18:
#     print(f'{nome}, você ainda vai se alistar para o serviço militar. Faltam {18 - diferenca} ano(s)')
# elif diferenca == 18:
#     print(f'{nome}, é hora de se alistar para o serviço militar!')
# else:
#     print(f'Você passou da hora de se alistar para o serviço militar em {diferenca - 18} ano(s), {nome}.')


# 40 - Crie um programa que leia duas notas de um aluno e calcule sua média. Mostre uma mensagem no final de acordo com a media atingida
# Media abaixo de 5.0: REPROVADO
# Media entre 5.0 e 6.9: RECUPERACAO
# Media 7.0 ou superior: APROVADO

# import statistics

# try:
#     nota_01: float = float(input("Insira a primeira nota: "))
#     nota_02: float = float(input("Insira a segunda nota: "))
#     media: float =  statistics.median([nota_01, nota_02])
# except ValueError:
#     print("Valores inseridos incorretamente.")

# if media < 5.0:
#     print(f'Aluno REPROVADO!. Média de notas de {media} pontos.')
# elif media >= 5.0 and media <= 6.9:
#     print(f'Aluno em RECUPERAÇÃO. Média de notas de {media} pontos.')
# else:
#     print(f'Aluno APROVADO com uma média de notas de {media} pontos. PARABÉNS!')


# 41 - A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
# até 9 anos : mirim
# até 14 anos: infantil
# até 19 anos: Junior
# até 20 anos: Senior
# Acima: Master

# from datetime import datetime

# while True:
#     try:
#         ano: int = int(input("Informe o ano de nascimento do atleta: "))
#         if ano < 0:
#             print("Gentileza informar o ano corretamente.")
#             continue
#         break
#     except ValueError:
#         print("Dados informados incorretamente.")

# ano_atual: int = datetime.now().year
# idade: int = ano_atual - ano

# if idade <= 9:
#     print("Atleta deve ser inscrito na categoria: MIRIM")
# elif idade <= 14:
#     print("Atleta deve ser inscrito na categoria: INFANTIL")
# elif idade <= 19:
#     print("Atleta deve ser inscrito na categoria: JUNIOR")
# elif idade <= 20:
#     print("Atleta deve ser inscrito na categoria: SENIOR")
# else:
#     print("Atleta deve ser inscrito na categoria: MASTER")


# 42 - Refazer exercicio 35

# try:
#     x: float = float(input("Insira o primeiro lado (x): "))
#     y: float = float(input("Insira o segundo lado (y): "))
#     z: float = float(input("Insira o terceiro lado (z): "))

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

# 43 - Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcula seu imc e mostre seu status de acordo com tabela:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 ate 30: sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade morbida

# try:
#     peso: float = float(input("Informe o seu peso: "))
#     altura: float = float(input("Informe sua altura: "))
# except ValueError:
#     print("Formato de dados incorretos.")

# imc: float = peso / (altura ** 2)
# if imc < 18.5:
#     print(f'Você está muito abaixo do peso. Seu IMC é de: {imc:.2f}.')
# elif imc >= 18.5 and imc < 25.0:
#     print(f'Seu peso está ideal. Seu IMC é de: {imc:.2f}.')
# elif imc >= 25.0 and imc < 30.0:
#     print(f'Você está com sobrepeso. Seu IMC é de: {imc:.2f}')
# elif imc >= 40.0 and imc <= 40.0:
#     print(f'Você está obeso. Seu IMC está em {imc:.2f}')
# else:
#     print(f'Você está com obesidade mórbida. Seu IMC está em {imc:.2f}')



# 44 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# A vista dinheiro/cheque: 10% de desconto
# A vista cartao : 5% de desconto
# em até 2 vezes no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

# try:
#     preco: float = float(input("Informe o valor do produto: "))
    
#     print("Escolha a condição de pagamento:")
#     print("--------" * 20)
#     print("[ 1 ] - À vista dinheiro/Cheque")
#     print("[ 2 ] - À vista cartão")
#     print("[ 3 ] - Até 2x no cartão")
#     print("[ 4 ] - Até 3x ou mais no cartão")
#     print("--------" * 20)

#     opcao: int = int(input("Escolha sua opção de pagamento: "))

#     if opcao == 1:
#         print(f'O valor do produto será de R$ {preco - (preco * 0.10):.2f} reais.')
#     elif opcao == 2:
#         print(f'O valor do produto será de R$ {preco - (preco * 0.05):.2f} reais.')
#     elif opcao == 3:
#         print(f'O valor do produto será de R$ {preco:.2f} reais.')
#     elif opcao == 4:
#         print(f'O valor do produto será de R$ {preco + (preco * 0.20):.2f} reais.')
#     else:
#         print("Opção inválida! Escolha uma opção entre 1 e 4.")

# except ValueError:
#     print("Erro: Você deve inserir um número válido.")


# 45 - Crie um programa que faça o computador jogar jokenpô com você.

# from random import choice
# from time import sleep

# jogador: str =  input("Insira sua escolha: ").lower()
# opcoes: list = ["pedra", "papel", "tesoura"]
# computador: str = choice(opcoes)
# print("JO...")
# sleep(1)
# print("KEN...")
# sleep(1)
# print("PO...")
# sleep(1)
# print("Ambos mostram as mãos...")
# sleep(1)
# if jogador == "pedra" and computador == "papel":
#     print("VocÊ PERDEU!")
#     print(f'Você escolheu {jogador} e o computador escolheu {computador}.')
# elif jogador == "pedra" and computador == "tesoura":
#     print("Você GANHOU!")
#     print(f'Você escolheu {jogador} e o computador escolheu {computador}.')
# elif jogador == "papel" and computador == "tesoura":
#     print("Você PERDEU!")
#     print(f'Você escolheu {jogador} e o computador escolheu {computador}.')
# elif jogador == "papel" and computador == "pedra":
#     print("Você GANHOU!")
#     print(f'Você escolheu {jogador} e o computador escolheu {computador}.')
# elif jogador == "tesoura" and computador == "pedra":
#     print("Você PERDEU!")
#     print(f'Você escolheu {jogador} e o computador escolheu {computador}.')
# elif jogador == "tesoura" and computador == "papel":
#     print("Você GANHOU!")
#     print(f'Você escolheu {jogador} e o computador escolheu {computador}.')
# else:
#     print("Empatamos! Ambas as nossas opções foram iguais.")
#     print(f'Você escolheu {jogador} e o computador escolheu {computador}.')

# 46 - Faça um programa que mostre uma tela com uma contagem regressiva para o estouro de fogos de artificio. Indo de 10 a 0 com uma pausa de 1 segundo entre elas.

# from time import sleep

# for c in range(10, 0, -1):
#     print(c)
#     sleep(1)
# fogos: str = print("BUM!  BUM !  POOOOW!!!")


# 47 - Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 a 50

# for c in range(1, 50):
#     if c % 2 == 0: 
#         print(c, end=' ')

#COMENTÁRIO: Para printar as informações na "mesma linha", podemos utilizar end= dentro do nosso comando PRINT.


# 48 - Faça um programa que calcula a soma entre todos os números impares que são multiplos de 3 e que se encontram no intervalo entre 1 a 500

# try:
#     soma: int = 0
#     contador: int = 0
#     for c in range(1, 501):
#         if c % 2 != 0 and c % 3 == 0:
#             contador += 1
#             soma += c
#     print(f'A soma de todos os {contador} números ímpares entre 1 a 500 é: {soma}')

# except ValueError as m:
#     print(m)
 
# 49 - Refaça o exercicio 9, mostrando a tabuada de um número que o usuário escolher. Só que agora utilizando o laço for.

# try:
#     numero: int = int(input("Insira seu número: "))
#     for i in range(1, 11):
#         tabuada = i * numero
#         print(f'A multiplicação de {numero} x {i} = {tabuada}')
# except ValueError as a:
#     print(a)

# 50 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

# soma: int = 0
# numeros: int = 0
# contador: int = 0
# for c in range(1,7):
#     numeros: int = int(input(f'Insira o {c}º número: '))
#     if numeros % 2 == 0:
#         soma += numeros
#         contador += 1
#     else:
#         print("Número informado é ímpar. Vamos desconsidera-lo.")
# print(f'A soma dos {contador} números pares informados é: {soma}')

# 51 - Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final mostre os 10 primeiros termos dessa progressão.

# linha: str = "==" * 20
# print(linha)
# print("10 TERMOS DE UMA PA".center(len(linha)))
# print(linha)

# try:
#     termo: int = int(input("Primeiro termo: "))
#     razao: int = int(input("Razão: "))
#     decimo: int = termo + (10 - 1) * razao

#     for c in range(termo, decimo + razao, razao):
#         print(f'{c}', end=" -> ")
#     print("ACABOU!")

# except ValueError as m:
#     print(m)


# 52 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# try:
#     numero: int = int(input("Digite um número: "))
#     total: int = 0
#     for c in range(1, numero + 1):
#         if numero % c == 0:
#             print('\033[34m', end='')
#             total += 1
#         else:
#             print('\033[m', end='')
#         print(f'{c}', end=' ')

#     print(f'\nO número {numero} foi divisível {total} vezes')
#     if total == 2:
#         print('E por isso ele é PRIMO!')
#     else:
#         print('E por isso ele NÃO É PRIMO!')

# except ValueError as m:
#     print(m)


# 53 - Crie um programa criando uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.

# try:
#     frase: str = input("Digite uma frase: ")
#     frase_sem_espaco: str = frase.replace(" ", "").upper().strip()
#     frase_invertida: str = frase_sem_espaco[::-1]
#     print(f'O inverso de {frase_sem_espaco} é {frase_invertida}.')
#     if frase_sem_espaco == frase_invertida:
#         print("Temos um palíndromo!")
#     else:
#         print("A frase digitada não é um palíndromo!")
# except ValueError as mensagem:
#     print(mensagem)


# 54 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

# from datetime import date

# menor: int = 0
# maior: int = 0

# for c in range(1,8):
#     datas: int = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
#     if (date.today().year - datas) < 18:
#         menor += 1
#     else:
#         maior += 1
# print(f'Ao todo tivemos {maior} pessoas maiores de idade.\nE também tivemos {menor} pessoas menores de idade.')



# 55 - Faça um programa qu leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lido

# try:
#     pesos: list = []

#     for c in range(1,6):
#         peso: float = float(input(f'Peso da {c}ª pessoa: '))
#         pesos.append(peso)
#     print(f'O maior peso lido foi de {max(pesos)}kg.')
#     print(f'O menor peso lido foi de {min(pesos)}kg.')

# except ValueError as m:
#     print(m)

# 56 - Desenvolva um programa que leia, nome, idade e sexo de 4 pessoas. No final do programa mostre:
# a média de idade do grupo
# qual o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos


# nome: str = ''
# idade: int = 0
# sexo: str = ''
# totalidade: int = 0
# mediaidade: float = 0
# maiorhomem: int = 0
# nomehomem: str = ''
# mulheres: int = 0

# for c in range(1, 5):
#     print(f'----- {c}ª PESSOA -----')
#     nome = input("Nome: ")
#     idade = int(input("Idade: "))
#     sexo = input("Sexo [M/F]: ").strip().upper()
#     totalidade += idade
#     if c == 1 and sexo == "M":
#         maiorhomem = idade
#         nomehomem = nome
#     if sexo == "M" and idade > maiorhomem:
#         maiorhomem = idade
#         nomehomem = nome
#     if sexo == "F" and idade < 20:
#         mulheres += 1

# mediaidade = totalidade / 4

# print(f'A média de idade do grupo é de {mediaidade} anos.')
# if nomehomem != '':
#     print(f'👴 O homem mais velho é {nomehomem} com {maiorhomem} anos.')
# else:
#     print("❌ Não há homens cadastrados.")

# if mulheres > 0:
#     print(f'👧 Há {mulheres} mulher(es) com menos de 20 anos.')
# else:
#     print("❌ Não há mulheres cadastradas.")

#57 - Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.

# while True:
#     sexo: str = str(input("Gentileza informar o sexo. Se M/F: ")).strip().upper()[0]
#     if sexo != "M" and sexo != "F":
#         print("Informe um sexo válido.")
#         continue
#     break
# print(f'Sexo {sexo} registrado com sucesso.')


#58 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram necessários para vencer.

# import random
# from time import sleep
# tentativas: int = 0
# numero: int = random.randint(0, 10)
# print("-=-" * 20)
# print("Sou seu computador...")
# sleep(1)
# print("Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?")
# print("-=-" * 20)

# while True:
#     adivinha: int = int(input("Qual é o seu palpite? "))
#     tentativas += 1
#     if adivinha < numero:
#         print("Mais...Tente mais uma vez.")
#     elif adivinha > numero:
#         print(f'Menos...Tente mais uma vez.')
#         continue
#     else:
#         print(f'Acertou com {tentativas} tentativa(s). Escolhi {numero}. Parabéns!')
#     break    


#59 - Crie um programa que leia 2 valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa
# O programa deverá realizar a ação solicitada em cada caso.

primeiro: int = int(input("Primeiro valor: "))
segundo: int = int(input("Segundo valor: "))
menu: int = 0

while menu != 5:
    print("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa")
    menu: int = int(input(">>>>>> Qual é a sua opção? "))
    if menu == 1:
        print(f'A soma entre {primeiro} e {segundo} é: {primeiro + segundo}')
    elif menu == 2:
        print(f'A multiplicação entre {primeiro} e {segundo} é: {primeiro * segundo}')
    elif menu == 3:
        print(f'O maior número entre {primeiro} e {segundo} é: {max(primeiro, segundo)}')
    elif menu == 4:
        print("Informe os números novamente: ")
        primeiro: int = int(input("Primeiro valor: "))
        segundo: int = int(input("Segundo valor: "))
    elif menu > 5:
        print("Opção inválida. Tente novamente")
    else:
        print("Finalizando...")
        print("=-==-" * 30)
        print("Fim do programa. Volte sempre!")

#60 - Faça um programa que leia um número qualquer e mostre o seu fatorial: Ex 5! = 5x4x3x2x1 = 120
#61 - Refaça o DESAFIO 051, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura WHILE
#62 - Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
#63 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma sequência fibonacci. Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
#64 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o FLAG)
#65 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
# o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
