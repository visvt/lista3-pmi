'''Crie um sistema de cronômetro que use range para contar regressivamente.'''

def cronometro (horas, minutos, segundos):
    segu = (horas * 3600) + (minutos * 60) + segundos
    for h in range(segu, -1, -1):
        hor = h // 3600
        faltseg = h % 3600
        minu = faltseg // 60
        segund = faltseg % 60
        print (f"{hor} : {minu} : {segund}")


hrs = int (input ("Digite a quantidade de horas: "))
mi = int (input ("Digite a quantidade de minutos: "))
seg = int (input ("Digite a quantidade de segundos: "))

cronometro (hrs, mi, seg)
