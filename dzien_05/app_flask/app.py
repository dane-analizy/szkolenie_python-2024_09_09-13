# instalacja Flaska: pip install flask

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates_app")


@app.route("/")
def home():
    return render_template("zmienne.html", zmienna="jakiś nasz napis", inna_zmienna=12)


@app.route("/tabela")
def tabela():
    lista = [
        {"imie": "Jan", "nazwisko": "Nowak"},
        {"imie": "Krzysztof", "nazwisko": "Jarzyna"},
        {"imie": "Rysio", "nazwisko": "Czarnecki"},
    ]
    return render_template("tabelka.html", osoby=lista)


@app.route("/dodaj/<a>/<b>")
def dodaj(a, b):
    return {"a": a, "b": b, "suma": float(a) + float(b)}

### ZADANIE

# Bazując na endpoincie /dodaj przygotuj analogiczny z mnożeniem



if __name__ == "__main__":
    app.run(debug=True, port=5000)


# def funkcja(arg1, arg2, **kwargs):
#     kwargs -> {}

# funkcja(a1, a2, ala=1, basia=30, zosia=50)
#     kwargs['ala'] <- 1
#     kwargs['basia'] <- 30
