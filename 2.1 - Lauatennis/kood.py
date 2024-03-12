# 2.1 - Lauatennis

fail = open("2.1 - Lauatennis/tulemused.txt", encoding="UTF-8")

tulemuste_tabel = []

for rida in fail:                           # iga rea jaoks failist
    seti_punktid = []                       # kogume ühe seti punkte
    osad = rida.split()                     # tühikute kohalt osadeks

    for osa in osad:                        # osade kaupa
        seti_punktid.append(int(osa))       # järjekordsed punktid juurde

    tulemuste_tabel.append(seti_punktid)    # seti punktide järjend juurde

fail.close()

eesti_punktid = 0
soome_punktid = 0

for mäng in tulemuste_tabel:
    if mäng[0] > mäng[1]:
        eesti_punktid += 1
    elif mäng[0] < mäng[1]:
        soome_punktid += 1

if eesti_punktid > soome_punktid:
    print('Eesti võitis ' + str(eesti_punktid) + '-' + str(soome_punktid))
elif eesti_punktid < soome_punktid:
    print('Soome võitis ' + str(soome_punktid) + '-' + str(eesti_punktid))