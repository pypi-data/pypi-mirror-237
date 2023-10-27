from sphinx.util import requests
import requests
from diningcodeapi.config import HEADERS


class DistrictMixin:
    def get_district(self, proxy=None):
        url = f"https://im.diningcode.com/API/recommend/"
        data = {
            "mode": "district"
        }
        response = requests.post(url, data=data, headers=HEADERS, proxies={"http": proxy})
        response.raise_for_status()
        themes = response.json()
        themes['_id'] = 1
        return themes
