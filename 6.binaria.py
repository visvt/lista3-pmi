'''Desenvolva um algoritmo de busca binária usando range para otimizar a busca.'''

def busca (palp):
    lista = list(range(0,100))
    num = lista[77]
    while (palp != num):
        if (palp < num):
            print ("Número secreto é maior, tente novamente!")
            return palp
        elif (palp > num):
            print ("Número secreto é menor, tente novamente!")
            return palp
        elif (palp == 0):
            print ("Você acertou")
            break

    nume = int (input ("adivinhe o número: "))
    print (busca (nume))


