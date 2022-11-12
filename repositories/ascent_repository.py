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
            result["date"], result["description"], climber, hill, result["id"]
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


def aggregate_climbs_all():
    sql = "SELECT climber_id, hill_id, Count(*) AS Climbs FROM ascents GROUP BY climber_id, hill_id"
    results = run_sql(sql)
    return results


def climbers_climbs(id):
    climbs = []
    sql = "SELECT hill_id, Count(*) AS climbs FROM ascents WHERE climber_id = %s GROUP BY climber_id, hill_id"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        climb = [result["hill_id"], result["climbs"]]
        climbs.append(climb)
    return climbs


def climbing_comm_summits_alltime():
    all_time_summits = []
    sql = "SELECT ascents.climber_id, Count(DISTINCT hill_id) AS corbetts FROM ascents GROUP BY ascents.climber_id ORDER BY corbetts DESC"
    results = run_sql(sql)
    for result in results:
        all_time_summits.append(result)
    return all_time_summits

def climbing_comm_height_alltime():
    all_time_height = []
    climbers = climber_repo.select_all()
    for climber in climbers:
        total = [climber.id, climber_repo.total_climbing_height(climber.id)]
        all_time_height.append(total)
    return all_time_height