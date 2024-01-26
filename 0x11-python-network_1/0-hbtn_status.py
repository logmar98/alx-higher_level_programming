#!/usr/bin/python3
"""fetches url using urllib"""

if __name__ == '__main__':
    from urllib.request import Request, urlopen

    req = Request("https://alx-intranet.hbtn.io/status")

    with urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")
