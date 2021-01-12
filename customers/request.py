CUSTOMERS= [
    {
      "id": 1,
      "name": "Hannah Hall",
      "email": "blah123@blah.com",
      "password": "blah"
    },
    {
      "id": 2,
      "name": "Jimmy",
      "email": "blah123@blah.com",
      "password": "blah"
    },
    {
      "id": 3,
      "name": "Candance",
      "email": "blah123@blah.com",
      "password": "blah"
    },
    {
      "id": 4,
      "name": "David Williams",
      "password": "blah",
      "email": "blah@blah.com"
    },
    {
      "email": "david.lav.williams@gmail.com",
      "password": "blah",
      "name": "David Williams",
      "id": 5
    }
  ]



def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer=None

    for customer in CUSTOMERS:
        if customer["id"]==id:
            requested_customer=customer
    
    return requested_customer
