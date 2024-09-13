import random
import time
from datetime import datetime, timedelta

import requests


def notowania_nbp(rok=2024, miesiac=9, dzien=12, waluty=["EUR", "USD", "CHF"]):
    """Pobiera z API NBP listę notowań wskazanych walut dla podanej daty"""
    url = f"https://api.nbp.pl/api/exchangerates/tables/A/{rok}-{miesiac:02d}-{dzien:02d}/?format=json"

    try:
        # czekamy losowo wybrany czas (losowanie z [0.1, 0.25, 0.15, 0.05]) żeby być miłym dla serwera
        time.sleep(random.choice([0.1, 0.25, 0.15, 0.05]))
        res = requests.get(url)
    except Exception as e:
        # być może się nie udało - serwer padł, internet padł, pożoga! - obsługujemy błąd
        print(f"Błąd dla {url=}: {e}")
        return {}

    if res.status_code != 200:
        print(f"Błąd pobrania danych dla {rok}-{miesiac:02d}-{dzien:02d}")
        return {}

    data = res.json()[0]

    wynik = {"data_notowania": data["effectiveDate"]}

    for kwotowanie in data["rates"]:
        if kwotowanie["code"] in waluty:
            wynik[kwotowanie["code"]] = kwotowanie["mid"]

    return wynik


if __name__ == "__main__":
    # obecna data i czas - minus jeden dzień
    wczoraj = datetime.now() - timedelta(days=1)

    notowanie = notowania_nbp(wczoraj.year, wczoraj.month, wczoraj.day, ["EUR", "USD"])
    if notowanie:
        print(notowanie)
