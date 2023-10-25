import io
import urllib
import urllib3

import pandas as pd

from marcuslion.config import base_url, api_key


class Documents:
    """
    MarcusLion Documents class
    """

    @staticmethod
    def list() -> pd.DataFrame:
        """
        Documents.list()
        """
        url = base_url + "/" + 'core/documents/list?'
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
    def query(self, search, sub_search):
        """
        Documents.query()
        """
        pass

    @staticmethod
    def search(self):
        """
        Documents.search()
        """
        pass

