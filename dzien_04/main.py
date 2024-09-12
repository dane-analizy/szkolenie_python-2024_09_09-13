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

for i, linia in enumerate(open("dane.csv", "r", encoding="utf-8"), start=1):
    lista_linia = linia.strip().split(";")
    try:
        print(lista_linia[3])
    except IndexError as e:
        print(f"Nieodpowiednia struktura w linii {i}")
    except Exception as e:
        print(f"Nieznany błąd: {e}")