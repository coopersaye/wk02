import requests

# Base URL for the Rick and Morty API
base_url = "https://rickandmortyapi.com/api/character"

def get_characters(page=1):
    url = f"{base_url}?page={page}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        for character in data["results"]:
            print(f"Name: {character['name']}")
            print(f"Status: {character['status']}")
            print(f"Species: {character['species']}")
            print(f"Origin: {character['origin']['name']}")
            print(f"Image: {character['image']}")
            print("-" * 40)
    else:
        print(f"Error: {response.status_code}")

# Call the function to get the first page of characters
get_characters()
