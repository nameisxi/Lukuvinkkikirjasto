import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"

    def create_user(self, kayttajatunnus, salasana):
        data = {
            "tunnus": kayttajatunnus,
            "salasana": salasana,
        }

        requests.post(f"{self._base_url}/rekisteroidu", data=data)