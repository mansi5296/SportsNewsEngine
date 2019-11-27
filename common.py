import json

def openFile(filename):
    with open(filename) as json_data:
        data = json.load(json_data)
        json_data.close()
        return data

def writeFile(filename, data):
    with open(filename, "w") as write_file:
        json.dump(data, write_file)

