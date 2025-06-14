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

# from time import sleep

# primeiro: int = int(input("Primeiro valor: "))
# segundo: int = int(input("Segundo valor: "))
# menu: int = 0

# while menu != 5:
#     print("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa")
#     menu: int = int(input(">>>>>> Qual é a sua opção? "))
#     sleep(2)
#     if menu == 1:
#         print(f'A soma entre {primeiro} e {segundo} é: {primeiro + segundo}')
#     elif menu == 2:
#         print(f'A multiplicação entre {primeiro} e {segundo} é: {primeiro * segundo}')
#     elif menu == 3:
#         print(f'O maior número entre {primeiro} e {segundo} é: {max(primeiro, segundo)}')
#     elif menu == 4:
#         print("Informe os números novamente: ")
#         primeiro: int = int(input("Primeiro valor: "))
#         segundo: int = int(input("Segundo valor: "))
#     elif menu > 5:
#         print("Opção inválida. Tente novamente")
#     else:
#         print("Finalizando...")
#         print("=-==-" * 30)
#         print("Fim do programa. Volte sempre!")

#60 - Faça um programa que leia um número qualquer e mostre o seu fatorial: Ex 5! = 5x4x3x2x1 = 120

# import math

# fatorial: int = int(input("Digite um número para calcular o seu fatorial: "))

# print(f'Calculando {fatorial}! = ', end='')
# for c in range(2, fatorial + 1)[::-1]:
#     print(f'{c}', end=' x ')
# print(f'1 = {math.factorial(fatorial)}')

# UTILIZANDO WHILE

# fatorial: int = int(input("Digite o número para calcular o seu fatorial: "))
# contador: int = fatorial

# print(f'Calculando {fatorial}! = ', end='')
# while contador > 0:
#     print(f'{contador}', end='')
#     if contador > 1:
#         print(" x ", end='')
#     else:
#         print(" = ", end='')
#     contador -= 1
# print(f'{math.factorial(fatorial)}')


#61 - Refaça o DESAFIO 51, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura WHILE

# linha: str = "==" * 20
# print(linha)
# print("10 TERMOS DE UMA PA".center(len(linha)))
# print(linha)

# try:
#     termo: int = int(input("Primeiro termo: "))
#     razao: int = int(input("Razão: "))
#     decimo: int = termo + (10 - 1) * razao

#     while termo <= decimo:
#         print(f'{termo}', end=" -> ")
#         termo += razao
#     print("ACABOU!")

# except ValueError as m:
#     print(m)

#62 - Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

# linha: str = "==" * 20
# print(linha)
# print("10 TERMOS DE UMA PA".center(len(linha)))
# print(linha)

# try:
#     termo: int = int(input("Primeiro termo: "))
#     razao: int = int(input("Razão: "))
#     iterador: int = 1
#     contagem: int = 10
#     limite: int = 0

#     while contagem != 0:
#         limite = limite + contagem
#         while iterador <= limite:
#             print(f'{termo}', end=" -> ")
#             termo += razao
#             iterador += 1
#         print("Aguardando...")
#         contagem: int = int(input("Quantos termos você quer mostrar a mais? "))
#     print(f'Progressão finalizada com {limite} termos mostrados')

# except ValueError as m:
#     print(m)

#63 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma sequência fibonacci. Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

# print("---" * 10)
# print("Sequência de Fibonacci")
# print("---" * 10)
# numero: int = int(input("Informe a quantidade de números que deseja apresentar: "))
# a: int = 0
# b: int = 1
# c: int = 0
# iterador: int = 0
# while iterador < numero:
#     print(f'{c}', end=' -> ')
#     a = b
#     b = c
#     c = a + b
#     iterador += 1
# print("FIM")


#64 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o FLAG)

# soma: int = 0
# contador: int = 0
# numero: int = int(input("Digite um número: "))

# while numero != 999:
#     soma += numero
#     contador += 1
#     numero: int = int(input("Digite um número: "))

# print(f'A quantidade de números digitados foi {contador} e a somatória de todos os números é: {soma}')


#65 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
# o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

# soma: int = 0
# contador: int = 0
# continuar: str = "S"
# lista: list = []

# while continuar == "S":
#     numero: int = int(input("Digite um número: "))
#     soma += numero
#     lista.append(numero)
#     contador += 1
#     continuar: str = str(input("Deseja continuar? [S/N] ")).upper()
# print(f'A média entre os valores digitados é {soma/contador}. O maior valor digitado foi {max(lista)} e o menor valor digitado foi {min(lista)}')

#66 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre eles (DESCONSIDERANDO O FLAG) - Utilizar o modo de interrupção de repetições/laços.

# soma: int = 0
# contador: int = 0
# lista: list = []

# while True:
#     numero: int = int(input("Digite um número (999 para parar): "))
#     if numero == 999:
#         break
#     soma += numero
#     contador += 1
#     lista.append(numero)

# print(f'A média entre os valores digitados é {soma/contador}. O maior valor digitado foi {max(lista)} e o menor valor digitado foi {min(lista)}')

#67 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número
# digitado for NEGATIVO.

