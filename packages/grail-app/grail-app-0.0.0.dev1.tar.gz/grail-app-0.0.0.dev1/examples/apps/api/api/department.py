from open_alchemy import models
Department = models.Department
def search():

    """Get all employees from the flask.current_app.extensions['sqlalchemy']."""
    employees = Department.query.all()
    employee_dicts = map(lambda employee: employee.to_dict(), employees)
    return list(employee_dicts)