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