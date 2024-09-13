from sqlalchemy import text
from utils.config import load_config
from utils.db import connect_db, insert_into_db
from utils.nbp import notowania_nbp

# CONFIG_PATH = "db_postgres.yaml"
# CONFIG_PATH = "db_config_lukasz.yaml"
CONFIG_PATH = "db_sqlite.yaml"


# 1. wczytać konfigurację -> load_config()
config = load_config(CONFIG_PATH)

# 2. podłączyć się do bazy -> connect_db()
db_conn = connect_db(config)

# 3. utworzyć tabelę - czyli wysłać do bazy zapytanie:
sql_query = """
CREATE TABLE IF NOT EXISTS waluty (
    data VARCHAR(12),
    waluta VARCHAR(4),
    kurs FLOAT
);
"""
db_conn.execute(text(sql_query))
db_conn.commit()

# 4. pobrać notowania z NBP - np. EUR, CHF i USD dla całego sierpnia i września -> notowania_nbp()

r = 2024  # pobieramy tylko rok 2024
# te waluty pobieramy
waluty = ["CAD", "JPY"]

# lecimy po miesiącach:
for m in range(1, 13):
    # lecimy po dniach:
    for d in range(1, 32):
        # pobieramy kwotowanie dla wszystkich wybranych walut dla danego dnia
        kwotowanie = notowania_nbp(r, m, d, waluty)

        # jeśli się nie udało - idziemy do kolejnego dnia
        if not kwotowanie:
            continue

        # budujemy rekord dla bazy danych
        kwotowanie_db = {"data": f"{r}-{m:02d}-{d:02d}"}

        # dla każdej waluty - robimy odpowiedni rekord dla DB i wkładamy do bazy
        for waluta in waluty:
            kwotowanie_db["waluta"] = waluta
            kwotowanie_db["kurs"] = kwotowanie[waluta]
            # 5. zapisać do bazy notowania -> insert_into_db(), odpowiednio przebuduj słownik z notowaniem
            try:
                insert_into_db(db_conn, "waluty", kwotowanie_db)
            except Exception:
                pass

# 6. rozłączyć się z bazą -> db_conn.close()
db_conn.close()