# try:
#     while True:
#         numero: int = int(input("Digite um número para apresentação de tabuada: "))
#         if numero <= 0:
#             break
#         print("-=-=-" * 30)
#         print(f'A TABUADA DO NÚMERO {numero}.')
#         print("-=-=-" * 30)
#         for c in range(1, 11):
#             tabuada: int = c * numero
#             print(f'{numero} x {c} = {tabuada}')
#     print("PROGRAMA TABUADA ENCERRADO. Volte Sempre!")

# except ValueError as m:
#     print(m)

#68 - Faça um programa que jogue PAR ou IMPAR com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.

# import random


# print("=-=" * 30)
# print("VAMOS JOGAR PAR OU ÍMPAR")
# print("=-=" * 30)

# contador: int = 0

# while True:
#     jogador: int = int(input("Diga um valor: "))
#     computador: int = random.randint(0, 10)
#     total: int = jogador + computador
#     escolha: str = ' '
#     while escolha not in 'PI':
#         escolha: str = str(input("PAR ou ÍMPAR? [P/I] ")).strip().upper()[0]
#     print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
#     if total % 2 == 0:
#         print("DEU PAR.")
#     else:
#         print("DEU ÍMPAR.")
#     if escolha == "P":
#         if total % 2 == 0:
#             print("Você VENCEU!")
#             contador += 1
#         else:
#             print("Você PERDEU!")
#             break
#     elif escolha == "I":
#         if total % 2 == 1:
#             print("Você VENCEU!")
#             contador += 1
#         else:
#             print("Você PERDEU!")
#             break
# print(f'GAME OVER! Você venceu {contador}')
    



#69 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrados
# Quantas mulheres tem menos de 20 anos.

# contador_idade: int = 0
# contador_homem: int = 0
# contador_mulheres: int = 0
# continua: str = ' '

# while True:
#     print("---" * 40)
#     print("CADASTRE UM PESSOA")
#     print("---" * 40)
#     idade: int = int(input("Idade: "))
#     sexo: str = str(input("Sexo: [M/F] ")).strip().upper()[0]
#     print("---" * 40)
#     if idade >= 18 or sexo == "M":
#         contador_idade += 1
#         contador_homem += 1
#     elif sexo == "M":
#         contador_homem += 1
#     elif idade < 20 and sexo == "F":
#         contador_mulheres += 1
#     continua: str = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
#     if continua != "S":
#         break
# print(f'Total de pessoas com mais de 18 anos: {contador_idade}.')
# print(f'Ao todo temos {contador_homem} homens cadastrados.')
# print(f'E temos {contador_mulheres} mulheres com menos de 20 anos.')


#70 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:
# Qual é o total gasto na compra
# Quantos produtos custam mais de 1000 reais
# Qual é o nome do produto mais barato.

# continuar: str = ' '
# contador: int = 0
# itens: int = 0
# total: int = 0
# produto_menor: str = ' '
# menor: float = float('inf')

# while True:
#     produto: str = str(input("Nome do produto: "))
#     preco: float = float(input("Preço: R$ "))
#     if preco < menor:
#         menor = preco
#         produto_menor = produto
#     if preco > 1000:
#         contador += 1
#     quantidade: int = int(input("Quantidade: "))
#     itens += quantidade
#     total += preco
#     while continuar not in 'SN':
#         continuar: str = str(input("Quer continuar? [S/N ] ")).strip().upper()[0]
#     if continuar == "N":
#         break
# print("------------------- FIM DO PROGRAMA ---------------------")
# print(f'O total da compra realizada foi de R${total}. E a quantidade de itens vendida foi de {itens}')
# print(f'Temos {contador} produto(s) custando mais de R$ 1.000,00.')
# print(f'O produto mais barato foi a {produto_menor} que custa {menor}.')




#71 - Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio pergunte ao usuário qual o valor a ser sacado. O programa vai informar quantas cédulas de 
# cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de 50, 20, 10 e 1

# saque: int = 0
# r50: int = 0
# r20: int = 0
# r10: int = 0
# r1: int = 0

# print('                     INTER BANK                       ')
# print('-------------------- BEM VINDO! --------------------')
# print('Sistema operacional: Xpgdkffss v.01')
# while saque == 0:
#     saque: int = int(input("Que valor você quer sacar? R$ "))
# while saque >= 50:
#     saque -= 50
#     r50 += 1
# while saque >= 20:
#     saque -= 20
#     r20 += 1
# while saque >= 10:
#     saque -= 10
#     r10 += 1
# while saque >= 1:
#     saque -= 1
#     r1 += 1
# print(f'O saque do valor solicitado foi realizado com sucesso. \nLiberadas: \n{r50} cédulas de R$50,00.\n{r20} cédulas de R$20,00.\n{r10} cédulas de R$10,00.\n{r1} cédulas de R$1,00.')

#72 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero a vinte. 
# nosso programa deve ler um número pelo teclado (também de 0 a 20) e mostra-lo por extenso.

# tupla: tuple = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", 
#                 "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

# while True:
#     numero: int = int(input("Digite um número entre 0 a 20: "))
#     while numero < 0 or numero > 20:
#         numero: int = int(input("Tente novamente. Digite um número entre 0 a 20: "))
#     if numero >= 0 or numero <= 20:
#         break
# print(f'Você digitou o número {tupla[numero]}')

