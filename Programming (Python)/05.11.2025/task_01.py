#!/usr/bin/env python3

import requests

# response = requests.get("https://swapi.dev/api/people/1")
# data = response.json()
#
# print(data)


def send_request(url: str):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    return None


def main():
    url = "https://swapi.dev/api/people/1"
    data = send_request(url)

    if not data:
        print("Err")
        return
    else:
        name = data["name"]
        height = data["height"]
        mass = data["mass"]
        hair_color = data["hair_color"]

        print(
            f"Name: {name}",
            f"\nHeight: {height}",
            f"\nMass: {mass}",
            f"\nHair color: {hair_color}"
        )


if __name__ == "__main__":
    main()
