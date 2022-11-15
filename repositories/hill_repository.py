from db.run_sql import run_sql
from models.hill import Hill
import pdb


def save(hill):
    sql = "INSERT INTO hills (name, height, area, image_path, route_link, weather_path) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [hill.name, hill.height, hill.area, hill.image_path, hill.route_link, hill.weather_path]
    results = run_sql(sql, values)
    id = results[0]["id"]
    hill.id = id
    return


def select_all(order_by="height"):
    hills = []
    if order_by == "height":
        sql = f"SELECT * FROM hills ORDER BY {order_by} DESC"
    else:
        sql = f"SELECT * FROM hills ORDER BY {order_by}"
    # values = [order_by]
    results = run_sql(sql)
    for result in results:
        hill = Hill(
            result["name"],
            result["height"],
            result["area"],
            result["image_path"],
            result["route_link"],
            result["weather_path"],
            result["id"],
        )
        hills.append(hill)
    return hills


def select_by_id(id):
    hill = None
    sql = "SELECT * FROM hills WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        hill = Hill(
            result["name"],
            result["height"],
            result["area"],
            result["image_path"],
            result["route_link"],
            result["weather_path"],
            result["id"],
        )
    return hill


def select_by_name(name):
    hill = None
    sql = "SELECT * FROM hills WHERE name = %s"
    values = [name]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        hill = Hill(
            result["name"],
            result["height"],
            result["area"],
            result["image_path"],
            result["route_link"],
            result["weather_path"],
            result["id"],
        )
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
