'''Implemente um algoritmo de ordenação otimizado usando range.'''

def ordenar (lista):
    ordem = len(lista)
    for i in range (0, ordem):
        num = lista[i]
        esp = i
        while (esp > 0 and lista[esp - 1] > num):
            lista[esp] = lista[esp - 1]
            esp = esp - 1
        lista[esp] = num
    return lista

numeros = []
while True:
    nume = int (input ("Insira um número para adicionar na lista: "))
    if (nume == 0):
        print (f"Essa é a lista digitada: {numeros}")
        print (f"Essa é a lista ordenada: {ordenar(numeros)}")
        break
    else:
        numeros.append(nume)
        print (f"Essa é a lista digitada: {numeros} \nCaso não queira adicionar mais nada, escreva sair")