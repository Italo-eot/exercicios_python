def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO: por favor, digite um número inteiro válido")
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuário")
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'{contador} - {item}')
        contador += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc