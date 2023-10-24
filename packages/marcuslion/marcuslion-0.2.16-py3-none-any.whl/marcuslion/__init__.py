import logging
import ssl
import skimage as ski
import os.path
import pandas as pd

from src.marcuslion.datasets import Datasets
from src.marcuslion.providers import Providers

logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

logger.info("Start marcuslion lib")

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 2000)

resource_path = os.path.join(os.path.split(__file__)[0], "resources")
image = ski.io.imread(resource_path + "/marcus_lion_logo.jpg")
ski.io.imshow(image)


# this required downgrading requests library to urllib3-1.24.3 to avoid SSL cert error
ssl._create_default_https_context = ssl._create_unverified_context

ml_api_key = os.getenv('MARCUSLION_API_KEY', "<DUMMY>")
base_url = "https://qa1.marcuslion.com"

providers = Providers()
datasets = Datasets()

def help1():
    print("  ml.providers.list() or ml.datasets.search()")





