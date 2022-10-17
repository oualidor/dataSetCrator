import json


def nextText():
    # Opening JSON file
    f = open('data.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    print(len(data))
    for article in data:
        yield article['title'].split(' ')[0]
    # Closing file
    f.close()
