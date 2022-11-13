from db.run_sql import run_sql
from models.climber import Climber
import math


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
        climber = Climber(result["name"], result["id"])
        climbers.append(climber)
    return climbers


def select(id):
    climber = None
    sql = "SELECT * FROM climbers WHERE id = %s"
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


def total_climbing_height(id):
    sql = "SELECT hills.height, Count(*) AS climbs FROM ascents INNER JOIN hills ON ascents.hill_id = hills.id WHERE climber_id = %s GROUP BY ascents.climber_id, ascents.hill_id, hills.height"
    values = [id]
    results = run_sql(sql, values)
    total = 0
    for result in results:
        hill_total = result[0] * result[1]
        total += hill_total
    return total


def amount_completed(id):
    climbs = []
    sql = "SELECT hill_id, Count(*) AS climbs FROM ascents WHERE climber_id = %s GROUP BY climber_id, hill_id"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        climbs.append(result)
    return [len(climbs), math.ceil(len(climbs)/222 * 100)]

