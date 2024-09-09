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

# rozwiązanie
# imie = input("Jak masz na imię?")
# hello = f"Witaj \n\"mój\tdrogi\" {imie}."
# print(hello)




### ZADANIE 
# Napisz program, który pobierze od użytkownika masę i wzrost, a następnie policzy BMI i wypisze wynik na konsolę.

# https://pl.wikipedia.org/wiki/Wska%C5%BAnik_masy_cia%C5%82a
# BMI = masa [kg] / wzrost^2 [m]

# potegowanie - do kwadratu:
# a*a
# a**2
# pow(a, 2)

# masa = input("Podaj swoją wagę w kg: ")
# wzrost = input("Podaj swój wzrost w cm ")

# masa = float(masa)
# wzrost = float(wzrost)/100

# bmi = masa / wzrost**2

# # zaokrąglenie
# # bmi = round(bmi, 2)

# print(f"Przy wzroście {wzrost*100} cm i masie {masa=} kg Twoje BMI = {bmi:.2f}")


# warunki - IF
# a = 20
# print("przed ifem")
# if a == 1 :
#     print("A jest równe 1")
# elif a == 2:
#     print("A jest równe 2")
# else:
#     print("A nie jest równe 1 ani nie jest równe 2")

# print("po ifie")


### ZADANIE
# Niech użytkownik poda jakąś liczbę.
# W odpowiedzi wyświetlamy tę liczbę i informację czy liczba jest dodatnia, ujemna czy też jest zerem.

# rozwiązanie 1
# liczba = float(input("Daj mi liczbę: "))

# if liczba < 0:
#     print("ujemna")
# elif liczba > 0:
#     print("dodatnia")
# else:
#     print("zero")

# rozwiązanie 2

# liczba = float(input("Daj mi liczbę: "))
# a = "ujemna"
# b = "dodatnia"
# c = "zerem"

# if liczba < 0:
#     print(a)
# elif liczba > 0:
#     print(b)
# else:
#     print(c)


# # rozwiązanie 3

# liczba = float(input("Daj mi liczbę: "))

# KOMUNIKAT_UJEMNA = "ujemna"
# KOMUNIKAT_DODATNIA = "dodatnia"
# KOMUNIKAT_ZERO = "zerem"

# if liczba < 0:
#     komunikat_wyjsciowy = KOMUNIKAT_UJEMNA
# elif liczba > 0:
#     komunikat_wyjsciowy = KOMUNIKAT_DODATNIA
# else:
#     komunikat_wyjsciowy = KOMUNIKAT_ZERO
    
# print(f"Twoja liczba {liczba} jest {komunikat_wyjsciowy}")


# a = 2 
# b = 2

# if a == 1 and b == 2:
#     print("a == 1 and b == 2")

# if a != 1 or b != 2:
#     print("a != 1 or b != 2")
    
# if not a == 1:
#     print("a != 1")
    
# d = False
# if not d:
#     print("D jest NIE PRAWDZIWE")



# jak sprawdzić czy user podał floata

# zmienna = input("Daj cos ")
# print(type(zmienna))

# f = None


# wyjątki - będzie w czwartek
# try:
#     f = float(zmienna)
# except:
#     print("błąd")

# print(zmienna, f)


# funkcja - będzie w czwartek
# def as_float(s):
#     try:
#         f = float(s)
#         return f
#     except:
#         return None


# f = as_float(liczba)



# ZADANIE

# Napisz program, który pobierze od użytkownika masę i wzrost, a następnie policzy BMI i wypisze na konsolę.
# Dodatkowo - na podstawie wartości obliczonego BMI niech poda komentarz.
# <= 16 => wygłodzenie
# 16 - 16.999999 => wychudzenie
# 17 - 18,49 => niedowaga
# 18,5 - 24,999 => pożądana masa ciała
# 25 - 29,999 => nadwaga
# 30 - 34,999 => otyłość I stopnia
# 35 - 39,999 => otyłość II stopnia (duża)
# > 40 otyłość III stopnia (chorobliwa)