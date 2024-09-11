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


# jak długo trwa wykonywanie programu?
# import time
# import statistics

# lista_czasow = []
# for _ in range(100):
#     # liczba sekund od chwili 1970-01-01 00:00:00
#     start = time.perf_counter()
#     # wstrzymanie programu na 0.1 sekundy
#     time.sleep(.1)
#     end = time.perf_counter()
#     lista_czasow.append(end-start)

# print(statistics.mean(lista_czasow))
# print(statistics.stdev(lista_czasow))


### ZADANIE

# Policz ile razy występują poszczególne słowa w tekście "Pana Tadeusza".
# Użyj słowników - kluczem niech będzie słowo zapisane małymi literami,
# a wartością - liczba jego wystąpień.


# rozwiązanie 1
# import time

# # wczytanie całego pliku do jednej zmiennej typu string
# tresc = open("tadzio.txt", "r", encoding="utf-8").read()
# tresc = tresc.lower()

# # znaki do usunięcia
# zle_znaki = ",./?!()-—;:\"'/\\…\n\t*+«»<>"

# # oczyszczenie tekstu
# for znak in zle_znaki:
#     tresc = tresc.replace(znak, " ")

# slowa = tresc.split(" ")

# licznik_slow = {}
# start_time = time.perf_counter()

# for slowo in slowa:
#     # puste słowa omijamy
#     if not slowo:
#         continue

#     # pomijamy słowa krótsze niż 4 znaki
#     if len(slowo) <= 4:
#         continue

#     # można sprawdzać czy słowo jest na liście tzw. stop-words https://github.com/bieli/stopwords/blob/master/polish.stopwords.txt

#     # zwiększamy licznik wystąpień dla słowa o 1 jeśli istniał
#     if slowo in licznik_slow.keys():
#         licznik_slow[slowo] = licznik_slow[slowo] + 1
#     else:
#         # licznik nie istniał - "tworzymy" nowy dla nowego słowa
#         licznik_slow[slowo] = 1

# print(time.perf_counter()-start_time)

# # ile razy występuje "tadeusz"
# print(licznik_slow['tadeusz'])

# # jakie słowa i ile razy występują zaczynają się od "tadeusz"?
# for k,v in licznik_slow.items():
#     if k.startswith("tadeusz"):
#         print(k,v)

# # najpopularniejsze słowa
# licznik_slow = sorted(licznik_slow.items(), key=lambda kv: kv[1])
# print(licznik_slow)


# rozwiązanie 2

# # wczytanie całego pliku do jednej zmiennej typu string
# tresc = open("tadzio.txt", "r", encoding="utf-8").read()
# tresc = tresc.lower()

# # znaki do usunięcia
# zle_znaki = ",./?!()-—;:\"'/\\…\n\t*+«»<>"

# # oczyszczenie tekstu
# for znak in zle_znaki:
#     tresc = tresc.replace(znak, " ")

# slowa = tresc.split(" ")


# licznik_slow = {}
# for slowo in slowa:
#     # pomijamy słowa krótsze niż 4 znaki
#     if len(slowo) <= 4:
#         continue

#     # zwiększamy licznik wystąpień dla słowa o 1 jeśli istniał
#     licznik_slow[slowo] = licznik_slow.get(slowo, 0) + 1

# # najpopularniejsze słowa
# licznik_slow = sorted(licznik_slow.items(), key=lambda kv: kv[1])
# print(licznik_slow)


# rozwiązanie 3

# from collections import defaultdict


# # wczytanie całego pliku do jednej zmiennej typu string
# tresc = open("tadzio.txt", "r", encoding="utf-8").read()
# tresc = tresc.lower()

# # znaki do usunięcia
# zle_znaki = ",./?!()-—;:\"'/\\…\n\t*+«»<>"

# # oczyszczenie tekstu
# for znak in zle_znaki:
#     tresc = tresc.replace(znak, " ")

# slowa = tresc.split(" ")


# # słownik, który zwróci wartość 0 dla kluczy które nie istnieją
# licznik_slow = defaultdict(lambda: 0)

