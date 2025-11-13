'''Desenvolva um sistema de paginação usando range para dividir listas grandes.'''

def paginas (lista):
    tampag = 10
    fim = len(lista)
    ind = 1
    for i in range (0, fim, tampag):
        pag = lista[i : i+tampag]
        print (f"Página {ind}: {pag}")
        ind = ind + 1

poke = ["Florges", "Clefable", "Primarina", "Altaria", "Camerupt", "Sylveon", "Gardevoir", "Serperior", "Garchomp", "Gengar", "Starmie", "Eevee", "Drampa", "Applin", "Appletun", "Furfrou", "Vivillon", "Scatterbug", "Fletchling", "Taillow", "Barbaracle"]
while True:
    item = (input ("Digite o nome do pokémon! (Caso queira sair, digite 0): "))
    if (item == "0"):
        break
    else:
        poke.append(item)
        continue
paginas(poke)
