import requests
import certifi

def main():
  animal_name = input("Enter animal name: ")
  response = requests.get(

    f"https://api.api-ninjas.com/v1/animals?name={animal_name}&X-Api-Key=9UaBWKTevqExmKLM6ZOCJQ==Ut1IWMTAbSsgpk9U",
    verify=certifi.where(),
    timeout=10
  )
  response.raise_for_status()
  data = response.json()
  print(data)


if __name__ == "__main__":
  main()
