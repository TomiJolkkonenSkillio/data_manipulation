import json

# python dictionary
item = {
    "name": "Book of the knowledge",
    "rarity": "common",
    "durability": 100
}

# key-value pair to python object
item["price"] = 1000

# array to python object
item["sellers"] = ["John", "Peter", "Mary"]

# object to python object
item["description"] = {
    "text": "This is a book of knowledge",
    "author": "Unknown",
    "importantPages": [33, 44, 555]
}

# print item variable
print("Updated Python object:")
print(item["description"])

# print price from object
print("\nPrice: ", item["price"])

# print "Peter" from array
print("\nAuthor from array:", item["sellers"][1])

# print out "555" from object
print("\nOne important page: ", item["description"]["importantPages"][2])

# print out using one line (check if description exists)
print(f"\nDescription: {item['description']['text']}\nBookmarked page: {item['description']['importantPages'][2]}")

# remove price, seller, description from object
item.pop("price", None)
item.pop("sellers", None)
item.pop("description", None)

# final print out
print("\nFinal Python object after removals:")
print(item)
