# listy
# lista = list()
# print(lista)

# lista_b = []
# print(lista_b)

# lista = [1, 2, 3]
# print(lista)

# lista_a = [1, 2, 3, "ala", "e", 3.14, 1.23]
# print(lista_a)


# # iteracja po liście
# lista_a = [1, 2, 3, "ala", "e", 3.14, 1.23]
# print(lista_a[3])

# print(f"Lista 'lista_a' ma długość {len(lista_a)} elementów")


# for n, element in enumerate(lista_a):
#     print(f"Element o indeksie {n} : {element}")


# # sposób bardzo łopatologiczny iteracji po liście - częsty "bład" początkującego:
# for i in range(len(lista_a)):
#     print(lista_a[i])

# # pythonic-style:
# for el in lista_a:
#     print(el)


# lista_a = [1, 2]
# for el in lista_a:
#     print(el)
#     print("koniec iteracji")
# else:
#     print("wszystkie iteracje przeszły")


# dodawanie elementów do listy
# lista = []
# print(lista)


# # dodajemy element "1" do listy
# lista.append(1)
# print(lista)

# lista.append(2)
# lista.append(2)
# lista.append(5)
# lista.append(2)

# lista.append("ala ma kota")
# print(lista)

# # usuwanie
# lista.remove(2)
# print(lista)

# czy element jest na liście
# if 5 in lista:
#     print("5 jest na liście, usuwam")
#     lista.remove(5)
# print(lista)

# # wstawienie obiektu przed element o podanym indeksie - tutaj index=2
# lista.insert(2, "napis")
# print(lista)


### ZADANIE

# Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
# Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.


# lista = []

# for p in range(10):
#     lista.append(2**p)

# # print(lista)

# for el in lista:
#     print(el)


# # generator - zna przepis na kolejną wartość
# print(range(1, 2000, 3))

# # generator zrzutowany do listy - od razu mamy wszystkie wartości
# print(list(range(1, 2000, 3)))


# zakresy w liście

# lista = list(range(20))
# print(lista)

# 3 elementy o indeksach od 0  włącznie
# print(lista[0:3])


# elementy o indeksach od 10 do 16, ale bez 16
# print(lista[10:16])

# # pierwsze 5 elementów
# print(lista[:5])

# # ostatni element
# print(lista[-1])

# # ostatnie 5 elementów
# # tak "javowo"
# print(lista[len(lista)-5 : len(lista)])
# # pythonic-style
# print(lista[-5:])

# # co 3 element
# # [od : do : krok]
# print(lista[::3])

# # od końca
# print(lista[::-1])


### ZADANIE

# Napisz program, który pobierze od użytkownika 10 liczb,
# zapamięta je (zapisze na liście), a na koniec wyświetli całą listę pobranych wartości od końca.

# lista = []

# for i in range(10):
#     w = input("Podaj coś: ")
#     lista.append(w)

# print(lista[::-1])


# podmiana wartości w liście
# lista = list(range(20))
# print(lista)


# print(lista[10])

# lista[10] = "zamienione"

# print(lista[10])
# print(lista)


# mutowalność - uwaga nie zawsze kopia jest kopią, a wskazuje na to samo
# l1 = [1, 2, 3, 4]
# l2 = l1
# l3 = l1.copy()
# print(l1)
# print(l2)
# print(l3)


# kopiowania list

# from copy import deepcopy

# nowa_lista = deepcopy(lista)


# l2[2] = "nowa wartość"
# print(l1)
# print(l2)
# print(l3)

# def zrob_cos_z_lista(lista):
#     lista = lista[::-1]
#     # return lista

# l1 = [1, 2, 3, 4]
# l2 = zrob_cos_z_lista(l1)
# print(l1)
# print(l2)


# łączenie list
# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8, 9]

# Python v3.7+
# l3 = l1 + l2

