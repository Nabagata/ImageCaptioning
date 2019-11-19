import json

with open("results_train.json") as json_file:
    json_data = json.load(json_file)
    print(json_data['images'])
