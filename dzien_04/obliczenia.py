def bmi(waga, wzrost):
    if not isinstance(waga, (int, float)):
        print("Waga musi być typu float lub int")
        raise TypeError
    if not isinstance(wzrost, (int, float)):
        print("Wzrost musi być typu float lub int")
        raise TypeError

    if (waga < 0) or (wzrost < 0):
        print("Wzrost i waga nie mogą być mniejsze od zera")
        raise ValueError

    wynik = round(waga / (wzrost / 100) ** 2, 2)
    return wynik
