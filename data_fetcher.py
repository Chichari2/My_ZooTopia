import requests

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
  response = requests.get(
    f"https://api.api-ninjas.com/v1/animals?name={animal_name}&X-Api-Key=9UaBWKTevqExmKLM6ZOCJQ==Ut1IWMTAbSsgpk9U"
  )
  response.raise_for_status()
  data = response.json()
  data_dictionary = data[0]
  return data_dictionary