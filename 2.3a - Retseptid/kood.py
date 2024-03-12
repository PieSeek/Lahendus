# 2.3a - Retseptid

fail = open("2.3a - Retseptid/retseptid.txt", encoding="UTF-8")

retseptid_tabel = []

for rida in fail:                           # iga rea jaoks failist
    koostisosad = []                        # kogume reas olevad koostisosad järjendisse
    osad = rida.split(",")                  # jupitame rea koma koha pealt

    for osa in osad:                        # vaatame iga juppi eraldi
        koostisosad.append(osa.strip())     # visame reas olevad koostisosad järjendisse

    retseptid_tabel.append(koostisosad)     # lisame koostisosade järjendi retseptide tabelisse

fail.close()

for retsept in retseptid_tabel:
    if 'suhkur' in retsept:
        if 'maasikad' in retsept:
            print(retsept)