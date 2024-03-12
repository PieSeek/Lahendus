def keskmised(hinnete_tabel):
    väljund = []
    for rida in hinnete_tabel:
        aine = rida[0]
        rida.pop(0)
        keskmine = round(sum(rida) / len(rida), 1)
        tulemus = [aine, keskmine]
        väljund.append(tulemus)
    return väljund

print(keskmised([   ['eesti keel', 5, 4, 3, 4, 4, 3, 4, 4],
                    ['matemaatika', 4, 4, 5, 5, 4, 5, 5, 4, 5],
                    ['keemia', 4, 3, 3, 2, 3, 4]]))