#!/usr/bin/python3
"""
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON
formatted and not empty, display the
id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
You are not allowed to import packages
other than requests and sys
"""
if __name__ == '__main__':
    import requests
    import sys
    import json

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        q = ''
    else:
        q = sys.argv[1]

    r = requests.post(url, data={'q': q})
    try:
        sortie = r.json()
        if sortie:
            print("[{}] {}".format(sortie['id'], sortie['name']))
        else:
            print("No result")
    except json.JSONDecodeError:
        print("Not a valid JSON")
