import requests

ninja_cats = []

# fetch data from api 5 times
for _ in range(5):
    response = requests.get("https://catfact.ninja/fact")
    if response.status_code == 200:
        data = response.json()
        ninja_cats.append(data["fact"])
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

print("\nList of Ninja Cat Facts:")
for ninja_fact in ninja_cats:
    print(ninja_fact)