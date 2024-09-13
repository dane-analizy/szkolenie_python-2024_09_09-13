# instalacja Flaska: pip install flask

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Strona główna 1</h1>"


@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)


### ZADANIE

# Zrób nową stronę w oparciu o template w html
