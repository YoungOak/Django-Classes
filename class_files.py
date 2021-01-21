# Clase Manejo de archivos
import json

lines = ["This is line 5", "This is line 6", "This is line 3", "This is line 7"]
with open('data.txt', 'r') as data:
    data_as_list = data.readlines()

data_as_list.insert(1, "This is between line 1 and 2\n")

with open('data.txt', 'w') as data:
    data_as_str = "".join(data_as_list)
    data.write(data_as_str)

with open('data.txt', 'a') as data:
    for line in lines:
        data.write(line)
        data.write('\n')

"""
    Text file's modes:
        w - Write
        r - Read
        a - Append
        r+ - Read  Write
        x - Creation Mode

    Binary file's modes:
        wb - Write
        rb - Read
        ab - Append
        rb+ - Read  Write
"""

data = {
    "id": 0,
    "name": "Mau",
    "age": 24,
    "position": "Web Developer"
}

data_as_json = json.dumps(data)
print(type(data_as_json))

with open('06data.json', 'w') as json_file:
    json.dump(data, json_file)


with open('06data.json', 'r') as json_file:
    pythonic_json = json.load(json_file)

print(pythonic_json)