#73 - Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro 2025 na ordem atual de colocação. Depois mostre, 
# Apenas os 5 primeiros colocados
# Os 4 últimos da tabela
# Lista com ordem alfabética
# Em que posição encontra-se o Atletico-MG

# times: tuple = ('Flamengo', 'Palmeiras', 'Bragantino', 'Cruzeiro', 'Fluminense', 'Internacional', 'Bahia', 'Botafogo', 'Ceara',
#                 'São Paulo', 'Vasco', 'Corinthians', 'Juventude', 'Mirassol', 'Fortaleza', 'Vitória', 'Atlético-MG', 'Grêmio', 'Santos', 'Sport')

# print("-=-" * 50)
# print(f'Lista de times do brasileirão: {times}')
# print("-=-" * 50)
# print(f'Os cinco primeiros colocados são: {times[:5]}')
# print("-=-" * 50)
# print(f'Os quatro últimos colocados (Zona de Rebaixamento) são: {times[-4:]}')
# print("-=-" * 50)
# print(f'Os times em órdem alfabética são: {sorted(times)}')
# print("-=-" * 50)
# print(f'O {times[16]} está na {times.index("Atlético-MG")}ª posição.')
# print("-=-" * 50)

#74 - Crie um programa que vai gerar 5 números aleatórios e inserir em uma tupla. Depois disso, mostre a listagem de numeros gerados e também indique o menor e o maior
# valor que está na tupla.

# from random import choices

# numeros: tuple = choices(range(10), k=5)
# print(f'Os valores sorteados foram: {numeros}')
# print(f'O maior valor sorteado foi {max(numeros)}.\nO menor valor sorteado foi {min(numeros)}.')

#75 - Desenvolva um programa que leia 4 valores no teclado e guarde-os em uma tupla. No final mostre:
# quantas vezes apareceu o numero 9
# em que posição foi digitado o primeiro valor 3
# quais foram os números pares

# pares: int = 0
# n1: int = int(input("Digite um número: "))
# n2: int = int(input("Digite outro número: "))
# n3: int = int(input("Digite mais um número: "))
# n4: int = int(input("Digite o último número: "))
# tupla: tuple = (n1, n2, n3, n4)
# for numeros in tupla:
#     if numeros % 2 == 0:
#         pares += 1
# print(f'Você digitou os valores {tupla}')
# print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
# if 3 in tupla:
#     print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição.')
# else:
#     print("O valor 3 não foi digitado em nenhuma posição.")
# print(f'Os valores pares digitados foram {pares}.')


#76 - Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços. No final mostre uma listagem de preços organizando os dados em forma tabular.

# produtos: tuple = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
#             "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

# print("---" * 17)
# print("LISTAGEM DE PREÇOS".center(51))
# print("---" * 17)
# for p in range(0, len(produtos),2):
#     print(f'{produtos[p]:.<40}',f'R${produtos[p+1]:.7}')
# print("---" * 17)

#77 - Crie um programa que tenha uma tupla com várias palavras (nao usar acentos). Depois disso, voce deve mostrar, para cada palavra, quais são as suas vogais.

# palavras = ('aprender', 'programar', 'linguagem', 'python',
#             'curso', 'gratis', 'estudar', 'praticar',
#             'trabalhar', 'mercado', 'programador', 'futuro')

# for p in palavras:
#     print(f'Na palavra {p.upper()} temos ', end='')
#     for letra in p:
#         if letra.lower() in 'aeiou':
#             print(f'{letra}', end=' ')
#     print()

#78 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior
# e o menor valor digitado e as suas respectivas posições na lista

# lista: list = []

# for numeros in range(0, 5):
#     numeros: int = int(input(f'Digite um valor para posição {numeros}: '))
#     lista.append(numeros)
# print(f'Nossa lista criada foi: {lista}')
# print(f'O menor valor digitado foi {min(lista)} e encontra-se na posição {lista.index(min(lista))}.')
# print(f'O maior valor digitado foi {max(lista)} e encontra-se na posição {lista.index(max(lista))}.')

#79 - Crie um programa onde um usuário crie vários valores numéricos e cadastre-os em uma lista. Caso o número já exista la dentro
# ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente.

# lista: list = []


# while True:
#     numeros: int = int(input("Digite um valor: "))
#     if numeros not in lista:
#         lista.append(numeros)
#         print("Valor adicionado com sucesso...")
#     else:
#         print("Valor duplicado! Não vou adicionar...")
    
#     continua: str = " "
#     while continua not in 'SN':
#        continua: str = str(input("Quer continuar? [S/N ] ")).strip().upper()[0]
#     if continua == "N":
#          break
# lista.sort()
# print(f'Você digitou os valores {lista}')

# 80 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort). No final mostre a lista ordenada na tela.

# lista: list = []

# for _ in range(0, 5):
#     numeros: int = int(input("Digite um valor: "))
#     posicao: int = 0  # Reinicia a posição a cada iteração
#     while posicao < len(lista) and numeros > lista[posicao]:
#         posicao += 1
#     print(f'Adicionando o número {numeros} na posição {posicao} da lista...')
#     lista.insert(posicao, numeros)

# print(f'{lista}')

#81 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
# Quantos números foram digitados
# A lista de valores de forma decrescente
# E se o valor 5 está ou não na lista

# lista: list = []

