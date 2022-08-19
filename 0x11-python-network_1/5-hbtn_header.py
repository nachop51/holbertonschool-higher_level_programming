#!/usr/bin/python3
""" Python script that takes in a URL, sends a request
to the URL and displays the value of the variable X-Request-Id
in the response header """

if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html['X-Request-Id'])
