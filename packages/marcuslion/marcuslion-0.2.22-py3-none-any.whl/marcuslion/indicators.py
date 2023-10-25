import io
import urllib
import urllib3

import pandas as pd

from marcuslion.config import base_url, api_key


class Indicators:
    """
    MarcusLion Indicators class
    """

    @staticmethod
    def list() -> pd.DataFrame:
        """
        Indicators.list()
        """
        # $ curl 'https://qa1.marcuslion.com/core/datasets/search?providers=kaggle,usgov&title=bike'
        url = base_url + "/" + 'core/datasets/providers?'
        params = {"apiKey": api_key}
        full_url = url + urllib.parse.urlencode(params)

        # Sending a GET request and getting back response as HTTPResponse object.
        http = urllib3.PoolManager()
        resp = http.request("GET", full_url)
        if resp.status != 200:
            raise ValueError("status: " + url + " -> " + str(resp.status))

        # converting
        string_io = io.StringIO(resp.data.decode())
        return pd.read_json(string_io)

    @staticmethod
    def query(self):
        """
        Indicators.query()
        """
        pass

    @staticmethod
    def search(self, search) -> pd.DataFrame:
        """
        Indicators.search(search)
        """
        pass

    @staticmethod
    def download(self, ref, params) -> pd.DataFrame:
        """
        Indicators.download(ref, params)
        """
        pass

    @staticmethod
    def subscribe(self, ref, params):
        """
        Indicators.subscribe(ref, params)
        """
        pass

