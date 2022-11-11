from db.run_sql import run_sql
from models.activity import Activity
from repositories import activity_repository as activity_repo, climber_repository as climber_repo, hill_repository as hill_repo


def save(activity):
    sql = "INSERT INTO activities (name, time, description, climber, hill) RETURNING id"
    values = [
        activity.name,
        activity.time,
        activity.description,
        activity.climber.id,
        activity.hill.id,
    ]
    results = run_sql(sql, values)
    id = results[0]["id"]
    activity.id = id
    return


def select_all():
    activities = []
    sql = "SELECT * FROM activities"
    results = run_sql(sql)

    for result in results:
        climber = climber_repo.select(result["climber"])
        hill = hill_repo.select(result["hill"])
        activity = Activity(
            result["name"],
            result["time"],
            result["description"],
            climber.name,
            hill.name,
        )
        activities.append(activity)
    return activities


def select(id):
    sql = "SELECT * FROM activities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        climber = climber_repo.select(result["climber"])
        hill = hill_repo.select(result["hill"])
        activity = Activity(result["name"], result["time"], result["description"], climber.name, hill.name, result["id"])
    return activity

def delete(id):
    sql = "DELETE * FROM activities WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    return

def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)
    return

def update(activity):
    sql = "UPDATE activities SET (name, time, description, climber, hill) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [activity.name, activity.time, activity.description, activity.climber.id, activity.hill.id, activity.id]
    run_sql(sql, values)
    return