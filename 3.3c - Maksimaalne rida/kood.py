def fail_listiks(failinimi):
    fail = open(failinimi, encoding="UTF-8")

    arvude_tabel = []

    for rida in fail:
        tabel = []
        poolik_tabel = rida.split()
        for arv in poolik_tabel:
            tabel.append(int(arv))

        arvude_tabel.append(tabel)
    
    return arvude_tabel

    fail.close()

failinimi = input('Sisesta failinimi: ')

tabel = fail_listiks(failinimi)

suurim_summa = 0

for rida in tabel:
    if sum(rida) > suurim_summa:
        suurim_summa = sum(rida)

for rea_number, rida in enumerate(tabel, 1):
    jada = []
    jada.append(rea_number)
    jada.append(rida)
    for i in jada:
        if sum(jada[1]) == suurim_summa:
            suurima_summaga_rida = jada[0]

print('Suurim summa on failis', str(suurima_summaga_rida) + '. real ja see on', suurim_summa)