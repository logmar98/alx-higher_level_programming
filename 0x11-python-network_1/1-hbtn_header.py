#!/usr/bin/python3
"""displays the value of the X-Request-Id"""

if __name__ == '__main__':
    from urllib.request import Request, urlopen
    import sys

    url = str(sys.argv[1])
    req = Request(url)

    with urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
