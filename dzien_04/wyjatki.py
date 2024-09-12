lista = [1, 2, 3, 0, "abc", 10, 50]

for el in lista:
    print("el: ", el)
    try:
        wynik_liczenia = 1 / el
        print("wynik_liczenia: ", wynik_liczenia)
        wynik_scalania = 1 + str(el)
        print("wynik_scalania: ", wynik_scalania)
    except TypeError:
        print("Błąd typów - nie możesz dodawać stringa do liczby")
    except ZeroDivisionError:
        print("Błąd typów - nie możesz dzielić przez zero")
    except Exception as e:
        print("nie udało się")
        print("Wyjątek:", e, type(e))
