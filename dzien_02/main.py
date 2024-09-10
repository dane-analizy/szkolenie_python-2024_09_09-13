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