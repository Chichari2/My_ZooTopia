import requests

def main():
  animal_name = input("Enter a name of an animal: ")
  response = requests.get(
  f"https://api.api-ninjas.com/v1/animals?name={animal_name}&X-Api-Key=9UaBWKTevqExmKLM6ZOCJQ==Ut1IWMTAbSsgpk9U"
  )
  response.raise_for_status()
  data = response.json()
  if data == []:
    print(f"<h2>The animal {animal_name} doesn't exist.</h2>")
  else:
    print(data)


if __name__ == "__main__":
  main()
