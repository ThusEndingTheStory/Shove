from sqlitedict import SqliteDict
import os
 
class SHOVE():
    def __init__(self, data):
        self.data = data
 
def save(key, value):
    try:
        with SqliteDict("shove.cache.sqlite3") as cache:
            cache[key] = value
            cache.commit()
    except Exception as ex:
        print("Error during storing data (possibly unsupported):", ex)
 
def load(key):
    try:
        with SqliteDict("shove.cache.sqlite3") as cache:
            value = cache[key]
            return value
    except Exception as ex:
        print("Error during loading data:", ex)

def clearData():
  try:
    os.system("rm shove.cache.sqlite3")
  except Exception as ex:
    print("Error during clearing data:", ex)
