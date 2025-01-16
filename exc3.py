import json

# python dictionary
item = {
    "name": "Book of the knowledge",
    "rarity": "common",
    "durability": 100
}

# encode to json
json_string = json.dumps(item)
print("Encoded to JSON string:")
print(json_string)

# decode back to python
decoded_item = json.loads(json_string)
print("\nDecoded back to Python dictionary:")
print(decoded_item)

# write json to file
with open("item.json", "w") as json_file:
    json.dump(item, json_file)
    print("\nJSON data written to file 'item.json'.")

# read json from file
with open("item.json", "r") as json_file:
    loaded_item = json.load(json_file)
    print("\nJSON data read from file:")
    print(loaded_item)