#!/usr/bin/env python3

import requests


def send_request(url: str):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    return None


def main():
    url = "https://swapi.dev/api/people/1"
    data = send_request(url)

    if not data:
        print("Ошибка")
        return
    else:
        new_url = data["homeworld"]
        new_data = send_request(new_url)
        planet = new_data["name"]

        print(f"Люк Скайуокер родился на планете {planet}.")


if __name__ == "__main__":
    main()