# while True:
#     numeros: int = int(input("Digite um valor: "))
#     lista.append(numeros)
#     continua: str = " "
#     while continua not in 'SN':
#        continua: str = str(input("Quer continuar? [S/N ] ")).strip().upper()[0]
#     if continua == "N":
#          break
# lista.sort(reverse=True)
# print(f'Você digitou {len(lista)} elementos.')
# print(f'Os valores em ordem decrescente são {lista}')
# if 5 in lista:
#     print(f'O valor 5 faz parte da lista!')
# else:
#     print("O valor 5 não faz parte da lista!")

#82 - Crie um programa que vai ler vários numeros e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os impares digitados, respectivamente.
# ao final mostre o conteúdo das três listas geradas.

# lista: list = []
# par: list = []
# impar: list = []

# while True:
#     numeros: int = int(input("Digite um valor: "))
#     lista.append(numeros)
#     continuar: str = " "
#     while continuar not in 'SN':
#         continuar: str = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
#     if continuar == "N":
#         break
# for numero in lista:
#     if numero % 2 == 0:
#         par.append(numero)
#     else:
#         impar.append(numero)
# print(f'A lista completa é: {lista}')
# print(f'A lista de pares é: {par}')
# print(f'A lista de ímpares é: {impar}')

#83 - Crie um programa onde o usuário digite uma expressao qualquer que use parenteses. Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.

# expressao: str = input("Digite a expressão: ")
# parenteses: int = 0

# for p in expressao:
#     if p == "(":
#         parenteses += 1
#     elif p == ")":
#         parenteses -= 1
#     if parenteses < 0:
#         break

# if parenteses == 0:
#     print("Expressão válida!")
# else:
#     print("Expressão inválida!")

#84 - Crie um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# quantas pessoas foram cadastradas
# listagem com as mais pesadas (nome)
# listagem com as mais leves (nome)

# principal: list = []
# cadastro: list = []

# while True:
#     nome: str = input("Digite o nome: ")
#     peso: float = float(input("Digite o peso: "))
#     cadastro.append(nome)
#     cadastro.append(peso)
#     continuar: str = ' '
#     principal.append(cadastro[:])
#     while continuar not in 'SN':
#         continuar: str = input("Deseja continuar? [S/N] ").strip().upper()[0]
#     if continuar == "N":
#         break
#     cadastro.clear()

# maior: float = max(pessoa[1] for pessoa in principal)
# menor: float = min(pessoa[1] for pessoa in principal)

# print(f'A lista de pessoas cadastradas é: {principal}')
# print(f'Ao todo, você cadastrou {len(principal)} pessoas.')

# print(f'O maior peso foi de {maior}kg. Peso de ', end='')
# for pessoa in principal:
#     if pessoa[1] == maior:
#         print(f'[{pessoa[0]}] ', end='')

# print(f'\nO menor peso foi de {menor}kg. Peso de ', end='')
# for pessoa in principal:
#     if pessoa[1] == menor:
#         print(f'[{pessoa[0]}] ', end='')


#85 - Crie um programa onde um usuário possa digitar 7 valores numericos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final 
# mostre os valores pares e impares em ordem crescente

# lista: list = [[],[]]

# for c in range(1,8):
#     numero: int = int(input(f'Digite o {c}º valor: '))
#     if numero % 2 == 0:
#         lista[0].append(numero)
#     else:
#         lista[1].append(numero)
# lista[0].sort()
# lista[1].sort()
# print("-=" * 30)
# print(f'Os valores pares digitados foram {lista[0]}')
# print(f'Os valores ímpares digitados foram {lista[1]}')


#86 - Crie um programa que leia uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

# matriz: list = [[], [], []]

# for c in range(0,9):
#     numero: int = int(input("Digite um valor: "))
#     if c < 3:
#         matriz[0].append(numero)
#     elif c < 6:
#         matriz[1].append(numero)
#     else:
#         matriz[2].append(numero)

# print("-=" * 30)
# for linha in matriz:
#     print(f'[ {linha[0]:^3} ] [ {linha[1]:^3} ] [ {linha[2]:^3} ]')
# print("-=" * 30)

#87 - Aprimore o desafio anterior, mostrando no final. 
# A soma de todos os números pares digitados
# A soma dos valores da terceira coluna
# O maior valor da segunda linha

# matriz: list = [[], [], []]
# par: int = 0

# for c in range(0,9):
#     numero: int = int(input("Digite um valor: "))
#     if numero % 2 == 0:
#         par += numero
#     if c < 3:
#         matriz[0].append(numero)
#     elif c < 6:
#         matriz[1].append(numero)
#     else:
#         matriz[2].append(numero)
# print("-=" * 30)
# for linha in matriz:
#     print(f'[ {linha[0]:^3} ] [ {linha[1]:^3} ] [ {linha[2]:^3} ]')
# print("-=" * 30)
# print(f'A soma dos valores pares é {par}.')
# print(f'A soma dos valores da terceira coluna é {sum(matriz[2])}.')
# print(f'O maior valor da segunda linha é {max(matriz[1])}.')

#88 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números 
# entre 1 a 60 para cada jogo. Cadastrando tudo em uma lista composta.

# import random

# jogos: list = []
# quantidade: int = int(input("Quantos jogos deseja realizar? "))

