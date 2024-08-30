import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
API_KEY = os.getenv('API_KEY')

# Define the base URL for the API
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
  """
  Fetches the animal data for the given animal name.
  Returns: a list of animals, each animal is a dictionary.
  """
  headers = {
    'X-Api-Key': API_KEY
  }

  # Construct the API request URL
  url = f"{API_URL}?name={animal_name}"

  # Make the API request
  response = requests.get(url, headers=headers)

  # Raise an error for bad responses
  response.raise_for_status()

  # Parse the JSON response
  data = response.json()

  # Return the list of animals
  return data
