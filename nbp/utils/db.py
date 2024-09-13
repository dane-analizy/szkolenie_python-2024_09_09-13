import sqlalchemy as sa
from sqlalchemy import text


# funkcje które budują conn-stringi
def generate_connection_string_postgresql(db_config, use_pass=True):
    if use_pass:
        return f"postgresql+psycopg2://{db_config['db_user']}:{db_config['db_pass']}@{db_config['db_host']}:{db_config['db_port']}/{db_config['db_name']}"

    return f"postgresql+psycopg2://{db_config['db_user']}@{db_config['db_host']}:{db_config['db_port']}/{db_config['db_name']}"


def generate_connection_string_sqlite(db_config):
    return f"sqlite:///{db_config['db_file']}"


def get_connect_to_db(conn_string):
    # budujemy silnik połączenia do bazy
    db_engine = sa.create_engine(conn_string)
    db_conn = db_engine.connect()
    return db_conn


def connect_db(config):
    # zbuduj connection string
    # rozpoznaj z konfigu jaki to typ bazy i odpowiednio zbuduj conn-str
    if config["db_type"] == "postgresql":
        conn_string = generate_connection_string_postgresql(config)
    elif config["db_type"] == "sqlite":
        conn_string = generate_connection_string_sqlite(config)
    else:
        print("Nie umiem zbudować connection stringa")
        return None

    db_conn = get_connect_to_db(conn_string)
    return db_conn


def insert_into_db(db_conn, nazwa_tabeli, rekord):
    """Wkłada do podanej tabeli (w ramach połączenia) rekord ze słownika"""

    lista_kolumn = ", ".join(rekord.keys())
    lista_kluczy = ", ".join([f":{k}" for k in rekord.keys()])
    sql_query = f"INSERT INTO {nazwa_tabeli} ({lista_kolumn}) VALUES ({lista_kluczy})"

    try:
        db_conn.execute(text(sql_query), rekord)
        db_conn.commit()
    except Exception:
        # print(e)
        print("Błąd - dane do bazy nie trafiły, rekord:", rekord)