# Python wcześniejsze
# rozszerzenie - uwaga zmienia l1
# l1.extend(l2)
# print(l1)
# print(l1)

# l3 = [ *l1, *l2  ]
# print(l3)


# losowa liczba
# import random
# print(random.randint(1, 100))


### ZADANIE

# Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-100.
# Połącz te dwie listy do jednej i wyświetl na konsoli.

# from random import randint

# list_a = []
# list_b = []

# for _ in range(10):
#     list_a.append(randint(1, 100))
#     list_b.append(randint(1, 100))

# list_c = list_a + list_b
# print(list_c)


# list comprehention = lista składana

# from random import randint

# lista_a = []
# for i in range(10):
#     lista_a.append(i)

# print(lista_a)

# # krócej = list comprehention:
# lista_b = [i for i in range(10)]
# print(lista_b)


#### ZADANIE

# Korzystając z list składanych wygeneruj listę 10 kolejnych potęg dwójki.
# Wyświetl tę listę. Spróbuj zrobić to w jak najkrótszym zapisie.

# rozwiązanie bardzo długie
# l = []
# for p in range(10):
#     w = 2**p
#     l.append(w)

# print(l)


# krok 2 upraszczania
# l = []
# for p in range(10):
#     l.append(2**p)

# print(l)


# krok 3:
# l = [2**p for p in range(10)]

# print(l)

# krok 4
# print([2**p for p in range(10)])


# lista składana z filtrowaniem
# oryginał
# l = []
# for p in range(10):
#     if p % 2 == 0:
#         w = 2**p
#         l.append(w)

# print(l)

# rozwiązanie
# l = [2**p for p in range(10) if p % 2 == 0]
# print(l)


### ZADANIE

# Stwórz dwie listy. Każda z list ma zawierać max 20 losowych liczb z zakresu 1-100.
# Pierwsza ma zawierać tylko parzyste, druga - tylko nie parzyste.
# Użyj list składanych do przygotowania tych list.
# Wyświetl obie listy na ekranie.

# rozwiązanie 1

# import random

# lista_losowych = [random.randint(1, 100) for _ in range(20)]
# lista_parzystych = [el for el in lista_losowych if el % 2 == 0]
# print(lista_parzystych)

# lista_losowych = [random.randint(1, 100) for _ in range(20)]
# lista_nieparzystych = [el for el in lista_losowych if el % 2 != 0]
# print(lista_nieparzystych)


# operator walarus :=
# import random

# print([el for _ in range(20) if (el := random.randint(1, 100)) % 2 == 0])


# rozwiązanie 2
# import random

# lista_losowych = [random.randint(1, 100) for _ in range(40)]

# lista_parzystych = [el for el in lista_losowych if el % 2 == 0]
# print(len(lista_parzystych))
# lista_parzystych = lista_parzystych[:20]
# print(len(lista_parzystych))
# print(lista_parzystych)

# lista_nieparzystych = [el for el in lista_losowych if el % 2 != 0][:20]
# print(len(lista_nieparzystych))
# print(lista_nieparzystych)


# listy list

# l = [
#     [1, 2, 3],
#     ["a", "b", "c"],
#     [10, "ala", 130],
#     [ [10, "20"], [50, 60]],
# ]

# print(l)
# print(l[2][1])
# print(l[3][0][1][0])


# napis = ["napis", "abc"]
# print(napis[::-1])

# tabliczka = []
# for x in range(1, 11):
#     wiersz = []
#     for y in range(1, 11):
#         w = x * y
#         wiersz.append(w)
#     tabliczka.append(wiersz)

# print(tabliczka)


# tabliczka = [[f"{x} * {y} = {x*y}" for y in range(1, 11)] for x in range(1, 11)]

# for row in tabliczka:
#     print(row)


# rozdzielanie napisu na listę stringów - metoda .split(...)
# napis = "ala ma kota.ale nie ma psa"
# slowa = napis.split()
# print(slowa)


