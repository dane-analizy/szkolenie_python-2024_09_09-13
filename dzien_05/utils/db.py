# funkcje które budują conn-stringi
def generate_connection_string_postgresql(db_config, use_pass=True):
    if use_pass:
        return f"postgresql+psycopg2://{db_config['db_user']}:{db_config['db_pass']}@{db_config['db_host']}:{db_config['db_port']}/{db_config['db_name']}"

    return f"postgresql+psycopg2://{db_config['db_user']}@{db_config['db_host']}:{db_config['db_port']}/{db_config['db_name']}"


def generate_connection_string_sqlite(db_config):
    return f"sqlite:///{db_config['db_file']}"
