#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter
as a parameter """

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) > 1:
        letter = {"q": sys.argv[1]}
    else:
        letter = {"q": ""}
    response = requests.post('http://0.0.0.0:5000/search_user', data=letter)
    try:
        result = response.json()
        if result == {}:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
    except ValueError:
        print("Not a valid JSON")
