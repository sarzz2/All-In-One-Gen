import requests
import json


def random_quote(formatted=False):
    url = "https://favqs.com/api/qotd"
    response = requests.request("GET", url)
    x = json.loads(response.text)["quote"]
    author, body = x["author"], x["body"]
    return author, body if formatted else body


def formatted_quote():
    author, quote = random_quote(formatted=True)
    return f'{quote} ~{author}'


if __name__ == '__main__':
    print(formatted_quote())





