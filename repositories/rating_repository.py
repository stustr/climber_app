from db.run_sql import run_sql
from models.rating import Rating
from repositories import hill_repository as hill_repo

def save(rating): 
    sql = "INSERT INTO ratings (hill, score) VALUES (%s, %s) RETURNING id"
    values = [rating.hill.id, rating.score]
    results = run_sql(sql, values)
    id = results[0]["id"]
    rating.id = id
    return

def select_all():
    ratings = []
    sql = "SELECT * FROM ratings ORDER BY score DESC"
    results = run_sql(sql)
    for result in results:
        hill = hill_repo.select(result["hill_id"])
        rating = Rating(hill, result["score"])
        ratings.append(rating)
    return ratings

def select(id):
    sql = "SELECT * FROM ratings WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        hill = hill_repo.select(result["hill_id"])
        rating = Rating(hill, result["score"])
    return rating

def delete(id):
    sql = "DELETE FROM ratings WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    return


def delete_all():
    sql = "DELETE FROM ascents"
    run_sql(sql)
    return