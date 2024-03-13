import csv

fail = open("4.2b Programmeerimisest maalähedaselt/maalähedane.csv", encoding="UTF-8")
loetudFail = csv.reader(fail, delimiter=';')

osalejate_tabel = []

for rida in loetudFail:
    osalejate_tabel.append(rida)

fail.close()

tabel = []
maakonnad = []

suurimSumma = 0
suurimaSummagaMaakond = None

arvutusTabel = []
maakonnaTabel = []

for rida3 in osalejate_tabel:
    arvutusTabel.append(rida3)
    maakonnaTabel.append(rida3)

summa = 0

for rida1 in arvutusTabel:
    arvutusRida = rida1
    arvutusRida.pop(0)

    tabel1 = []

    for number in arvutusRida:
        tabel1.append(int(number))
    tabel.append(tabel1)

    summa += sum(tabel1)
    if sum(tabel1) > suurimSumma:
        suurimSumma = sum(tabel1)
    
    tabel2 = []

    maakonnaTabel.pop(0)
    for rida4 in maakonnaTabel:

        tabel2.append(int(rida4))


print('Kõige rohkem osalejaid -', str(suurimaSummagaMaakond) + ',', suurimSumma, 'inimest.' )
print('Kokku on kursusel osalenud', summa, 'inimest.')