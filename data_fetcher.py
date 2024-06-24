import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


print(API_KEY)

def fetch_data(animal_name):

  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  API_KEY = f"https://api.api-ninjas.com/v1/animals?name={animal_name}&X-Api-Key=9UaBWKTevqExmKLM6ZOCJQ==Ut1IWMTAbSsgpk9U"
  response = requests.get(
    API_KEY
  )
  response.raise_for_status()
  data = response.json()
  data_dictionary = data[0]
  return data_dictionary