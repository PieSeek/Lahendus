# 2.2 - Kalorsus 

fail = open("2.2 - Kalorsus/kalorid.txt", encoding="UTF-8")

toitude_tabel = []

for rida in fail:                           # iga rea jaoks failist
    korra_grammid = []                      # kogume ühe toidukorra info
    osad = rida.split()                     # tühikute kohalt osadeks

    for osa in osad:                        # osade kaupa
        korra_grammid.append(int(osa))      # järjekordne info juurde

    toitude_tabel.append(korra_grammid)     # toidukorra järjend juurde

fail.close()

kalorid_kokku = 0

for toidukord in toitude_tabel:
    kalorid_kokku =  toidukord[0] * 4 + kalorid_kokku         # süsivesikud
    kalorid_kokku =  toidukord[1] * 4 + kalorid_kokku         # valgud
    kalorid_kokku =  toidukord[2] * 9 + kalorid_kokku         # rasvad

print(kalorid_kokku)