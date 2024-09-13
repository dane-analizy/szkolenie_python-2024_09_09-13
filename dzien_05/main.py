import time
import sqlalchemy as sa
from sqlalchemy import text
from utils.config import load_config
from utils.db import (
    generate_connection_string_postgresql,
    generate_connection_string_sqlite,
)

# CONFIG_PATH = "db_postgres.yaml"
CONFIG_PATH = "db_config_lukasz.yaml"

config = load_config(CONFIG_PATH)

# rozpoznaj z konfigu jaki to typ bazy i odpowiednio zbuduj conn-str
if config["db_type"] == "postgresql":
    conn_string = generate_connection_string_postgresql(config)
elif config["db_type"] == "sqlite":
    conn_string = generate_connection_string_sqlite(config)
else:
    print("Nie umiem zbudować connection stringa")
    conn_string = ""


print(conn_string)

# budujemy silnik połączenia do bazy
db_engine = sa.create_engine(conn_string)
db_conn = db_engine.connect()
print(db_conn)

result = db_conn.execute(text("SELECT * FROM players;"))
col_names = list(result.keys())
print(col_names)

for r in result:
    print(r)
    for el in r:
        print(el)

db_conn.close()
