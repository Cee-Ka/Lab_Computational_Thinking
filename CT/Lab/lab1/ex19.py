import json
json_str = '{"name": "Mai", "age": 25, "city": "Hanoi"}'
d = json.loads(json_str)
print("Ten: ", d["name"])
print("Tuoi: ", d["age"])
print("Thanh pho: ", d["city"])
print(json.dumps(d))