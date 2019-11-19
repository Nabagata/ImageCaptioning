import json

with open("captions_val2014.json") as json_file:
    json_data = json.load(json_file)
    print(json_data['annotations'])
