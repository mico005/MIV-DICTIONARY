import json

# Load JSON file
with open("words.json", "r") as f:
    data = json.load(f)

# Convert every string in the list to lower case
data = [item.lower() for item in data if isinstance(item, str)]

# Save the updated list to the JSON file
with open("words.json", "w") as f:
    json.dump(data, f)
