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