# for slowo in slowa:
#     # pomijamy słowa krótsze niż 4 znaki
#     if len(slowo) <= 4:
#         continue

#     # zwiększamy licznik wystąpień dla słowa o 1 jeśli istniał
#     licznik_slow[slowo] = licznik_slow[slowo] + 1

# # najpopularniejsze słowa
# licznik_slow = sorted(licznik_slow.items(), key=lambda kv: kv[1])
# print(licznik_slow)


# rozwiązanie 4

# from collections import Counter
# import time

# # wczytanie całego pliku do jednej zmiennej typu string
# tresc = open("tadzio.txt", "r", encoding="utf-8").read()
# tresc = tresc.lower()

# # znaki do usunięcia
# zle_znaki = ",./?!()-—;:\"'/\\…\n\t*+«»<>"

# # oczyszczenie tekstu
# for znak in zle_znaki:
#     tresc = tresc.replace(znak, " ")

# slowa = tresc.split(" ")


# start_time = time.perf_counter()
# licznik_slow = {k: v for k, v in Counter(slowa).items() if len(k) > 4}
# print(time.perf_counter()-start_time)

# # najpopularniejsze słowa
# licznik_slow = sorted(licznik_slow.items(), key=lambda kv: kv[1])
# # print(licznik_slow)


# from collections import Counter

# lista = [1, 2, 3, 4, 5, 5, 5, 3]
# print(Counter(lista))


# rozwiązanie 5

# import time

# # wczytanie całego pliku do jednej zmiennej typu string
# tresc = open("tadzio.txt", "r", encoding="utf-8").read()
# tresc = tresc.lower()

# # znaki do usunięcia
# zle_znaki = ",./?!()-—;:\"'/\\…\n\t*+«»<>"

# # oczyszczenie tekstu
# for znak in zle_znaki:
#     tresc = tresc.replace(znak, " ")

# slowa = [s for s in tresc.split(" ") if len(s) > 4]
# unikalne_slowa = set(slowa)

# d = {}
# start_time = time.perf_counter()
# for slowo in unikalne_slowa:
#     d[slowo] = tresc.count(slowo)

# print(time.perf_counter() - start_time)


# sztuczne dane - pakiet Faker
# instalacja:
# pip install Faker
# PEP8 - nazwy klas CamelCase

# from faker import Faker

# f = Faker("pl_PL")
# print(f.name())
# print(f.first_name())
# print(f.last_name())
# print(f.company())
# print(f.street_name())
# print(f.city())
# print(f.phone_number())
# print(f.job())
# print(f.email())
# print(f.uuid4())

### ZADANIE

# Korzystając z pakietu Faker wygeneruj plik typu CSV zawierający 10 tysięcy rekordów zawierających:
# id będący kolejną liczbą, imię, nazwisko, nazwa firmy, email, telefon, miasto.


# from faker import Faker

# f = Faker("pl_PL")

# faker_list = []
# for i in range(10_000):
#     faker_list.append(
#         {
#             "firstName": f.first_name(),
#             "lastName": f.last_name(),
#             "firma": f.company(),
#             "email": f.email(),
#             "phone": f.phone_number(),
#         }
#     )

# with open("faker.txt", "w", encoding="utf-8") as file:
#     for rec in faker_list:
#         file.write(
#             rec.get("firstName")
#             + ";"
#             + rec.get("lastName")
#             + ";"
#             + rec.get("firma")
#             + ";"
#             + rec.get("email")
#             + ";"
#             + rec.get("phone")
#             + "\n"
#         )


# pliki json

# import json

# from faker import Faker

# f = Faker("pl_PL")

# faker_list = []
# for i in range(10):
#     faker_list.append(
#         {
#             "id": i,
#             "firstName": f.first_name(),
#             "lastName": f.last_name(),
#             "firma": f.company(),
#             "email": f.email(),
#             "phone": f.phone_number(),
#         }
#     )

# # zapis do jsona w pliku
# with open("ludzie.json", "w", encoding="utf-8") as plik:
#     json.dump(faker_list, plik)

