ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1
    }
]
LOCATIONS= [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "8422 Johnson Pike"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "209 Emory Drive"
    }
  ]
EMPLOYEES = [
    {
      "id": 2,
      "name": "Baxter Williams",
      "animalId": 1,
      "locationId": 1
    },
    {
      "id": 4,
      "name": " Dwillz123",
      "locationId": 1,
      "animalId": 1
    },
    {
      "name": "Britt",
      "locationId": 1,
      "animalId": 1,
      "id": 5
    },
    {
      "name": "Jim",
      "locationId": 2,
      "animalId": 5,
      "id": 6
    }
  ]

def get_all_animals():
    return ANIMALS

def get_all_locations():
    return LOCATIONS

def get_all_employees():
    return EMPLOYEES
