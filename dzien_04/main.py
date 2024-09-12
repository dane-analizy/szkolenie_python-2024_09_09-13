# obsługa i typy wyjątków

# lista = [1, 2, 3, 0, "abc", 10, 50]

# for el in lista:
#     print("el: ", el)
#     try:
#         wynik_liczenia = 1/el
#         print("wynik_liczenia: ", wynik_liczenia)
#     except TypeError:
#         print("Błąd typów - nie możesz dodawać stringa do liczby")
#     except ZeroDivisionError:
#         print("Błąd typów - nie możesz dzielić przez zero")
#     except Exception as e:
#         print("nie udało się")
#         print("Wyjątek:", e, type(e))

#     try:
#         wynik_scalania = 1 + str(el)
#         print("wynik_scalania: ", wynik_scalania)
#     except TypeError:
#         print("Błąd typów - nie możesz dodawać stringa do liczby")
#     except ZeroDivisionError:
#         print("Błąd typów - nie możesz dzielić przez zero")
#     except Exception as e:
#         print("nie udało się")
#         print("Wyjątek:", e, type(e))

# print("Program zakończony")


# try:
#     # wczytaj plik
# except:
#     # nie udało się wczytać pliku
#     # kończę program - z błędem 10
#     # exit(10)

# try:
#     # otwórz połączenie z baza danych
# except:
#     # zakończ program
#     # exit(20)


# try:
#     # wsadz dane do bazy danych
#     # zamknij połączenie z bazą
# except:
#     # zamknij połączenie z bazą
#     # zakończ program
#     # exit(30)


# zwracanie wyjątków

# l = [1, 2, 3, 0, 5, 6]

# for el in l:
#     print(el)
#     if el == 0:
#         raise NotImplementedError

# własne typy błędów

# class WlasnyBlad(BaseException):
#     pass

# l = [1, 2, 3, 0, 5, 6]

# for el in l:
#     print(el)
#     if el == 0:
#         raise WlasnyBlad

#     if el == 3:
#         raise NotImplementedError


## ZADANIE

# Plik dane.csv zmodyfikuj tak, aby niektóre wiersze miały mniej niż 4 kolumny.
# Wczytaj plik i podziel każdy wiersz na elementy w tablicy, rozdzielenie jest przez ";"
# Wyświetl 4 element z każdej linii. Jeśli napotkasz błąd - obsłuż go.

# for i, linia in enumerate(open("dane.csv", "r", encoding="utf-8"), start=1):
#     lista_linia = linia.strip().split(";")
#     try:
#         print(lista_linia[3])
# łapiemy błąd zwiazany z brakiem elementu o indeksie = 3
#     except IndexError as e:
#         print(f"Nieodpowiednia struktura w linii {i}")
# łapiemy wszystkie inne potencjalne błędy
#     except Exception as e:
#         print(f"Nieznany błąd: {e}")


## funkcje

# print() <- to jest funkcja


# # funkcja bez parametrów:
# def funkcja():
#     print("Jestem w funkcji 'funkcja'")

# # wywołanie funkcji:
# funkcja()
# funkcja()


# funkcja z parametrami
# def funkcja(a):
#     print(f"Jestem 'funkcja' i podałeś parametr {a=}")
#     b = a + 1
#     print(f"Wynik dodania 1 do Twojego parametru to: {b}")

# funkcja(10)


# funkcja z 2 parametrami:
# def dodawanie(a, b):
#     print(f"Jestem funkcja 'dodawanie' i podałeś parametry {a=}, {b=}")
#     suma = a + b
#     print(f"Wynik dodania to: {suma}")

# dodawanie(10, 56)


# funkcja zwracająca wartości
# def dodawanie(a, b):
#     suma = a + b
#     return suma

# w = dodawanie(10, 56)
# print(w)


# def dodawanie(a: float, b: float) -> float:
#     suma = a + b
#     print(f"Wynik {a} + {b} = {suma}")
#     return suma

# print("wywołanie funkcji", dodawanie(10.0, 52))


### ZADANIE

# Przygotuj funkcję, która wyliczy na podstawie wagi i wzrostu (parametry)
# BMI z dokładnością do 2 miejsc po przecinku. W przypadku pojawienia się wyjątku - wypisze na konsoli
# błąd i zwróci wartość -1


# rozwiazanie 1
# def bmi(waga, wzrost):
#     if not isinstance(waga, (int, float)):
#         print("Waga musi być typu float lub int")
#         return -1
#     if not isinstance(wzrost, (int, float)):
#         print("Wzrost musi być typu float lub int")
#         return -1

