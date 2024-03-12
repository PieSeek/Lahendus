fail = open("4.1 Hinnete tabel failist/hinded.csv", encoding="UTF-8")

hinnete_tabel = []

for rida in fail:
    for hinne in rida:
        hinnete_tabel.append(hinne)
        

fail.close()

print(hinnete_tabel)