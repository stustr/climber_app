from db.run_sql import run_sql
from models.hill import Hill


def save(hill):
    sql = "INSERT INTO hills (name) VALUES (%s) RETURNING id"
    values = [hill.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    hill.id = id


def select_all():
    hills = []
    sql = "SELECT * FROM hills"
    results = run_sql(sql)
    for result in results:
        hill = hill(result["name"], result["height"], result["area"], result["id"])
        hills.append(hill)
    return hills


def select(id):
    hill = None
    sql = "SELECT FROM hills WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        hill = hill(result["name"], result["height"], result["area"], result["id"])
    return hill


def update(hill):
    sql = "UPDATE hills SET name = %s WHERE id = %s"
    values = [hill.name, hill.height, hill.area, hill.id]
    run_sql(sql, values)
    return


def delete(id):
    sql = "DELETE FROM hills WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    return


def delete_all():
    sql = "DELETE FROM hills"
    run_sql(sql)
