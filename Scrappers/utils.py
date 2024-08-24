import requests


def get_request(url: str="https://www.olympedia.org/sports") -> str:
    return requests.get(url).text