# for numero in range(quantidade):
#     sorteio = sorted(random.sample(range(1, 61), 6))
#     jogos.append(sorteio)

# for i, jogo in enumerate(jogos, 1):
#     print(f"Jogo {i}: {jogo}")

#89 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e 
# permita que o usuário possa mostrar as notas de cada aluno individualmente.

# escola: list = []
# auxiliar: list = []
# indice: int = 0

# while True:
#     nome: str = input("Digite o nome do aluno: ")
#     nota_1: float = float(input("Digite a primeira nota: "))
#     nota_2: float = float(input("Digite a segunda nota: "))
#     media: float = (nota_1 + nota_2) / 2
#     auxiliar.append(nome)
#     auxiliar.append(nota_1)
#     auxiliar.append(nota_2)
#     auxiliar.append(media)
#     escola.append(auxiliar[:])
#     auxiliar.clear()
#     continuar: str = " "
#     while continuar not in 'SN':
#         continuar: str = input("Deseja continuar? [S/N] ").strip().upper()[0]
#     if continuar == "N":
#         break
# print("-=" * 30)
# print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
# print("--" * 26)
# for i, a in enumerate(escola):
#     print(f'{i:<4}{a[0]:<10}{a[3]:>8.1f}')

# print("--" * 26)

# while True:
#     indice: int = int(input("De qual aluno gostaria de ver a nota? (999 interrompe) "))
#     if indice == 999:
#         print("FINALIZANDO...")
#         break
#     if indice < 0 or indice >= len(escola):
#         print("Opção inválida. Não há esse cadastro na base. Tente novamente!")
#     else:
#         print(f'Notas de {escola[indice][0]} são {escola[indice][1]} e {escola[indice][2]}')

#90 - Faça um programa que leia o NOME e a MÉDIA de um aluno. Guardando também a SITUAÇÃO em um dicionário. No final mostre o conteúdo da estrutura na tela.

# dicionario: dict = {}

# dicionario['Nome'] = str(input("Nome: "))
# dicionario['Média'] = float(input(f'Média de {dicionario["Nome"]}: '))
# print(f'Nome é igual a {dicionario["Nome"]}.')
# print(f'Média é igual a {dicionario["Média"]}.')
# if dicionario["Média"] >= 7:
#     print("Situação é igual a APROVADO.")
# else:
#     print("Situação é igual a REPROVADO.")

#91 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em
# ordem, sabendo que o vencedor tirou o maior número dado.

# import random
# from time import sleep

# dicionario: dict = {}
# dicionario_ordenado: dict = {}

# for j in range(1, 4):
#     dicionario['Jogador1'] = random.randint(1, 6)
#     dicionario['Jogador2'] = random.randint(1, 6)
#     dicionario['Jogador3'] = random.randint(1, 6)
#     dicionario['Jogador4'] = random.randint(1, 6)

# print("Valores Sorteados: ")
# sleep(1)
# print(f'O jogador1 tirou {dicionario["Jogador1"]}')
# sleep(1)
# print(f'O jogador2 tirou {dicionario["Jogador2"]}')
# sleep(1)
# print(f'O jogador3 tirou {dicionario["Jogador3"]}')
# sleep(1)
# print(f'O jogador4 tirou {dicionario["Jogador4"]}')

# dicionario_ordenado = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True))

# print("Ranking dos jogadores: ")
# for i, (jogador, valor) in enumerate(dicionario_ordenado.items(), start=1):
#     print(f'{i}º lugar: {jogador} com {valor}')

#92 - Crie um programa que leia nome, ano de nascimento e a carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a ctps for diferente de ZERO
# o dicionário receberá também o ano de contratação e o salário. Calcula e acrescente, além da idade com quantos anos a pessoa vai se aposentar.

# import datetime

# dicionario: dict = {}
# nascimento: int = 0
# ano: int = 0
# atual: int = datetime.date.today()
# aposentadoria: int = 0

# dicionario['Nome'] = str(input("Nome: "))
# nascimento: int = int(input("Ano de Nascimento: "))
# ano: int = atual.year - nascimento
# dicionario['Idade'] = ano
# dicionario['CTPS'] = int(input("Carteira de trabalho (Digite 0 se não possuir): "))
# if dicionario['CTPS'] != 0:
#     dicionario['Contratação'] = int(input("Ano de contratação: "))
#     dicionario['Salário'] = float(input("Salário: R$ "))

# print("-=-" * 40)
# print(f'Nome digitado: {dicionario['Nome']}')
# print(f'Idade: {dicionario['Idade']}')
# print(f'CTPS digitada: {dicionario['CTPS']}')
# print(f'Ano de contratação: {dicionario["Contratação"]}')
# print(f'O salário atual é: R$ {dicionario['Salário']}')
# aposentadoria = 35 - (atual.year - dicionario['Contratação'])
# if aposentadoria < 0:
#     print(f'Funcionário já pode se aposentar. Possui {atual.year - dicionario["Contratação"]} anos trabalhados.')
# else:
#     print(f'Faltam {aposentadoria} anos para se aposentar.')

#93 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele fez.  Depois vai ler 
# a quantidade de gols feitos em cada partida. No final, tudo isso sera guardado em um dicionário incluindo o total de gols feitos durante o campeonato.

# partidas: int = 0
# gols: int = 0

