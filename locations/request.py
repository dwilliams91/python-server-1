import sqlite3
import json
from models import Location

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

def get_all_locations():
    with sqlite3.connect("./kennels.db") as conn:

        conn.row_factory=sqlite3.Row
        db_cursor=conn.cursor()

        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        """)

        locations=[]

        dataset=db_cursor.fetchall()

        for row in dataset:

            location=Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    return json.dumps(locations)


def get_single_location(id):
    with sqlite3.connect("./kennels.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        WHERE l.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        location = Location(data['id'], data['name'], data['address'])

    return json.dumps(location.__dict__)

def delete_location(id):

    location_index= -1

    for index, location in enumerate(LOCATIONS):
        if location["id"]==id:
            location_index=index
    
    if location_index >=0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location["id"] ==id:
            LOCATIONS[index] = new_location
            break