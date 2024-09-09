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


# rozwiązanie 1

# masa = input("Ile ważysz (w kg)? ")
# wzrost = input("podaj wzrost (w cm) ")

# masa = float(masa)
# wzrost = float(wzrost) / 100

# bmi = masa / (wzrost**2)
# # print(f"Twoje BMI to {bmi}.")

# if bmi < 16:
#     bmi_opis = "wyglodzenie"
# elif bmi >= 16 and bmi < 17:
#     bmi_opis = "wychudzenie"
# elif bmi >= 17 and bmi < 18.5:
#     bmi_opis = "niedowaga"
# elif bmi >= 18.5 and bmi < 25:
#     bmi_opis = "pożądana masa ciała"
# elif bmi >= 25 and bmi < 30:
#     bmi_opis = "nadwaga"
# elif bmi >= 30 and bmi < 35:
#     bmi_opis = "otyłość I stopnia"
# elif bmi >= 35 and bmi < 40:
#     bmi_opis = "otyłość II stopnia"
# else:
#     bmi_opis = "otyłość III stopnia"

# print(
#     f"Przy wzroscie {wzrost*100} cm i masie ciala {masa} kg twoje BMI to {bmi:.2f}. Jest to {bmi_opis}."
# )


# rozwiązanie 2

# masa = input("Ile ważysz (w kg)? ")
# wzrost = input("podaj wzrost (w cm) ")

# masa = float(masa)
# wzrost = float(wzrost) / 100

# bmi = masa / (wzrost**2)
# # print(f"Twoje BMI to {bmi}.")

# if bmi < 16:
#     bmi_opis = "wyglodzenie"
# elif bmi < 17:
#     bmi_opis = "wychudzenie"
# elif bmi < 18.5:
#     bmi_opis = "niedowaga"
# elif bmi < 25:
#     bmi_opis = "pożądana masa ciała"
# elif bmi < 30:
#     bmi_opis = "nadwaga"
# elif bmi < 35:
#     bmi_opis = "otyłość I stopnia"
# elif bmi < 40:
#     bmi_opis = "otyłość II stopnia"
# else:
#     bmi_opis = "otyłość III stopnia"

# print(
#     f"Przy wzroscie {wzrost*100} cm i masie ciala {masa} kg twoje BMI to {bmi:.2f}. Jest to {bmi_opis}."
# )


# if 17 <= bmi < 18.5:
#     ...


# Pętle

# for i in iterable:
#     ...

# # range(10) - poda nam 10 kolejnych liczb 0..9
# for i in range(10):
#     print(i)

# print("*|"*40)

# # range(1, 10) - poda nam kolejne liczby 1..9
# for i in range(1, 10):
#     print(i)

# print("*|" * 40)

# # range(3, 10, 2) - poda nam kolejne liczby 3..9 co 4
# for i in range(3, 10, 4):
#     print(i)
    
# print("*|" * 40)


### ZADANIE

# Wyświetl 20 kolejnych potęg liczby 2.

# for n, i in enumerate(range(20), start=1):
#     print(n, 2**i)


# dzielenie
# print("10 / 4 = ", 10 / 4) # zwykłe dzielenie
# print("10 % 4 = ", 10 % 4) # reszta z dzielenia
# print("10 // 4 = ", 10 // 4) # modulo - liczba całkowita z dzielenia


## ZADANIE

# Wydrukuj liczby od 1 do 100 razem z informacją czy liczba jest parzysta czy nieparzysta.

# for i in range(1, 101):
#     if i % 2 == 0:
#         print(f"{i=} parzysta")
#     else:
#         print(f"{i=} nieparzysta")
  
# nieco odwrotnie:      

# for i in range(1, 101):
#     if i % 2:
#         print(f"{i=} nieparzysta")
#     else:
#         print(f"{i=} parzysta")


### ZADANIE

# Napisz symulator lokaty.
# Symulator ma przyjmować zmienne:
# - kwotę lokaty
# - oprocentowanie w skali roku
# - ilość miesięcy na jaką zakładamy lokatę
# Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc oraz ile mamy aktualnie zgromadzone po doliczeniu odsetek. 
# Zakładamy kapitalizację odsetek co miesiąc.


# rozwiązanie

money_amount = float(input("Podaj kwotę lokaty:\n"))
percent = float(input("Podaj oprocentowanie w skali roku (bez znaku %):\n"))
duration = int(input("Podaj czas trwania lokaty w miesiącach:\n"))

for month_number, _ in enumerate(range(1, duration + 1), start=1):
    money_amount += money_amount * ((percent) / 100 / 12)
    # money_amount = money_amount + money_amount * ((percent) / 100 / 12)
    print(f"Miesiąc {month_number}, Stan konta {money_amount:.02f}.")
