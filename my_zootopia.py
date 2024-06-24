import requests
from data_fetcher import fetch_data

def main():
  animal_name = input("Enter a name of an animal: ")
  data = fetch_data(animal_name)
  if data == []:
    print(f"<h2>The animal {animal_name} doesn't exist.</h2>")
  else:
    print(data)


if __name__ == "__main__":
  main()
