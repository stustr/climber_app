from db.run_sql import run_sql
from models.climber import Climber


def save(climber):
    sql = "INSERT INTO climbers (name) VALUES (%s) RETURNING id"
    values = [climber.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    climber.id = id
    return


def select_all():
    climbers = []
    sql = "SELECT * FROM climbers"
    results = run_sql(sql)
    for result in results:
        climber = Climber(result["name"])
        climbers.append(climber)
    return climbers


def select(id):
    climber = None
    sql = "SELECT FROM climbers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        climber = Climber(result["name"], result["id"])
    return climber


def update(climber):
    sql = "UPDATE climbers SET name = %s WHERE id = %s"
    values = [climber.name, climber.id]
    run_sql(sql, values)
    return


def delete(id):
    sql = "DELETE FROM climbers WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    return


def delete_all():
    sql = "DELETE FROM climbers"
    run_sql(sql)