# dicionario: dict = {
#     'Nome': '',
#     'Gols': [],
#     'Total': ''
# }

# dicionario['Nome'] = str(input("Nome do jogador: "))
# partidas: int = int(input(f'Quantas partidas {dicionario["Nome"]} jogou? '))

# for contador in range(1, partidas + 1):
#     gols = int(input(f'Quantos gols na partida {contador}ª? '))
#     dicionario['Gols'].append(gols)

# dicionario['Total'] = sum(dicionario['Gols'])

# print("-=-" * 40)
# print(dicionario)
# print("-=-" * 40)
# print(f'O campo nome tem o valor {dicionario["Nome"]}')
# print(f'O campo gols tem os valores {dicionario["Gols"]}')
# print(f'O campo total tem o valor {dicionario["Total"]}')
# print("-=-" * 40)
# print(f'O jogador {dicionario["Nome"]} jogou {partidas} partidas.')
# for partida in range (partidas):
#     print(f' => Na partida {partida + 1}, fez {dicionario["Gols"][partida]} gols.')

#94 - Crie um programa que leia, nome, sexo e idade de várias pessoas. Guardando os dados de cada um em um dicionário  e todos os dicionários em uma lista. No final mostre:
# Quantas pessoas foram cadastradas
# A média de idade do grupo
# uma lista com todas as mulheres
# uma lista com todas as pessoas com idade acima da média

# cadastros: list = []
# soma_idade: int = 0 
# mulheres: list = []
# acima_media: list = []


# while True:
#     cadastro = {}
#     cadastro['Nome'] = str(input("Nome: "))
#     cadastro['Sexo'] = str(input("Sexo: [M/F] "))

#     while cadastro["Sexo"] != "M" and cadastro["Sexo"] != "F":
#         print("ERRO! Por favor, digite apenas M ou F.")
#         cadastro['Sexo'] = str(input("Sexo: [M/F] "))

#     cadastro['Idade'] = int(input("Idade: "))

#     while cadastro["Idade"] < 0 or cadastro["Idade"] > 130:
#         print("ERRO! Por favor, digite uma idade válida.")
#         cadastro['Idade'] = int(input("Idade: "))

#     cadastros.append(cadastro.copy())
#     continua = str(input("Deseja continuar? [S/N] ")).strip().upper()

#     while continua not in 'SN':
#         print("Digite uma opção válida.")
#         continua = str(input("Deseja continuar? [S/N] ")).strip().upper()

#     if continua == "N":
#         break

# print("-=-" * 50)
# print(f'A) Ao todo temos {len(cadastros)} pessoas cadastradas.')
# for pessoa in cadastros:
#     soma_idade += pessoa['Idade']

# if len(cadastros) > 0:
#     print(f'B) A média de idade é de {soma_idade / len(cadastros):.2f} anos.')
# else:
#     print('B) Nenhuma pessoa cadastrada para calcular a média.')

# for pessoa in cadastros:
#     if pessoa['Sexo'] == 'F':
#         mulheres.append(pessoa['Nome'])
# if mulheres:
#     print(f'C) As mulheres cadastradas foram: {", ".join(mulheres)}')
# else:
#     print('C) Nenhuma mulher cadastrada.')

# for pessoa in cadastros:
#     if pessoa['Idade'] > soma_idade / len(cadastros):
#         acima_media.append(pessoa)
# print("D) Lista de pessoas que estão acima da média: ")
# for pessoa in acima_media:
#     print(f'Nome = {pessoa['Nome']},Sexo = {pessoa['Sexo']}, Idade = {pessoa['Idade']}')

# print("<< ENCERRADO >>")

#95 - Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

# historico = []

# while True:
#     dicionario = {}
#     dicionario['Nome'] = input("Nome do jogador: ")
#     partidas = int(input(f'Quantas partidas {dicionario["Nome"]} jogou? '))
    
#     gols = []
#     for contador in range(1, partidas + 1):
#         gol = int(input(f'Quantos gols na partida {contador}ª? '))
#         gols.append(gol)
    
#     dicionario['Gols'] = gols
#     dicionario['Total'] = sum(gols)
    
#     historico.append(dicionario)
    
#     while True:
#         resposta = input("Quer continuar? [S/N] ").strip().upper()[0]
#         if resposta in 'SN':
#             break
#         print("ERRO! Insira somente S ou N")
    
#     if resposta == 'N':
#         break

# print("-=-" * 40)
# print(f"{'Cod':<4}{'Nome':<15}{'Gols':<20}{'Total':<5}")
# print("-=-" * 40)
# for idx, jogador in enumerate(historico):
#     print(f"{idx:<4}{jogador['Nome']:<15}{str(jogador['Gols']):<20}{jogador['Total']:<5}")

# while True:
#     busca = int(input("Deseja visualizar os dados de qual jogador? (insira 999 para sair) "))
    
#     if busca == 999:
#         break
    
#     if busca < 0 or busca >= len(historico):
#         print(f'ERRO! Não existe jogador com o código {busca}!')
#     else:
#         print(f' -- LEVANTAMENTO DO JOGADOR {historico[busca]["Nome"]}')
#         for jogo, gols in enumerate(historico[busca]['Gols']):
#             print(f'    No jogo {jogo + 1} fez {gols} gols.')
    
