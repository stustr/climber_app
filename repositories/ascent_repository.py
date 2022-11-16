from db.run_sql import run_sql
from models.ascent import Ascent
from repositories import (
    climber_repository as climber_repo,
    hill_repository as hill_repo,
)
import pdb
import pandas
import july
from datetime import datetime, date
import matplotlib
from matplotlib import pyplot
import math


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
    sql = "SELECT * FROM ascents ORDER BY date DESC"
    results = run_sql(sql)

    for result in results:
        climber = climber_repo.select(result["climber_id"])
        hill = hill_repo.select_by_id(result["hill_id"])
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
        hill = hill_repo.select_by_id(result["hill_id"])
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


def monthly_heat():
    sql = "select CAST (date as varchar) from ascents where date >= (current_date - 30) and date <= current_date group by date, climber_id"
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
    july.heatmap(
        df[0],
        df[1],
        title="Monthly Activity",
        cmap=matplotlib.colors.LinearSegmentedColormap.from_list(
            "", ["#c8d3d5", "#9d9aa3", "#0cca4a"]
        ),
    ).get_tightbbox()
    pyplot.savefig(f"./static/images/agg_monthly_heat.png", bbox_inches="tight")
    pyplot.clf()
    pyplot.cla()
    pyplot.close()
    return

def total_climbing_height():
    sql = "SELECT hills.height, Count(*) AS climbs FROM ascents INNER JOIN hills ON ascents.hill_id = hills.id GROUP BY ascents.climber_id, ascents.hill_id, hills.height"
    values = [id]
    results = run_sql(sql, values)
    total = 0
    for result in results:
        hill_total = result[0] * result[1]
        total += hill_total
    return total