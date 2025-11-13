'''Implemente um gerador de progressões aritméticas e geométricas usando range de forma criativa.'''

def aritmetica (inicio, fim, passo):
    ari = list (range (inicio, fim, passo))
    if len(ari) == 0:
        print ("A progressão aritmética está vazia")
        return None
    return ari

def geometrica (inicial, razao, taman):
    geo = []
    for i in range(taman):
        atual = inicial * (razao ** i)
        geo.append(atual)
    return geo
    
teste = aritmetica(0, 49, 5)
teste2 = geometrica (1, 3, 49)
print (f"progressão aritmética: {teste} \nprogressão geométrica: {teste2}")