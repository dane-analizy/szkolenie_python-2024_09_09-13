# CONFIG_PATH = "db_postgres.yaml"
CONFIG_PATH = "db_config_lukasz.yaml"

# 1. wczytać konfigurację -> load_config()
# 2. podłączyć się do bazy -> connect_db()
# 3. utworzyć tabelę - czyli wysłać do bazy zapytanie:
"""
CREATE TABLE IF NOT EXISTS waluty (
    data VARCHAR(12),
    waluta VARCHAR(4),
    kurs FLOAT
);
"""
# 4. pobrać notowania z NBP - np. dla całego sierpnia i września -> notowania_nbp()
# 5. zapisać do bazy notowania -> insert_into_db(), odpowiednio przebuduj słownik z notowaniem
# 6. rozłączyć się z bazą -> db_conn.close()
