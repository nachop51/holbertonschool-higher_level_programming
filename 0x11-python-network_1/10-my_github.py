#!/usr/bin/python3
""" Python script that takes your GitHub
credentials (username and password) and uses
the GitHub API to display your id """


if __name__ == "__main__":
    import requests
    import sys


    auth = (sys.argv[1], sys.argv[2])
    response = requests.get('https://api.github.com/user', auth=auth)
    if response.status_code < 400:
        print(response.json().get('id'))
    else:
        print('None')