#     print("-=-" * 40)

# print(">>>>>>>>>>>>>>> VOLTE SEMPRE <<<<<<<<<<<<<<<<<")

#96 - Faça um programa que tenha uma funcao chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno

# def terreno():
#     print("   Controle de Terrenos   ")
#     print("-" * 30)
#     L: float = float(input("LARGURA (m): "))
#     C: float = float(input("COMPRIMENTO (m): "))
#     area = C * L
#     print(f'A área de um terreno {L} x {C} é de {area}m².')

# terreno()

#97 - Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# def escreva(texto):
#     print("~" * len(texto))
#     print(texto)
#     print("~" * len(texto))

# texto: str = str(input("Digite sua frase: "))
# escreva(texto)

#98 - Faça um programa que tenha uma função chamada contador(), que receba três parâmetros, início, fim e passo e realiza a contagem.
# Seu programa tem que realizar três contagens através da função criada.
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

# from time import sleep

# def contador(i, f, p):
#     if p < 0:
#         p *= -1
#     if p == 0:
#         p = 1
#     print(f'Contagem de {i} até {f} de {p} em {p}')
#     sleep(0.5)
#     if i < f:
#         cont = i
#         while cont <= f:
#             print(f'{cont} ', end='', flush=True)
#             sleep(0.5)
#             cont += p
#         print("FIM!")
#     else:
#         cont = i
#         while cont >= f:
#             print(f'{cont} ', end='', flush=True)
#             sleep(0.5)
#             cont -= p
#         print("FIM!")


# contador(1, 10, 1)
# contador(10, 0, 2)
# print("~" * 20)
# print("Insira a contagem que deseja ver: ")
# ini: int = int(input("Início: "))
# fim: int = int(input("Fim: "))
# passo: int = int(input("Passo: "))
# contador(ini, fim, passo)

#99 - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# from time import sleep

# def maior(*num):
#     print("-=" * 30)
#     print("Analisando os valores passados...")
#     sleep(0.5)
#     if num:
#         numero: int = max(num)
#     else:
#         numero: int = 0
#     for n in num:
#         print(f'{n}', end=' ')
#     print(f'Foram informados {len(num)} valores ao todo.')
#     print(f'O maior valor informado foi {numero}.')


# maior(2, 9, 4, 5, 7, 1)
# maior(4, 7, 9)
# maior(1, 2)
# maior()

#100 - Faça um programa que tenha uma lista chamada numeros e duas funções. Uma chamada sorteia() e somaPar(). A primeira função vai sortear 5 números e colocar dentro da lista
# e a segunda vai mostrar a soma de todos os valores pares sorteados pela funcao anterior.

# from random import randint

# def sorteia(lista):
#     lista.clear()
#     for n in range(0, 5):
#         lista.append(randint(1, 10))
#     print(f'Números sorteados: {lista}')

# def somaPar(lista):
#     pares = 0
#     for n in lista:
#         if n % 2 == 0:
#             pares += n
#     print(f'A soma dos valores pares é: {pares}')

# numeros = []
# sorteia(numeros)
# somaPar(numeros)

#101 - Crie um programa que tenha uma funcao chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal,
# indicando se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições

# from datetime import datetime

# def voto(m):
#     dataAtual = datetime.today()
#     anoAtual = dataAtual.year
#     idade = anoAtual - m
#     if idade >= 65:
#         print(f'Com {idade} anos: VOTO OPCIONAL!')
#     elif idade >= 18:
#         print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
#     else:
#         print(f'Com {idade} anos: NÃO VOTA!')
#     return m


# print("--" * 20)
# ano = int(input("Em que ano você nasceu? "))
# voto(ano)

#102 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros. O primeiro que indique o número  a calcular e o outro chamado show, que será
# um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo fatorial.

# def fatorial(n, opcional=False):
#     """-> Calcula o fatorial de um número

#     Args:
#         n (int): O número a ser calculado
#         opcional (bool, optional): Mostrar ou não a conta. Defaults to False.

#     Returns:
#         int: O valor do fatorial de um número n
#     """
#     fat = 1
#     if opcional:
#         print(f'Fatorial de {n}: ', end='')

#     for i in range(n, 0, -1):
#         fat *= i
#         if opcional:
#             print(f'{i}', end='')
#             if i > 1:
#                 print(' x ', end='')
#             else:
#                 print(' = ', end='')
                
#     return fat

# numero = int(input("Deseja ver o fatorial de qual número? "))
# mostra = str(input("Deseja ver a conta? [S/N] ")).strip().upper()[0]
# if mostra == 'S':
#     mostra = True
# else:
#     mostra = False

# resultado = fatorial(numero, mostra)
# print(resultado)


#103 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente.

# def ficha(nome='<desconhecido>',gols=0):
#     """-> Retorna as informações do campeonato

#     Args:
#         nome (str, optional): Nome do jogador informado. Defaults to '<desconhecido>'.
#         gols (int, optional): Quantidade de gols feitos. Defaults to 0.
#     """
#     print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


# n = str(input("Nome do jogador: "))
# if n.strip() == '':
#     n = "<desconhecido>"
# g = str(input("Número de Gols: "))
# if g.isnumeric():
#     g = int(g)
# else:
#     g = 0
# ficha(n, g)
        

