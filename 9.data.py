'''Crie um sistema de calendário que use range para gerar datas.'''

def calendario (anoinicio, anofim):
    for a in range (anoinicio, anofim + 1):
        for m in range (0, 13):
            for d in range (0, 31):
                print (f"{a} / {m} / {d}")

ini = int (input ("Digite o ano de inicío: "))
fim = int (input ("Digite o último ano: "))
calendario (ini, fim)