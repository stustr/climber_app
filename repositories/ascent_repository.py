from db.run_sql import run_sql
from models.ascent import Ascent
from repositories import (
    ascent_repository as ascent_repo,
    climber_repository as climber_repo,
    hill_repository as hill_repo,
)
import pdb


def save(ascent):
    sql = "INSERT INTO ascents (date, description, climber_id, hill_id) values (%s, %s, %s, %s)RETURNING id"
    values = [
        ascent.date,
        ascent.description,
        ascent.climber.id,
        ascent.hill.id,
    ]
    results = run_sql(sql, values)
    id = results[0]["id"]
    ascent.id = id
    return


def select_all():
    ascents = []
    sql = "SELECT * FROM ascents"
    results = run_sql(sql)

    for result in results:
        climber = climber_repo.select(result["climber_id"])
        hill = hill_repo.select(result["hill_id"])
        ascent = Ascent(
            result["date"], result["description"], climber.name, hill.name, result["id"]
        )
        ascents.append(ascent)
    return ascents


def select(id):
    sql = "SELECT * FROM ascents WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        climber = climber_repo.select(result["climber_id"])
        hill = hill_repo.select(result["hill_id"])
        ascent = Ascent(
            result["date"],
            result["description"],
            climber,
            hill,
            result["id"],
        )
    return ascent


def delete(id):
    sql = "DELETE FROM ascents WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    return


def delete_all():
    sql = "DELETE FROM ascents"
    run_sql(sql)
    return


def update(ascent):
    sql = "UPDATE ascents SET (date, description, climber_id, hill_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [
        ascent.date,
        ascent.description,
        ascent.climber.id,
        ascent.hill.id,
        ascent.id,
    ]
    run_sql(sql, values)
    return