#     if (waga < 0) or (wzrost < 0):
#         print("Wzrost i waga nie mogą być mniejsze od zera")
#         return -1

#     try:
#         wynik = round(waga / (wzrost / 100) ** 2, 2)
#         print("Wynik:", wynik)
#         return wynik
#     except Exception as e:
#         print("Błąd:", e)
#         return -1

# print("liczenie 1")
# print(bmi(80,180))

# print("liczenie 2")
# print(bmi(80, "180"))

# print("liczenie 3")
# print(bmi(80, -180))


# rozwiązanie 2
# def bmi(waga, wzrost):
#     if not isinstance(waga, (int, float)):
#         print("Waga musi być typu float lub int")
#         raise TypeError
#     if not isinstance(wzrost, (int, float)):
#         print("Wzrost musi być typu float lub int")
#         raise TypeError

#     if (waga < 0) or (wzrost < 0):
#         print("Wzrost i waga nie mogą być mniejsze od zera")
#         raise ValueError

#     wynik = round(waga / (wzrost / 100) ** 2, 2)
#     return wynik


# pary_wartosci = [(80, 180), (80, "180"), (80, -180)]
# for i, para in enumerate(pary_wartosci, start=1):
#     print(f"liczenie {i}")
#     try:
#         wynik = bmi(para[0], para[1])
#         print(wynik)
#     except Exception as e:
#         print("Błąd:", e, type(e))


## ZADANIE

# Korzystając z poprzednio pisanego kodu - zbuduj funkcję, która wczyta do listy krotek plik csv rozdzielony ";"
# Wynikiem działania funkcji (powinna to zwracać) ma być ta lista krotek, a argumentem - nazwa pliku.

# rozwiązanie w pliku plik_1.py


# Na podstawie kodu z plik_1.py przygotowano plik.py - moduł


# importowanie całego modułu
# import plik

# zawodnicy = plik.wczytaj("dane.csv")
# print(zawodnicy)
# print(plik.STALA_TESTOWA)


# # importowanie pojedynczej funkcji
# from plik import wczytaj

# zawodnicy = wczytaj("dane.csv")
# print(zawodnicy)

# importowanie wszystkiego z modułu
# from plik import *

# STALA_TESTOWA = "Dobry wieczór"

# zawodnicy = wczytaj("dane.csv")
# print(zawodnicy)
# print(STALA_TESTOWA)

# import matplotlib.pyplot as plt

# plt.axis()


# import matplotlib.pyplot
# matplotlib.pyplot.axis()

# from matplotlib.pyplot import axis
# axis()


### ZADANIE

# Zbuduj moduł obliczenia zawierający funkcję liczącą BMI.
# Użyj tej funkcji w kodzie w ramach main.py.

# rozwiązanie

# powstał plik obliczenia.py

# użycie moduły:
# from obliczenia import bmi
# print(bmi(80, 180))


### ZADANIE

# Do modułu plik dodaj funkcję zapis(), która zapisze do pliku listę krotek.
# Elementy krotki rozdzielone powinny być separatorem (= argument funkcji, domyślnie ;),
# plik powinien mieć odpowiednie kodowanie (= argument, domyślnie utf-8)
# i nazwę (= argument).

# do plik.py dodana została funkcja zapisz()

# test funkcji
# from plik import zapisz

# lista = [
#     ("linia 1", 10, "nazwisko A"),
#     ("linia 2", 20, "nazwisko B"),
#     ("linia 3", 30, "nazwisko C"),
# ]

# zapisz(lista, "test_zapisz.csv")


# Pakiety = zbiory modułów, czyli katalogi z plikami-modułami + plik __init__.py

# zaimportowanie całego modułu z pakietu
# from utils import plik
# plik.wczytaj(...)

# zaimportowanie pojedynczej funkcji z modułu wchodzącego w skład pakietu
# from utils.obliczenia import bmi
# bmi(...)


# import całego pakietu
# import utils
# import utils.plik

# print(utils.plik.STALA_TESTOWA)
# utils.funkcja_w_utils()

# from utils.config import load_config

# config = load_config(..)


## Usługi sieciowe

# odpytujemy serwisy przez pakiet requests
# instalujemy:
# pip install requests
# py -m pip install requests
# python -m pip install requests


# import requests

# response = requests.get("https://api.nbp.pl/dupa")
# print(response)

# print("response.content")
# print(response.content)


# print("response.status_code")
# print(response.status_code)


