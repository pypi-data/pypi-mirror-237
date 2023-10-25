import io
import urllib
import urllib3
import json

import pandas as pd

from marcuslion.config import base_url, api_key


class Datasets:
    """
    MarcusLion Datasets class
    """
    @staticmethod
    def search(search, provider_list) -> pd.DataFrame:
        """
        Datasets.search()
        """
        # $ curl 'https://qa1.marcuslion.com/core/datasets/search?providers=kaggle,usgov&title=bike'
        url = base_url + '/core/datasets/search?'
        params = {"providers": provider_list, "title": search, "apiKey": api_key}
        full_url = url + urllib.parse.urlencode(params)

        # Sending a GET request and getting back response as HTTPResponse object.
        http = urllib3.PoolManager()
        resp = http.request("GET", full_url)
        if resp.status != 200:
            raise ValueError("status: " + url + " -> " + str(resp.status))

        # converting
        string_io = io.StringIO(resp.data.decode())
        data = json.load(string_io)
        return pd.DataFrame(data['data'])

    @staticmethod
    def query(self, ref):
        """
        Datasets.query(ref)
        """
        pass

    @staticmethod
    def search(self, search) -> pd.DataFrame:
        """
        Datasets.search(search)
        """
        pass

    @staticmethod
    def download(self, ref) -> pd.DataFrame:
        """
        Datasets.download(ref)
        """
        pass