# łączenie listy stringów

# to nie działa
# napis_na_nowo = [slowo+slowo for slowo in slowa]
# print(napis_na_nowo)


# napis_na_nowo = ""
# for slowo in slowa:
#     napis_na_nowo = napis_na_nowo + " " + slowo
# print(napis_na_nowo)

# napis_na_nowo = " ".join(slowa)
# print(napis_na_nowo)


### ZADANIE

# Napisz program który z pliku dane.csv wyświetli powiększone imię i nazwisko.

# lista_osob = []
# for linia in open("dane.csv", "r", encoding="utf-8"):
#     linia_czysta = linia.strip()
#     if len(linia_czysta) == 0:
#         continue

#     linia_czysta = linia_czysta.split(";")
#     linia_czysta[0] = linia_czysta[0].upper()
#     lista_osob.append(linia_czysta)

# for osoba in lista_osob:
#     print(osoba[0], osoba[1])


### ZADANIE

# Napisz program który z pliku dane.csv pobierze dane (wykorzystaj poprzednie zadanie)
# i dla każdej z osób policzy BMI. Wyświetl wszystkie dane (wraz z BMI) na ekranie.

# BMI = masa [kg] / wzrost^2 [m]


# wczytanie pliku do listy list - dość uniwersalnie
# sep = ";"
# nazwa_pliku = "dane.csv"
# enc = "utf-8"
# lista_plik = [
#     linia.strip().split(sep)
#     for linia in open(nazwa_pliku, "r", encoding=enc)
#     if linia.strip()
# ]

# # logika biznesowa
# for linia in lista_plik:
#     linia[0] = linia[0].upper()
#     linia[1] = linia[1].upper()
#     linia[2] = float(linia[2])
#     linia[3] = float(linia[3])
#     bmi = linia[3] / (linia[2] / 100) ** 2
#     linia.append(bmi)

# print(lista_plik)


# sortowanie list
# l = [1, 5, 9, 3, 2, 4]
# print(sorted(l))  # zwraca posortowaną listę, nie zmienia oryginału

# l.sort()  # sortuje listę "w miejscu" - pozostaje przesortowana
# print(l)


# l = [ "1", "abads", "9", "13515", "2", "4", "!", "ą", "ż", "deef" ]
# print(sorted(l))

# po którym polu sortować
# print(sorted(lista_plik, key=lambda el: el[2]))

# po którym polu sortować, w jakiej kolejności
# print(sorted(lista_plik, key=lambda el: el[3], reverse=True))


# Tuple = krotka

# l = [ 1, 2, 3, "a", "b" ,"c"]
# k = tuple(l)
# print("Lista:", l)
# print("Krotka:", k)

# k2 = ("napis", "ala", "ma", "kota")
# print("Krotka 2:", k2)
# # print(type(k2))

# # for e in k:
# #     print(e)

# print(list(k2))


# # krotka-comprehention
# k = ( i**2 for i in range(10) )
# print(k)

# for el in ( i**2 for i in range(10) ):
#     print(el)

# k2 = tuple([i**2 for i in range(10)])
# print(k2)


### ZADANIE

# W jednej linijce zbuduj krotkę zawierającą kolejne potęgi liczby 3. A następnie zamień
# te liczby na stringi (w ramach krotki) i posortuj je (tę krotkę) malejąco.

# k = tuple([ str(3**p) for p in range(10)])
# print(k)
# k_s = sorted(k, reverse=True)
# print(k_s)

# wypisanie od tyłu
# k = tuple([str(3**i) for i in range(10)])
# print(k[::-1])


# [
#     ("../katalog", ["katalog_1", "katalog_2"], []),
#     ("../katalog\\katalog_1", [], ["plik_1_1", "plik_1_2"]),
#     ("../katalog\\katalog_2", [], ["plik2_1"]),
# ]

# import os

