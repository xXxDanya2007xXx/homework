from django.shortcuts import render

# Create your views here.
import requests


def people_list(request):
    response = requests.get('https://swapi.dev/api/people/')
    data = response.json()
    people = data.get('results', [])
    return render(request, 'new_project/people_list.html', {'people': people})


def person_detail(request, person_id):
    response = requests.get(f'https://swapi.dev/api/people/{person_id}/')
    person = response.json()

    homeworld_url = person.get('homeworld')
    homeworld_data = requests.get(homeworld_url).json()
    person['homeworld_name'] = homeworld_data.get('name')

    films = []
    for film in person.get('films', []):
        film_data = requests.get(film).json()
        films.append(film_data.get('title'))
    person['films_list'] = films

    vehicles = []
    for vehicle in person.get('vehicles', []):
        vehicle_data = requests.get(vehicle).json()
        vehicles.append(vehicle_data.get('name'))
    person['vehicles_list'] = vehicles

    starships = []
    for starship in person.get('starships', []):
        starship_data = requests.get(starship).json()
        starships.append(starship_data.get('name'))
    person['starships_list'] = starships

    return render(request, 'new_project/person_detail.html', {'person': person})
