from flask import Flask, redirect, render_template, request
from sqlalchemy import text
from utils.config import load_config
from utils.db import connect_db

# CONFIG_PATH = "db_postgres.yaml"
# CONFIG_PATH = "db_config_lukasz.yaml"
CONFIG_PATH = "db_sqlite.yaml"


# 1. wczytać konfigurację -> load_config()
config = load_config(CONFIG_PATH)


app = Flask(__name__)


"""
waluta -> nazwa waluty do tytułu
waluty -> lista dostępnych walut
kwotowania -> lista par data-kurs

kurs/EUR?od=...&do=..
"""


@app.route("/")
def hp():
    return redirect("/kurs/EUR")


@app.route("/kurs/<waluta>")
def kurs(waluta):
    sql_query = f"""
    select
        data,
        kurs
    from waluty
    where
        waluta='{waluta.upper()}'
    order by data;"""

    if request.args.get("od"):
        sql_query = f"""
    select
        data,
        kurs
    from waluty
    where
        waluta='{waluta.upper()}'
        and data >= '{request.args.get("od")}'
    order by data;"""

    if request.args.get("do"):
        sql_query = f"""
    select
        data,
        kurs
    from waluty
    where
        waluta='{waluta.upper()}'
        and data <= '{request.args.get("do")}'
    order by data;"""

    if request.args.get("od") and request.args.get("do"):
        sql_query = f"""
    select
        data,
        kurs
    from waluty
    where
        waluta='{waluta.upper()}'
        and data >= '{request.args.get("od")}'
        and data <= '{request.args.get("do")}'
    order by data;"""

    # podłączyć się do bazy -> connect_db()
    db_conn = connect_db(config)

    # lista dostępnych walut
    res = db_conn.execute(text("select distinct waluta from waluty;"))
    waluty = [r[0] for r in res]

    # kwotowania wybranej waluty w zakresie od-do
    res = db_conn.execute(text(sql_query))

    wyniki = [{"data": r[0], "kurs": r[1]} for r in res]

    # zamykamy połącznie z bazą danych
    db_conn.close()

    return render_template("kurs.html", waluta=waluta, waluty=waluty, kwotowania=wyniki)


if __name__ == "__main__":
    app.run(port=5000)