# # zapis do jsona w zmiennej typu string
# json_str = json.dumps(faker_list)
# print(json_str)


# import json

# # wczytanie jsona z pliku
# with open("ludzie.json", "r", encoding="utf-8") as plik:
#     dane = json.load(plik)
    
# # wczytanie ze stringa: json.loads(string)

# print(dane)
# for d in dane:
#     print(d)
#     print(type(d))
# #     break


# import json

# # wczytanie jsona z pliku
# with open("ludek.json", "r", encoding="utf-8") as plik:
#     dane = json.load(plik)

# print(dane)
# print(type(dane))

# # czy wczytane dane są listą czy słownikiem?
# if isinstance(dane, list):
#     print("To jest lista")
# elif isinstance(dane, dict):
#     print("To jest słownik")
# else:
#     print("HGW co to jest")
    
 
# import json

# nbp = [
#     {
#         "table": "A",
#         "no": "177/A/NBP/2024",
#         "effectiveDate": "2024-09-11",
#         "rates": [
#             {"currency": "bat (Tajlandia)", "code": "THB", "mid": 0.1155},
#             {"currency": "dolar amerykański", "code": "USD", "mid": 3.8816},
#             {"currency": "dolar australijski", "code": "AUD", "mid": 2.5847},
#             {"currency": "dolar Hongkongu", "code": "HKD", "mid": 0.4977},
#             {"currency": "dolar kanadyjski", "code": "CAD", "mid": 2.8570},
#             {"currency": "dolar nowozelandzki", "code": "NZD", "mid": 2.3854},
#             {"currency": "dolar singapurski", "code": "SGD", "mid": 2.9804},
#             {"currency": "euro", "code": "EUR", "mid": 4.2864},
#             {"currency": "forint (Węgry)", "code": "HUF", "mid": 0.01081},
#             {"currency": "frank szwajcarski", "code": "CHF", "mid": 4.5900},
#             {"currency": "funt szterling", "code": "GBP", "mid": 5.0778},
#             {"currency": "hrywna (Ukraina)", "code": "UAH", "mid": 0.0943},
#             {"currency": "jen (Japonia)", "code": "JPY", "mid": 0.027422},
#             {"currency": "korona czeska", "code": "CZK", "mid": 0.1709},
#             {"currency": "korona duńska", "code": "DKK", "mid": 0.5744},
#             {"currency": "korona islandzka", "code": "ISK", "mid": 0.028144},
#             {"currency": "korona norweska", "code": "NOK", "mid": 0.3591},
#             {"currency": "korona szwedzka", "code": "SEK", "mid": 0.3752},
#             {"currency": "lej rumuński", "code": "RON", "mid": 0.8617},
#             {"currency": "lew (Bułgaria)", "code": "BGN", "mid": 2.1916},
#             {"currency": "lira turecka", "code": "TRY", "mid": 0.1143},
#             {"currency": "nowy izraelski szekel", "code": "ILS", "mid": 1.0300},
#             {"currency": "peso chilijskie", "code": "CLP", "mid": 0.004089},
#             {"currency": "peso filipińskie", "code": "PHP", "mid": 0.0694},
#             {"currency": "peso meksykańskie", "code": "MXN", "mid": 0.1945},
#             {
#                 "currency": "rand (Republika Południowej Afryki)",
#                 "code": "ZAR",
#                 "mid": 0.2170,
#             },
#             {"currency": "real (Brazylia)", "code": "BRL", "mid": 0.6853},
#             {"currency": "ringgit (Malezja)", "code": "MYR", "mid": 0.8959},
#             {"currency": "rupia indonezyjska", "code": "IDR", "mid": 0.00025205},
#             {"currency": "rupia indyjska", "code": "INR", "mid": 0.046235},
#             {"currency": "won południowokoreański", "code": "KRW", "mid": 0.002897},
#             {"currency": "yuan renminbi (Chiny)", "code": "CNY", "mid": 0.5457},
#             {"currency": "SDR (MFW)", "code": "XDR", "mid": 5.2266},
#         ],
#     }
# ]

# with open("nbp.json", "w") as f:
#     json.dump(nbp, f)