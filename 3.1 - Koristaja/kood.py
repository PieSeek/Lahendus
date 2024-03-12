# 3.1 - Koristaja

fail = open("3.1 - Koristaja/toad.txt", encoding="UTF-8")

tubade_tabel = []

for rida in fail:                           # iga rea jaoks failist
    korruse_toad = []                       # kogume ühe korruse tubasid
    osad = rida.split()                     # tühikute kohalt osadeks

    for osa in osad:                        # osade kaupa
        korruse_toad.append(int(osa))       # järjekordne tuba juurde

    tubade_tabel.append(korruse_toad)       # korruse tubade järjend juurde

fail.close()

for korrus, tuba in enumerate(tubade_tabel, 1):
    if korrus % 2 == 0:
        for i in tuba:
            if i % 2 == 0:
                print(i)
    