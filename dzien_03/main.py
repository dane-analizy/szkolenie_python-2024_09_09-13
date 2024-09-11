# # zip() -> iteracja przez dwie listy, kończy zwracanie elementów jak skończy się najkrótsza lista!

# l1 = [1, 2, 3, 4, 5] # 5 cyfr
# l2 = [literka for literka in "abcdefghij"] # 10 znaków

# print("zip():")
# for el1, el2 in zip(l1, l2):
#     print(el1, el2)

# # zip_longest -> idziemy przez wiele list, dopóki nie skończy się najdłuższa
# from itertools import zip_longest

# print("zip_longest():")
# for el1, el2 in zip_longest(l1, l2):
#     print(el1, el2)


# # cykl
# from itertools import cycle

# print("cycle():")
# for n, el1 in enumerate(cycle(l1)):
#     print(n, el1)
#     if n >= 100:
#         break


# # uczniowie kolejno odlicz do dwóch :)
# print("cycle() i zip()")
# for el1, el2 in zip(l2, cycle([1, 2])):
#     print(el1, el2)


# iloczyn wielu list
# from itertools import product

# l1 = [1, 2, 3, 4, 5]
# l2 = ["a", "b", "c"]
# l3 = ["Jan", "Marysia", "Basia", "Zdzisław"]
# print(list(product(l1, l2, l3)))


## SŁOWNIKI

# klucz : wartość

# d = dict()
# d = {
#     "imie": "Jan",
#     "nazwisko": "Nowak",
#     "wiek": 35,
#     "wzrost": 180,
#     "waga": 80.5,
#     "imiona_dzieci": ["Staś", "Halinka", "Józio"],
# }
# print(d)


os1 = {
    "imie": "Jan",
    "nazwisko": "Nowak",
    "wiek": 35,
    "wzrost": 180,
    "waga": 80.5,
    "imiona_dzieci": ["Staś", "Halinka", "Józio"],
}
os2 = {
    "imie": "Adam",
    "nazwisko": "Kowalski",
    "wiek": 10,
}

# print(os1, os2)
# ludzie = [ os1, os2] # lista osób

# klucze muszą być unikalne - tu się nadpiszą
# ludzie = {"osoba": os1,
#           "osoba": os2}
# print(ludzie)

rodzina = {
    "ojciec": os1,
    "syn": os2,
    "matka": {
        "imie": "Anna",
        "nazwisko": "Kowalska",
        "wiek": 33,
        "samochody": ["Ford", "Opel", "Audi"],
    },
    "miasto": "Kraków",
}

# print(rodzina)

# klucze - lista
# print(rodzina.keys())

# wartości
# print(rodzina.values())

# iteracja po słowniku =- klucz i wartość jednocześnie
# for k,v in rodzina.items():
#     print(f"Klucz: {k}\nWartość: {v}\n")

# pogoda = {
#     "2024-09-05": {"temp": 17, "cisnienie": 1023, "opad": 0},
#     "2024-09-06": {"temp": 21, "cisnienie": 1023, "opad": 0},
#     "2024-09-07": {"temp": 19, "cisnienie": 1023, "opad": 0},
#     "2024-09-08": {"temp": 20, "cisnienie": 1023, "opad": 0},
#     "2024-09-09": {"temp": 22, "cisnienie": 1023, "opad": 0},
# }

# # zmiana wartości w słowniku
# pogoda["2024-09-09"]["temp"] = 19

# # dodanie nowego elementu  (== pod nowym kluczem) do słownika
# pogoda["2024-09-10"] = {"temp": 25, "cisnienie": 1023, "opad": 50}


# # wypisać wszystkie dni kiedy było > 20 stopni
# for k,v in pogoda.items():
#     if v["temp"] > 20:
#         print(k)


# d = {
#     "a": 1,
#     "b": 2
# }

# # print(d["c"]) # -> KeyError, nie ma takiego klucza
# print(d.get("c", "brak tego czego oczekujesz")) # nie ma klucza, zwracamy wartość domyślną
# print("koniec programu")


# d = {}
# d = {"klucz": "wartosc"}

# klucze = ("a", "b", "c", "a")
# wartosci = [1, 2, 3, 5]
# d = {}
# for klucz, wartosc in zip(klucze, wartosci):
#     d[klucz] = wartosc

# print(d)


### ZADANIE

# Utwórz plik konfiguracja.txt, który będzie konfiguracją w postaci "klucz=wartość".
# Wczytaj konfigurację do słownika. Wypisz cały słownik
#
# {
# "login": "lukasz",
# "haslo": "wiosna2024",
# "numertelefonu": "123456789",
# }

# rozwiazanie 1
# s1 = dict()

# for linia in open("konfiguracja.txt", "r", encoding="utf-8"):
#     linia_czysta = linia.strip()
#     if len(linia_czysta) == 0:
#         continue
#     linia_czysta = linia_czysta.split("=")
#     s1[linia_czysta[0]] = linia_czysta[1]

# print(s1)


# rozwiązanie 2 - dict comprehension

# s1 = {
#     linia.strip().split("=")[0]: "=".join(linia.strip().split("=")[1:])
#     # linia.strip().split("=")[0]: linia.strip().split("=")[1:]
#     for linia in open("konfiguracja.txt", "r", encoding="utf-8")
#     if linia.strip()
# }

# print(s1)


# pip install pandas openpyxl
# import pandas as pd

# dane_xls = pd.read_excel("pogoda.xlsx")
# print(dane_xls)

