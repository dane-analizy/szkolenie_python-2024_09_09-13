# instalacja Flaska: pip install flask

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates_sklep")


@app.route("/")
def home():
    return render_template("sklep_hp.html")


@app.route("/kontakt")
def kontakt():
    return render_template("sklep_kontakt.html")


@app.route("/produkty")
def produkty():
    return render_template("sklep_produkty.html")


@app.route("/o_nas")
def o_nas():
    return render_template("sklep_o_nas.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)


### ZADANIE

# Zrób nową stronę w oparciu o template w html