#104 - Crie um programa que tenha uma função leiaInt(), que vai funcionar de forma semelhante à função input() do python, só que fazendo a validação
# para aceitar apenas um valor numérico

# def leiaInt(msg):
#     while True:
#         n = input(msg)
#         if not n.isnumeric():
#             print("ERRO! Digite um número válido.")
#         else:
#             return int(n)


# n = leiaInt('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')

#105 - Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)
# adicione também as docstrings da função

# def notas(*n, situacao=False):
#     """Função para analisar notas e situações de respectivos alunos

#     Args:
#         n (float): Uma ou mais notas informadas
#         situacao (bool, optional): Valor opcional, indicando se deve ou não mostrar a situação. Defaults to False.

#     Returns:
#         _type_: Dicionário com várias informações sobre a situação da turma
#     """
#     dicionario = {}
#     dicionario['Total'] = len(n)
#     dicionario['Notas'] = n
#     dicionario['Maior'] = max(n)
#     dicionario['Menor'] = min(n)
#     dicionario['Média'] = sum(n) / len(n)

#     if situacao:
#         media = dicionario['Média']
#         if media >= 7.0:
#             dicionario['Situação'] = "BOA"
#         elif media >= 5.0:
#             dicionario['Situação'] = "RAZOÁVEL"
#         else:
#             dicionario['Situação'] = "RUIM"

#     return dicionario

# resp = notas(5.5, 2.5, 1.5, situacao=False)
# print(resp)

#106 - Faça um mini sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra "FIM" o programa se encerrará.

# def ajuda():
#     while True:
#         verificador = input("Função ou biblioteca? ").strip().lower()
#         if verificador == "fim":
#             break
#         help(verificador)

# ajuda()

#107 - Crie um módulo chamado moeda.py que tenha funções incorporadas: aumentar(), diminuir(), dobro() e metade(). Faça um programa que importe esse módulo
# e use todas as funções.

# from pacotes.moeda import moeda

# preco = float(input("Digite o preço: R$ "))
# print(f'A metade de R${preco:.2f} é {moeda.metade(preco)}')
# print(f'O dobro de R${preco:.2f} é {moeda.dobro(preco)}')


# while True:
#     decisao = input("Deseja reduzir ou aumentar o salário? [R/A] ").strip().upper()
#     if decisao == "A":
#         aumentar = float(input("Digite o percentual de reajuste: "))
#         print(f'Aumentando em {aumentar}%, temos {moeda.aumenta(preco, aumentar)}')
#         break
#     elif decisao == "R":
#         reduz = float(input("Digite o percentual de redução: "))
#         print(f'Reduzindo {reduz}%, temos {moeda.diminuir(preco, reduz)}')
#         break
#     else:
#         print("Opção inválida. Digite apenas R ou A.")

#108 - Adapte o código da versão 107, criando uma função adicional chamada moeda que consiga mostrar os valores como um valor monetário formatado.

# from pacotes.moeda import moeda

# preco = float(input("Digite o preço: R$ "))
# print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
# print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')

#109 - modifique as funcoes que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não
# formatado pela função moeda() desenvolvida no 108.

# feito - Inseridos a opção True or False.

#110 - adicione ao modulo moeda() criado uma funcao chamada resumo(), que mostre na tela algumas informações geradas pela funcoes que já temos no módulo criado

# from pacotes.moeda import moeda

# preco = float(input("Digite o preço: R$ "))
# moeda.resumo(preco)

#111 - Crie um pacote chamado utilidadesCev que tenha dois módulos internos chamados moeda e dados. Transfira tudo para o primeiro pacote e mantenha tudo funcionando
# OBS: acabou que esse eu fiz no início. Criei toda a estrutura e realizei o commit no github

# feito

#112 - Crie uma funcao dentro do módulo dado criado no 111 e insira uma funcao chamada leiaDinheiro() que seja capaz de funcionar como a funcao input(),
# mas com validacao de dados para aceitar somente valores que sejam monetários.

#113 - Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie a função leiaFloat()
# com a mesma finalidade.

# def leiaInt(msg):
#     while True:
#         try:
#             n = int(input(msg))
#         except (ValueError, TypeError):
#             print("ERRO: por favor, digite um número inteiro válido")
#             continue
#         except KeyboardInterrupt:
#             print("Entrada de dados interrompida pelo usuário")
#             return 0
#         else:
#             return n

# def leiaFloat(mensagem):
#     while True:
#         try:
#             n = float(input(mensagem))
#         except (ValueError, TypeError):
#             print("ERRO: por favor, digite um número real válido")
#             continue
#         except KeyboardInterrupt:
#             print("Entrada de dados interrompida pelo usuário")
#             return 0
#         else:
#             return n


# n = leiaInt('Digite um número: ')
# m = leiaFloat('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')
# print(f'Você acabou de digitar o número {m}')

#114 - Crie um código em python que teste se o site Pudim está acessível pelo computador usado.

import requests

def verificar_acesso():
    url = 'http://www.pudim.com.br'
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        print('O site Pudim {url} está acessível!')
    except requests.exceptions.RequestException:
        print('O site Pudim {url} não está acessível.')


if __name__ == "__main__":
    verificar_acesso()

#115 - Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# o sistema vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas.

