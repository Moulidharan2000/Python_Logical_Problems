import json

sample_dict = {x: x ** 3 for x in range(10) if x ** 3 % 2 == 0}
print(sample_dict)

sample_json = json.dumps(sample_dict)
print(sample_json)

with open("sample_json.json", 'w') as file:
    json.dump(sample_dict, file)

sample_num = lambda x, y: x if x > y else y
print(sample_num(5, 8))

sample_dict = dict(map(lambda x: (x, x ** 3), range(10)))
print(sample_dict)