# for dir_name, dir_list, file_list in os.walk("../katalog"):
#     print(f"W katalogu {dir_name} mamy:")
#     print("Katalogi:")
#     for dir in dir_list:
#         print(f"\t{dir}")
#     print("Pliki:")
#     for file in file_list:
#         print(f"\t{file}")
#     print("---------")


#### ZADANIE
# Znajdź wszystkie pliki, które w nazwie mają ciąg podany przez użytkownika.
# Wyświetl pełne ścieżki do nich.
# Wielkość liter w nazwie plików nie ma znaczenia.


# rozwiązanie zadania z użyciem os
# import os

# name = input("Podaj fragment nazwy pliku: ")

# for dir_name, dir_list, file_list in os.walk(".."):
#     for file in file_list:
#         if name.lower() in file.lower():
#             print(f"Znalazłem plik {file} w katalogu {dir_name}")
#             print(f"Pełna ścieżka: {os.path.join(dir_name, file)}")


# biblioteka Path - Python v3.4+
# from pathlib import Path

# p = Path("../katalog")

# print(p)

# plik = p / "katalog_2" / "plik2_1"
# print(plik)

# print(plik.is_file())
# print(plik.exists())


# rozwiązanie zadania z użyciem Pathlib
# from pathlib import Path

# p = Path("../katalog")

# name = input("Podaj fragment nazwy pliku: ")

# for element in p.rglob("*"):
#     if element.is_dir():
#         continue

#     if name.lower() in element.name.lower():
#         print(f"Znalazłem plik {element.name} w katalogu {element}")


# zestawy = sety
# l = [1, 2, 2, 3, 3, 3, 4]
# print(l)

# k = tuple(l)
# print(k)

# s = set(k)
# print(s)

# print(set(range(10)))

# s = {1, 2, 2, 2, 3, 4, 5, 5, 5}
# print(s)

# s.add(6)
# print(s)

# s.remove(3)
# print(s)

# print(s.pop())
# print(s)
# print(s.pop())
# print(s)
# print(s.pop())
# print(s)


# s1 = {1, 2, 2, 2, 3, 4, 5, 5, 5}
# print("s1", s1)

# s2 = {1, 2, 5, 6, 7}
# print("s2", s2)

# print(s1.intersection(s2))
# print(s2.union(s1))
# print(s2.difference(s1))
# print(s1.difference(s2))


# if 3 in s1:
#     print("3 jest w s1")
# else:
#     print("3 nie ma w s1")

# s = { el for el in range(20)}
# print(s)


### ZADANIE

# Wygeneruj dwa zestawy, dodaj do nich po 20 losowych wartości z zakresu 1-40
# (zestaw finalnie może mieć mniej niż 20 elementów).
# Wyświetl sumę, różnicę i część wspólną takich zestawów.

# import random

# s1 = {random.randint(1, 40) for _ in range(20)}
# s2 = {random.randint(1, 40) for _ in range(20)}

# print("suma: ", s2.union(s1))
# print("część wspólna: ", s1.intersection(s2))
# print("s2 - s1: ", s2.difference(s1))
# print("s1 - s2: ", s1.difference(s2))


# usunięcie duplikatów z danych wejściowych

# sep = ";"
# nazwa_pliku = "dane.csv"
# enc = "utf-8"

# lista_plik = [
#     tuple(linia.strip().split(sep))
#     for linia in open(nazwa_pliku, "r", encoding=enc)
#     if linia.strip()
# ]

# print(lista_plik)

# set może być z elementów hashowalnych - np. tupli
# set_plik = set(lista_plik)
# print(set_plik)

# class Pies:
#     def __init__(self) -> None:
#         pass

# p1 = Pies()
# p2 = Pies()

# l = [ (1, 2), p1, (4, 5), 5, p2]
# print(l)

# print(tuple(l))
# print(set(l))

# print(p1.__hash__())
# print(l.__hash__())
