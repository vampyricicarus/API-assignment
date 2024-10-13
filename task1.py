import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
json_data = response.text
pikachu_data = json.loads(json_data)

def fetch_pokemon_data(pikachu_data):
    print(pikachu_data["name"])
    print(pikachu_data["abilities"])

fetch_pokemon_data(pikachu_data)

def fetch_weight(pokemon_name):
    data = response.json()
    return data["weight"]

def calculate_average_weight(pokemon_list):
    total_weight = 0
    valid_pokemon_count = 0
    for pokemon in pokemon_list:
        weight = fetch_weight(pokemon)
        total_weight += weight
        valid_pokemon_count += 1
        average_weight = total_weight / valid_pokemon_count
        print(average_weight)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

calculate_average_weight(pokemon_names)


def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    for planet in planets:
        if planet['isPlanet']:
            name = planet["englishName"]
            mass = planet["mass"]["massValue"]
            orbit_period = planet["sideralOrbit"]
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data() 

def find_heaviest_planet(planets):
    planet_data = []  
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue'] if 'mass' in planet else None
            planet_data.append((name, mass))
    
    heaviest_planet = None
    max_mass = 0
    for name, mass in planet_data:
        if mass is not None and mass > max_mass:
            max_mass = mass
            heaviest_planet = (name, mass)
    
    return heaviest_planet  


planets = fetch_planet_data()


heaviest_planet = find_heaviest_planet(planets)


if heaviest_planet:
    name, mass = heaviest_planet
    print(f"The heaviest planet is {name} with a mass of {mass} kg.")
else:
    print("No planets found.")
