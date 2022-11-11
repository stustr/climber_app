from db.run_sql import run_sql
from models.activity import Activity

def save(activity):
    sql = "INSERT INTO activities (name, )"