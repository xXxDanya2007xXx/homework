#!/usr/bin/env python3

import requests


def send_request(url: str):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    return None


def main():
    url = "https://swapi.dev/api/starships/?search=Millennium%20Falcon"
    data = send_request(url)
    ship_data = data["results"][0]
    pilot_urls = ship_data["pilots"]

    print("Пилоты Millennium Falcon:")
    for url in pilot_urls:
        pilot_data = send_request(url)
        pilot_name = pilot_data["name"]

        print(f"- {pilot_name}")


if __name__ == "__main__":
    main()