# zapytanie get
# res = requests.get("https://httpbin.org/get?param=1&param_b=alamakota",
#                    headers={"moj_naglowek": "to jestem ja"})
# print(res.text)

# data = res.json()
# print(data['headers'])


# zapytanie post - wysłanie JSONa
# res = requests.post("https://httpbin.org/post",
#                    json={"moje_pole": "to jestem ja",
#                          "moje_inne_pole": 123})

# print(res.json())


# zapytanie post - wysłanie dany via "data"
# res = requests.post(
#     "https://httpbin.org/post",
#     data="wgwoughwpogvhwpgihwpig",
# )

# print(res.json())


# API NBP
# https://api.nbp.pl/api/exchangerates/tables/A/2024-09-12/?format=json

##### ZADANIE

# Korzystając z API NBP wyświetl notowania EUR, USD, CHF z 2024-09-12


# res = requests.get()
# res.status_code == 200
# res.json()
# przeiterować po danych i wyświetlić odpowiednie elementy/klucze

# import random
# import time

# import requests


# def notowania_nbp(rok=2024, miesiac=9, dzien=12, waluty=["EUR", "USD", "CHF"]):
#     url = f"https://api.nbp.pl/api/exchangerates/tables/A/{rok}-{miesiac:02d}-{dzien:02d}/?format=json"

#     try:
#         # czekamy losowo wybrany czas (losowanie z [0.1, 0.25, 0.15, 0.05]) żeby być miłym dla serwera
#         time.sleep(random.choice([0.1, 0.25, 0.15, 0.05]))
#         res = requests.get(url)
#     except Exception as e:
#         # być może się nie udało - serwer padł, internet padł, pożoga! - obsługujemy błąd
#         print(f"Błąd dla {url=}: {e}")
#         return {}

#     if res.status_code != 200:
#         print(f"Błąd pobrania danych dla {rok}-{miesiac:02d}-{dzien:02d}")
#         return {}

#     data = res.json()[0]

#     wynik = {"data_notowania": data["effectiveDate"]}

#     for kwotowanie in data["rates"]:
#         if kwotowanie["code"] in waluty:
#             wynik[kwotowanie["code"]] = kwotowanie["mid"]

#     return wynik


#  print(notowania_nbp(2024, 9, 10, ['EUR', 'GBP']))


#### ZADANIE

# Używając funkcji notowania_nbp() pobierz notowania dla EUR i USD z całego czerwca,
# lipca i sierpnia 2024. Niech wynik będzie listą słowników.


# czy słownik jest pusty?
# d = {"a": 1}
# if d:
#     print("Coś w słowniku jest")
# else:
#     print("Nie ma nic w słowniku")

# lista_notowan = []

# for m in range(6, 9):
#     for d in range(1, 32):
#         notowanie = notowania_nbp(2024, m, d, ["EUR", "USD"])
#         if notowanie:
#             lista_notowan.append(notowanie)


# print(lista_notowan)

# aktualny czas
# from datetime import datetime
# print(datetime.now())



# konfiguracja w plikach yaml

# bibliotek pyyaml:
# pip install pyyaml

# import yaml

# with open("konfiguracja.yaml", "r", encoding="utf-8") as plik:
#     config = yaml.safe_load(plik)
    
# print(config)


# konfiguracja w różnych formatach https://blog.prokulski.science/2021/03/29/pliki-konfiguracyjne-python-r/


# from utils.config import load_config

# config = load_config("db_postgres.yaml")
# print(config)


# podłączenie do bazy danych - pakiet SQLAlchemy
# pip install sqlalchemy
# pakiety do konkretnych typów baz
# - postgresql - psycopg2
# - Oracle - cx_oracle
# - MSSQL - pymssql
# - MySQL - mysqldb

# https://docs.sqlalchemy.org/en/20/core/engines.html#backend-specific-urls


from utils.config import load_config


def generate_connection_string_postgresql(db_config):
    return f"postgresql+psycopg2://{db_config['db_user']}:{db_config['db_pass']}@{db_config['db_host']}:{db_config['db_port']}/{db_config['db_name']}"

def generate_connection_string_sqlite(db_config):
    return f"sqlite:///{db_config['db_file']}"

config = load_config("db_postgres.yaml")

if config['db_type'] == "postgresql":
    conn_string = generate_connection_string_postgresql(config)
elif config['db_type'] == "sqlite":
    conn_string = generate_connection_string_sqlite(config)
else:
    print("Nie umiem zbudować connection stringa")
    conn_string = ""
    
print(conn_string)