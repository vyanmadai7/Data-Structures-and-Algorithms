hashmap = {}

#insert
hashmap["apple"] = 5
hashmap["banana"] = 10

#access
print(hashmap["apple"])

#update
hashmap["apple"] += 2

#delete
del hashmap["banana"]

#existence check
if "apple" in hashmap:
    print("Exists")