def metade(valor = 0, formatacao = False):
    i = valor / 2
    return i if formatacao is False else moeda(i)

def dobro(valor = 0, formatacao = False):
    h = valor * 2
    return h if formatacao is False else moeda(h)

def aumenta(valor = 0, percentual = 0, formatacao = False):
    s = valor + (valor * percentual / 100)
    return s if formatacao is False else moeda(s)

def diminuir(valor = 0, percentual = 0, formatacao = False):
    d = valor - (valor * percentual / 100)
    return d if formatacao is False else moeda(d)

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')

def resumo(valor = 0):
    print("-" * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print("-" * 40)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Aumento de 10%: \t{aumenta(valor, 10, True)}')
    print(f'Redução de 13%: \t{diminuir(valor, 13, True)}')
    print("-" * 40)