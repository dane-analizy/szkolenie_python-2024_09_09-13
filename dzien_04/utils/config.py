import yaml


def load_config(nazwa_pliku):
    with open(nazwa_pliku, "r", encoding="utf-8") as plik:
        config = yaml.safe_load(plik)

    return config
