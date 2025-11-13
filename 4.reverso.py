'''Crie um sistema de indexação reversa usando range para processar dados em diferentes direções.'''

def normal (lista):
    fim = len(lista)
    for i in range (0, fim, 1):
        print (f"{lista[i]}\n")

def reverso (lista):
    inicio = len(lista) - 1
    for i in range(inicio, -1, -1):
        print (f"{lista[i]}\n")

poke = ["Altaria", "Appletun", "Applin", "Barbaracle", "Camerupt", "Clefable", "Drampa", "Eevee", "Fletchling", "Florges", "Furfrou", "Garchomp", "Gardevoir", "Gengar", "Primarina", "Scatterbug", "Serperior", "Starmie", "Sylveon", "Taillow", "Vivillon"]
while True:
    dec = str(input ("Digite 1 para ver a lista de pokémons em ordem alfabética; Digite 2 para ver a lista na ordem inversa; Digite 0 para sair: "))
    if (dec == "1"):
        normal (poke)
        continue
    elif (dec == "2"):
        reverso (poke)
        continue
    elif (dec == "0"):
        break
    else:
        print ("Decisão inválida, digite novamente!")
        continue
