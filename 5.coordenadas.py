'''Implemente um gerador de coordenadas para grade 2D usando range aninhado.'''

def grade (larg, alt):
    fimx = larg
    fimy = alt
    for y in range (fimy):
        for x in range (fimx):
            print (f"As coordenadas são: ({x}, {y})")

while True:
    try:
        xlar = int (input("Insira o valor de X: "))
        yalt = int (input("Insira o valor de Y: "))
        grade(xlar, yalt)
        break
    except ValueError:
        print ("Insira somente números!")
        continue