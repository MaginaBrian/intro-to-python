person = {
    "first_name": "Brian",
    "last_name": "kiptoo",
    "age": 20,
    "gender": "male",
    "isActive": True
}
print(dir(person))
# accessing values using key
# print(person["height"])

# accessing values using get method
# print(person.get("height", "key not found"))

# accessing keys using key() method

person_keys = person.keys()
# print(person_keys)

# accessing values using values() method

person_values = person.values()
# print(person_values)

# accesing both keys and values using items() method

items = person.items()
# print(items)

for key, value in items:
    print(f' {key} : {value}')   