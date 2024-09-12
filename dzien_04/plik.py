from pathlib import Path


def wczytaj_linie(nazwa_pliku, enc="utf-8"):
    """Wczytuje listę linii z pliku do listy stringów"""
    return [
        linia.strip() for linia in open(nazwa_pliku, "r", encoding=enc) if linia.strip()
    ]


def podziel_linie(linie_z_pliku, sep=";"):
    """Dzieli listę stringów na listę krotek, podział z 'sep'"""
    return [tuple(linia.split(sep)) for linia in linie_z_pliku]


def wczytaj(nazwa_pliku, enc="utf-8", sep=";"):
    """Funkcja wczytuje do listy krotek dane z pliku.

    Args:
        nazwa_pliku (str): ścieżka do pliku
        enc (str, optional): encoding pliku, domyślnie "utf-8".
        sep (str, optional): separator rozdzielający krotki w ramach linii, domyślnie ";".

    Raises:
        FileNotFoundError: jeśli nazwa_pliku nie jest plikiem lub nie istnieje

    Returns:
        _type_: lista krotek
    """
    # sprawdź czy plik istnieje
    if not Path(nazwa_pliku).is_file():
        raise FileNotFoundError

    linie_z_pliku = wczytaj_linie(nazwa_pliku, enc)
    lista_podzielona = podziel_linie(linie_z_pliku, sep)

    return lista_podzielona


print(wczytaj("dane.csv"))
