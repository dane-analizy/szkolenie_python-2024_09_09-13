# wyświetlenie napisu w pythonie
# print("hello world!")


# wyświetlenie napisu w Javie
# class HelloWorld {
#     public static void main(String[] args) {
#         System.out.println("Hello, World!");
#     }
# }


# PEP8 - długość linii
# def funkcja(
#     pierwszy,
#     drugi,
#     trzeci,
#     czwarty,
#     piaty,
#     pierwszya,
#     drugai,
#     trzaeci,
#     czawarty,
#     paiaty,
# ):
#     pass


# PEP8 - https://peps.python.org/pep-0008
# po polsku - https://analityk.edu.pl/jak-pisac-kod-w-python-aby-byl-czytelny-pep8/


### ZMIENNE

# # definicja zmiennych
# zmienna_liczba_int = 123
# zmienna_liczba_float = 3.1415
# zmienna_napis = "Ala ma kota"

# # wyświetlenie wartości zamiennych
# print(zmienna_liczba_int)
# print(zmienna_liczba_float)
# print(zmienna_napis)

# # zmieniamy wartość zmiennych
# zmienna_liczba_int = "napis drugi"
# zmienna_liczba_float = 998
# zmienna_napis = 1.234

# # wyświetlenie wartości zamiennych
# print(zmienna_liczba_int)
# print(zmienna_liczba_float)
# print(zmienna_napis)

# # operacje na zmiennych
# # wynik_a = zmienna_liczba_int / 2
# # print(wynik_a)

# wynik_b = zmienna_liczba_float + 1000
# print(wynik_b)

# # jakiego typu jest zmienna?
# print(type(zmienna_liczba_int))
# print(type(zmienna_liczba_float))
# print(type(zmienna_napis))

# sklejanie tekstów
# a = "napis jeden"
# b = "drugi ciąg tekstowy"
# c = a + b
# # print(c)
# # print(a, b)

# d = 1234
# # print(a, d)

# # wynik_a_d = a+d
# # print(wynik_a_d)

# # rzutowanie typów (po ang. casting)
# wynik_a_d = a + str(d)
# print(wynik_a_d)

# print(int("12345"))
# # print(int("1text"))
# print(float("123.315153"))


# sklejanie zmiennych do tekstu
# a = "napis"
# b = 123
# # c = a + str(b)
# c = "{}-łącznik-{}".format(b, a)
# print(c)

# # f-string
# c = f"{a}-łącznik-{b}"
# print(c)

# pobieranie wartości od użytkownika
# napis = input("tekst zachęty")
# print(napis)

## ZADANIE
# Napisz program, który pobierze od użytkownika jego imię i wyświetli pozdrowienie. Użyj f-stringów do przygotowania wyniku.
