import builtins
import io
import urllib
import urllib3

import pandas as pd

import src.marcuslion as ml

http = urllib3.PoolManager()


class Providers:
    """
    MarcusLion Providers class
    """

    @staticmethod
    def list() -> pd.DataFrame:
        """
        Providers.list()
        """
        # $ curl 'https://qa1.marcuslion.com/core/datasets/search?providers=kaggle,usgov&title=bike'
        url = ml.base_url + "/" +'core/datasets/providers?'
        params = { 'apiKey' : ml.ml_api_key }
        full_url = url + urllib.parse.urlencode(params)

        # Sending a GET request and getting back response as HTTPResponse object.
        resp = http.request("GET", full_url)
        if resp.status != 200:
            raise ValueError("status: " + url + " -> " + str(resp.status))

        # converting
        string_io = io.StringIO(resp.data.decode())
        return pd.read_json(string_io)

    def query(self):
        """
        Providers.query()
        """
        pass

    def search(self):
        """
        Providers.search()
        """
        pass