# print(dane_xls[dane_xls['temp'] > 20])

# dane_dict = {}
# for r in dane_xls.itertuples():
#     # print(r, r.data)
#     dane_dict[str(r.data.date())] = {"temp": r.temp, "cisnienie": r.cisnienie, "opad": r.opad}

# print(dane_dict)

# print(dane_dict['2024-09-08'])

# dane_dzienne = {
#     (2024, 9, 9): {...},
#     (2024, 9, 10): {...},
# }

# for y in [2022, 2023, 2024]:
#     for m in range(1, 13):
#         for d in range(1, 31):
#             print(dane_dzienne.get((y, m, d)))


#### ZADANIE

# Wczytaj z pliku data.csv dane o zawodnikach. Policz dla nich BMI.
# Każdego zawodnika "ubierz" w strukturę typu słownik, z odpowiednimi kluczami
# (imie, nazwisko, wzrost, waga, bmi) o odpowiednich typów.
# Zbuduj listę zawodników z tych struktur.

# # wczytanie pliku do listy list - dość uniwersalnie
# sep = ";"
# nazwa_pliku = "dane.csv"
# enc = "utf-8"
# lista_plik = [
#     linia.strip().split(sep)
#     for linia in open(nazwa_pliku, "r", encoding=enc)
#     if linia.strip()
# ]

# # logika biznesowa
# lista_zawodnikow = []
# for linia in lista_plik:
#     linia[2] = float(linia[2])
#     linia[3] = float(linia[3])
#     bmi = linia[3] / (linia[2] / 100) ** 2
#     lista_zawodnikow.append(
#         {
#             "imie": linia[0],
#             "nazwisko": linia[1],
#             "wzrost": linia[2],
#             "waga": linia[3],
#             "bmi": bmi,
#         }
#     )

# # wyświetlenie wyniku
# print(lista_zawodnikow)


# # extras - zapisanie listy słowników do Excela za pomocą pandas
# import pandas as pd

# df = pd.DataFrame(lista_zawodnikow)
# print(df)
# df.to_excel("zawodnicy_z_bmi.xlsx", index=False)


# zapisywanie plików

# # wczytanie pliku do listy list - dość uniwersalnie
# sep = ";"
# nazwa_pliku = "dane.csv"
# enc = "utf-8"
# lista_plik = [
#     linia.strip().split(sep)
#     for linia in open(nazwa_pliku, "r", encoding=enc)
#     if linia.strip()
# ]


# print(lista_plik)

# wczytanie pliku z context-managerem with...as...:
# sep = ";"
# nazwa_pliku = "dane.csv"
# enc = "utf-8"
# with open(nazwa_pliku, "r", encoding=enc) as plik:
#     lista_plik = [
#         linia.strip().split(sep)
#         for linia in plik
#         if linia.strip()
#     ]

# print(lista_plik)


# zapisanie listy do pliku
# nazwa_pliku_zapis = "dane_zapisane.csv"
# with open(nazwa_pliku_zapis, "w", encoding=enc) as plik:
#     for rekord in lista_plik:
#         linia_do_zapisania = sep.join(rekord) + "\n"
#         plik.write(linia_do_zapisania)


#### ZADANIE

# Korzystając z danych z poprzedniego zadania (lista obiektów "zawodnik") utwórz plik
# "zawodnicy_bmi.csv", który będzie zawierał informacje o zawodnikach razem z ich BMI.

# # wczytanie pliku do listy list - dość uniwersalnie
# sep = ";"
# nazwa_pliku = "dane.csv"
# enc = "utf-8"
# lista_plik = [
#     linia.strip().split(sep)
#     for linia in open(nazwa_pliku, "r", encoding=enc)
#     if linia.strip()
# ]

# # logika biznesowa
# lista_zawodnikow = []
# for linia in lista_plik:
#     linia[2] = float(linia[2])
#     linia[3] = float(linia[3])
#     bmi = linia[3] / (linia[2] / 100) ** 2
#     lista_zawodnikow.append(
#         {
#             "imie": linia[0],
#             "nazwisko": linia[1],
#             "wzrost": linia[2],
#             "waga": linia[3],
#             "bmi": bmi,
#         }
#     )


# lista_zawodnikow.append(
#     {
#         "wzrost": 175,
#         "imie": "Henio",
#         "waga": 87,
#         "nazwisko": "Iksiński",
#     }
# )


# # zapisanie do pliku
# nazwa_pliku_zapis = "dane_zapisane.csv"
# with open(nazwa_pliku_zapis, "w", encoding=enc) as plik:
#     for rekord in lista_zawodnikow:
#         # wartosci = [str(w) for w in rekord.values()]
#         # linia_do_zapisania = sep.join(wartosci) + "\n"
#         linia_do_zapisania = f'{rekord.get("imie", "")};{rekord.get("nazwisko", "")};{rekord.get("wzrost", "")};{rekord.get("waga", "")};{rekord.get("bmi", "")}\n'
#         plik.write(linia_do_zapisania)


# sortowanie słowników
# d = {
#     "Jan": 180,
#     "Adam": 190,
#     "Krzysztof": 195,
#     "Zdzisław": 160,
#     "Henio": 175,
#     # "Dobromir": [1,2]
# }

# # sortowanie po kluczu
# d_k = sorted(d.items(), key=lambda kv: kv[0], reverse=True)
# print(d_k)


# # sortowanie po wartości
# d_k = sorted(d.items(), key=lambda kv: kv[1])
# print(d_k)