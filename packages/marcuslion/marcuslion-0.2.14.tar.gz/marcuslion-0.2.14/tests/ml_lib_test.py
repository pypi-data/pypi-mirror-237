import src.marcuslion as ml
from src.marcuslion import *

if __name__ == '__main__':
    try:
        help(ml)
        help(ml.providers)
        # help(ml.datasets)

        df = ml.providers.list()
        print(df.head(10))

        df = ml.datasets.search("bike", "kaggle,usgov")
        print(df.head(3))
        print(df.tail(3))

    except Exception as e:
        print("Exception ", e)
