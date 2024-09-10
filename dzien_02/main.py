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

lista = list(range(20))
print(lista)

# elementy o indeksach od 0 do 3 włącznie
print(lista[0:3])

# elementy o indeksach od 10 do 16 włącznie
print(lista[10:16])

# pierwsze 5 elementów
print(lista[:5])

# ostatni elemnt
print(lista[-1])

# ostatnie 5 elementów
# tak "javowo"
print(lista[len(lista)-5 : len(lista)])
# pythonic-style
print(lista[-5:])

# co 3 element
# [od : do : krok]
print(lista[::3])

# od końca
print(lista[::-1])