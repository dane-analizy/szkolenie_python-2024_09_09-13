def wczytaj(nazwa_pliku, enc="utf-8", sep=";"):
    lista_plik = [
        tuple(linia.strip().split(sep))
        for linia in open(nazwa_pliku, "r", encoding=enc)
        if linia.strip()
    ]

    return lista_plik


print(wczytaj("dane.csv"))
