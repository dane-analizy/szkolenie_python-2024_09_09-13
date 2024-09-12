def wczytaj_linie(nazwa_pliku, enc="utf-8"):
    return [
        linia.strip() for linia in open(nazwa_pliku, "r", encoding=enc) if linia.strip()
    ]


def podziel_linie(linie_z_pliku, sep=";"):
    return [tuple(linia.split(sep)) for linia in linie_z_pliku]


def wczytaj(nazwa_pliku, enc="utf-8", sep=";"):
    linie_z_pliku = wczytaj_linie(nazwa_pliku, enc)
    lista_podzielona = podziel_linie(linie_z_pliku, sep)
    return lista_podzielona


print(wczytaj("dane.csv"))
