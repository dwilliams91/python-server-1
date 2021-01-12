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
    return EMPLOYEES

def get_single_employee(id):
    requested_employee=None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee=employee

    return requested_employee

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
