from utils.config import load_config

CONFIG_PATH = "db_postgres.yaml"
# CONFIG_PATH = "db_config_lukasz.yaml"


# funkcje które budują conn-stringi
def generate_connection_string_postgresql(db_config):
    return f"postgresql+psycopg2://{db_config['db_user']}:{db_config['db_pass']}@{db_config['db_host']}:{db_config['db_port']}/{db_config['db_name']}"


def generate_connection_string_sqlite(db_config):
    return f"sqlite:///{db_config['db_file']}"


config = load_config(CONFIG_PATH)

# rozpoznaj z konfigu jaki to typ bazy i odpowiednio zbuduj conn-str
if config["db_type"] == "postgresql":
    conn_string = generate_connection_string_postgresql(config)
elif config["db_type"] == "sqlite":
    conn_string = generate_connection_string_sqlite(config)
else:
    print("Nie umiem zbudować connection stringa")
    conn_string = ""


# można użyć conn-stringa
print(conn_string)
