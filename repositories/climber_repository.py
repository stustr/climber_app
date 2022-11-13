from db.run_sql import run_sql
from models.climber import Climber
import math
from matplotlib import pyplot
from datetime import date
import pdb
import pandas


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
    return [len(climbs), math.ceil(len(climbs) / 222 * 100)]


def monthly_bar(id):
    sql = "select CAST (date as varchar) from ascents where date >= (current_date - 30) and date < current_date and climber_id = %s group by date, climber_id"
    values = [id]
    results = run_sql(sql, values)
    today = date.today()
    today_less_month = date.today().replace(month=today.month - 1)
    last_month = pandas.date_range(today_less_month, today)
    days = {}
    for day in last_month:
        days[day.strftime("%Y-%m-%d")] = 0
    for result in results:
        for day in days:
            if day == result[0]:
                days.update({day: 1})
    df = pandas.DataFrame(list(days.items()))
    fig = pyplot.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(df[0], df[1])
    pyplot.savefig("./static/images/monthly_plot.jpg")
    # pdb.set_trace()
    return
