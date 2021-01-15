import sqlite3
import json
from models import Customer

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



# def get_all_customers():
#     with

def get_all_customers():
    # Open a connection to the database
    with sqlite3.connect("./kennels.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.email,
            c.password,
            c.address
        FROM customer c
        """)

        # Initialize an empty list to hold all animal representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            customer = Customer(row['id'], row['name'], row['email'], row['password'], row['address'])

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)


def get_single_customer(id):
    with sqlite3.connect("./kennels.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.email,
            c.password,
            c.address
        FROM customer c
        WHERE c.id=?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        customer = Customers(data['id'], data['name'], data['email'],
                            data['password'], data['address'])

    return json.dumps(customer.__dict__)

def get_customers_by_email(email):

    with sqlite3.connect("./kennels.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)

def create_customer(customer):
    # Get the id value of the last animal in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):

    customer_index= -1

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"]==id:
            customer_index=index
    
    if customer_index >=0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] ==id:
            CUSTOMERS[index] = new_customer
            break

