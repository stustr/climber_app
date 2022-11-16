from db.run_sql import run_sql
from models.climber import Climber
import math
import matplotlib
from matplotlib import pyplot
matplotlib.use("AGG")
from datetime import datetime, date
import pdb
import pandas
import july


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

def monthly_heat(id):
    sql = "select CAST (date as varchar) from ascents where date >= (current_date - 30) and date <= current_date and climber_id = %s group by date, climber_id"
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
    july.heatmap(df[0], df[1], title='Monthly Activity', cmap=matplotlib.colors.LinearSegmentedColormap.from_list("", ["#c8d3d5","#9d9aa3","#0cca4a"])).get_tightbbox()
    pyplot.savefig(f"./static/images/monthly_heat_{id}.png", bbox_inches="tight")
    pyplot.clf()
    pyplot.cla()
    pyplot.close()
    return


def greeting():
    today = datetime.today()
    hour = today.hour
    greeting = ""
    if hour >= 0 and hour < 12:
        greeting = "Morning"
    elif hour >= 12 and hour < 18:
        greeting = "Afternoon"
    else:
        greeting = "Evening"
    return greeting