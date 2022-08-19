#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter
as a parameter """

if __name__ == "__main__":
    import requests
    import sys

    if sys.argv[1]:
        letter = {"q": sys.argv[1]}
    else:
        letter = {"q": ""}
    response = requests.post('http://0.0.0.0:5000/search_user', letter)
    try:
        response = response.json()
        print("[{}] {}".format(response.get('id'), response.get('name'))
         if response.get('id') else "Not found")
    except Exception:
        print("Not a valid JSON")
