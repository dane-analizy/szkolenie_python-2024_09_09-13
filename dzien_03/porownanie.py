# parametry wejściowe
nazwa_pliku_1 = "text_1.txt"
nazwa_pliku_2 = "text_2.txt"
enc = "utf-8"

# wczytanie zawartości obu plików
lista_plik_1 = tuple(
    [linia.strip() for linia in open(nazwa_pliku_1, "r", encoding=enc)]
)

lista_plik_2 = tuple(
    [linia.strip() for linia in open(nazwa_pliku_2, "r", encoding=enc)]
)

# przejście linia po linii i sprawdzenie czy są różnice
liczba_roznic = 0


for numer_linii, tresc_linii_1 in enumerate(lista_plik_1):
    # czy mamy jeszcze linie w drugim pliku?
    if numer_linii >= len(lista_plik_2):
        print(
            f"\n===\nPlik {nazwa_pliku_2} się skończył na linii numer {numer_linii}. Kończę pracę"
        )
        break

    # czy linie się różnią?
    if tresc_linii_1 != lista_plik_2[numer_linii]:
        liczba_roznic += 1
        print(f"""
Różnica w linii {numer_linii+1}:
Plik "{nazwa_pliku_1}":
{tresc_linii_1}
Plik "{nazwa_pliku_2}":
{lista_plik_2[numer_linii]}""")


# podsumowanie ile różnic
print(f"\n===\nZnaleziono {liczba_roznic} różnych linii.")
