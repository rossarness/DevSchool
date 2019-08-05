import json

JSON_FILE = "test.json"


def json_print():
    with open(JSON_FILE) as data:
        json_file = data.read()
    json_data = json.loads(json_file)['objects']
    json_data = {obj['name']: obj for obj in json_data}
    print(json_data["Object_1"]["text"])
    print(json_data["Object_2"]["text"])
    print(json_data["RKS HUWDU"]['dmg'])
    

if __name__ == "__main__":
    json_print()
