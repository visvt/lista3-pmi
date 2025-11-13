'''Crie uma função que gere uma sequência personalizada usando range com diferentes parâmetros e calcule estatísticas.'''

def estatistica (inicio, fim, passo):
    print (f"Gerando lista com range {inicio}, {fim}, {passo}")
    lista = list (range (inicio, fim, passo))
    if len(lista) == 0:
        print ("A lista gerada está vazia")
        return None
    print (f"Lista gerada: {lista}")
    soma = sum (lista)
    contagem = len (lista)
    media = soma / contagem
    print (f"Soma dos valores: {soma}")
    print (f"Quantidade de números: {contagem}")
    return media

calculam = estatistica (0, 49, 5)
if calculam is not None:
    print (f"A media é: {calculam}")

