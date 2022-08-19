#!/usr/bin/python3
"""  Python script that takes in a URL,
sends a request to the URL and displays
the body of the response """

if __name__ == "__main__":
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
