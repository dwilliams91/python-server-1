import sqlite3
import json
from models import Employee 
from models import Location

EMPLOYEES= [
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


def get_all_employees():
  with sqlite3.connect("./kennels.db") as conn:
    conn.row_factory =sqlite3.Row
    db_cursor=conn.cursor()

    db_cursor.execute(""" 
    SELECT 
      e.id,
      e.name,
      e.address,
      e.location_id,
      l.name location_name,
      l.address location_address
    FROM employee e
    JOIN Location l
      on l.id=e.location_id
    """)
    
    employees=[]

    dataset=db_cursor.fetchall()

    for row in dataset:
      employee= Employee(row['id'], row['name'], row['address'], row['location_id'])

      location = Location(row['location_id'],row['location_address'], row['location_name'])
      employee.location=location.__dict__
      employees.append(employee.__dict__)
      
  return json.dumps(employees)




def get_single_employee(id):
    with sqlite3.connect("./kennels.db") as conn:
      conn.row_factory=sqlite3.Row
      db_cursor=conn.cursor()

    db_cursor.execute("""
    SELECT 
      e.id,
      e.name,
      e.address,
      e.location_id
    FROM employee e
    WHERE e.id=?    
    """,(id,))

    data=db_cursor.fetchone()

    employee= Employee(data['id'], data['name'], data['address'], data['location_id'])
  
    return json.dumps(employee.__dict__)

def create_employee(employee):

    max_id = EMPLOYEES[-1]["id"]
    
    new_id = max_id+1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee

def delete_employee(id):

    employee_index= -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"]==id:
            employee_index=index
    
    if employee_index >=0:
        EMPLOYEES.pop(employee_index)


def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] ==id:
            EMPLOYEES[index] = new_employee
            break

def get_employees_by_location(location_id):

  with sqlite3.connect("./kennels.db") as conn:
      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()

      db_cursor.execute("""
        SELECT 
          e.id,
          e.name,
          e.address,
          e.location_id
        FROM employee e
        WHERE e.location_id=?    
        """,(location_id,))

      employees=[]

      dataset=db_cursor.fetchall()

      for row in dataset:
        employee= Employee(row['id'], row['name'], row['address'], row['location_id'])
    
        employees.append(employee.__dict__)
  return json.dumps(employees)