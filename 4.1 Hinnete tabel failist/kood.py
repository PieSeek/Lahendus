import csv

fail = open("4.1 Hinnete tabel failist/hinded.csv", encoding="UTF-8")
loetudFail = csv.reader(fail, delimiter=',')

hinnete_tabel = []

for rida in loetudFail:
    hinnete_tabel.append(rida)

fail.close()


for rida in hinnete_tabel:
    hinded = []
    aine = rida[0]
    rida.pop(0)
    for hinne in rida:
        hinded.append(int(hinne))
    print(aine + ':', str(round(sum(hinded) / len(hinded), 1)))