#!/usr/bin/python3
""" Python script that takes in a URL, sends a request
to the URL and displays the body of the response """

if __name__ == "__main__":
    import requests
    import sys

    response = requests.get(sys.argv[1])
    if response.status_code < 400:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))
