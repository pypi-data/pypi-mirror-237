"""Functions handling API endpoints."""
import flask
from open_alchemy import models
Employee = models.Employee


def search():
    """Get all employees from the flask.current_app.extensions['sqlalchemy']."""
    employees = Employee.query.all()
    employee_dicts = map(lambda employee: employee.to_dict(), employees)
    return list(employee_dicts)


def post(body):
    """Save an employee to the flask.current_app.extensions['sqlalchemy']."""
    if Employee.query.filter_by(id=body["id"]).first() is not None:
        return ("Employee already exists.", 400)
    employee = Employee.from_dict(**body)
    flask.current_app.extensions['sqlalchemy'].db.session.add(employee)
    flask.current_app.extensions['sqlalchemy'].db.session.commit()


def get(id):
    """Get an employee from the flask.current_app.extensions['sqlalchemy']."""
    employee = Employee.query.filter_by(id=id).first()
    if employee is None:
        return ("Employee not found.", 404)
    return employee.to_dict()


def patch(body, id):
    """Update an employee in the dayabase."""
    employee = Employee.query.filter_by(id=id).first()
    if employee is None:
        return ("Employee not found.", 404)
    employee.name = body["name"]
    employee.division = body["division"]
    employee.salary = body["salary"]
    flask.current_app.extensions['sqlalchemy'].db.session.commit()
    return 200


def delete(id):
    """Delete an employee from the flask.current_app.extensions['sqlalchemy']."""
    result = Employee.query.filter_by(id=id).delete()
    if not result:
        return ("Employee not found.", 404)
    flask.current_app.extensions['sqlalchemy'].db.session.commit()
    return 200