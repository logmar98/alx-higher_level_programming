#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""

if __name__ == '__main__':
    from urllib.request import Request, urlopen
    import sys
    from urllib.parse import urlencode

    url = sys.argv[1]
    mail = {"email": sys.argv[2]}
    data = urlencode(mail).encode("ascii")
    req = Request(url, data)

    with urlopen(req) as response:
        print(response.read().decode("utf-8"))