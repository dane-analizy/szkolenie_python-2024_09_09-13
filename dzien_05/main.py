# ### odczyt danych z bazy


# # import sqlalchemy as sa
# # from sqlalchemy import text
# # from utils.config import load_config
# # from utils.db import (
# #     generate_connection_string_postgresql,
# #     generate_connection_string_sqlite,
# # )

# # # CONFIG_PATH = "db_postgres.yaml"
# # CONFIG_PATH = "db_config_lukasz.yaml"

# # config = load_config(CONFIG_PATH)

# # # rozpoznaj z konfigu jaki to typ bazy i odpowiednio zbuduj conn-str
# # if config["db_type"] == "postgresql":
# #     conn_string = generate_connection_string_postgresql(config)
# # elif config["db_type"] == "sqlite":
# #     conn_string = generate_connection_string_sqlite(config)
# # else:
# #     print("Nie umiem zbudować connection stringa")
# #     conn_string = ""


# # print("Connection string: ", conn_string)

# # # budujemy silnik połączenia do bazy
# # db_engine = sa.create_engine(conn_string)
# # db_conn = db_engine.connect()
# # print("Połączenie do bazy: ", db_conn)

# # sql_query = "SELECT * FROM players;"
# # # sql_query = "SELECT AVG(height) AS sr_wzrost FROM players;"

# # result = db_conn.execute(text(sql_query))
# # col_names = list(result.keys())
# # print("Nazwy kolumn: ", col_names)

# # wyniki_db = []
# # for r in result:
# #     print("Jeden wiersz pobrany z bazy: ", r)
# #     temp_dict = {}
# #     for c, el in zip(col_names, r):
# #         temp_dict[c] = el
# #     wyniki_db.append(temp_dict)

# # db_conn.close()

# # print("Lista słowników z wynikami z bazy:")
# # print(wyniki_db)


# ### zapis danych do bazy

# import sqlalchemy as sa
# from sqlalchemy import text
# from utils.config import load_config
# from utils.db import (
#     generate_connection_string_postgresql,
#     generate_connection_string_sqlite,
# )

# # CONFIG_PATH = "db_postgres.yaml"
# CONFIG_PATH = "db_config_lukasz.yaml"

# config = load_config(CONFIG_PATH)

# # rozpoznaj z konfigu jaki to typ bazy i odpowiednio zbuduj conn-str
# if config["db_type"] == "postgresql":
#     conn_string = generate_connection_string_postgresql(config)
# elif config["db_type"] == "sqlite":
#     conn_string = generate_connection_string_sqlite(config)
# else:
#     print("Nie umiem zbudować connection stringa")
#     conn_string = ""


# print("Connection string: ", conn_string)

# # budujemy silnik połączenia do bazy
# db_engine = sa.create_engine(conn_string)
# db_conn = db_engine.connect()
# print("Połączenie do bazy: ", db_conn)


# # pojedyncze zapytanie
# # sql_query = "insert into players (first_name,last_name,height,weight) values ('Stefan', 'Brzęczek', 2.05, 100);"
# # result = db_conn.execute(text(sql_query))


# # wiele rekordów na raz
# # dane do włożenia do tabelki:
# rekordy = [
#     {
#         "imie": "Druga Halina",
#         "nazwisko": "Kowalska-Bąk",
#         "wzrost": 1.65,
#         "waga": 59,
#     },
#     {"imie": "Druga Krystyna", "nazwisko": "Góral", "wzrost": 1.71, "waga": 58},
#     {"imie": "Druga Zosia", "nazwisko": "Iksińska", "wzrost": 1.84, "waga": 65},
#     {"imie": "Drugi Zły", "nazwisko": "Rekord", "wzrost": 1.84, "waga": 65},
# ]

# sql_query = """
# INSERT INTO players (first_name, last_name, height, weight)
# VALUES (:imie, :nazwisko, :wzrost, :waga);
# """

# for rekord in rekordy:
#     try:
#         result = db_conn.execute(text(sql_query), rekord)
#         db_conn.commit()
#         print("Rekord dodany do bazy", rekord)
#     except Exception as e:
#         print(e)
#         print("Błąd - dane do bazy nie trafiły, rekord:", rekord)


# db_conn.close()


rekord = {
    "imie": "Drugi Zły",
    "wzrost": 1.84,
    "waga": 65,
    "nazwisko": "Rekord",
}
print(rekord.keys())


nazwa_tabeli = "waluty"
lista_kolumn = ", ".join(rekord.keys())
lista_kluczy = ", ".join([f":{k}" for k in rekord.keys()])
sql_query = f"INSERT INTO {nazwa_tabeli} ({lista_kolumn}) VALUES ({lista_kluczy})"


#  kolejne kroki w oddzielnych folderach -> nbp oraz app_flask
