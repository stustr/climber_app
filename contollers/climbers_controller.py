from flask import Blueprint, redirect, render_template, request

from models.climber import Climber
import repositories.climber_repository as climber_repo
import repositories.ascent_repository as ascent_repo
import repositories.hill_repository as hill_repo
from datetime import datetime

climbers_blueprint = Blueprint("climbers", __name__)

# index
@climbers_blueprint.route("/climbers")
def climbers():
    today = datetime.now()
    climbers = climber_repo.select_all()
    greeting = climber_repo.greeting()
    return render_template("climbers/index.html", climbers=climbers, greeting=greeting)


# create
@climbers_blueprint.route("/climbers", methods=["POST"])
def create_climber():
    name = request.form["name"]
    new_climber = Climber(name)
    climber_repo.save(new_climber)
    return redirect("/climbers")


# new
@climbers_blueprint.route("/climbers/new")
def new_climber():
    return render_template("climbers/new.html")


# edit
@climbers_blueprint.route("/climbers/<id>/edit")
def edit_climber(id):
    climber = climber_repo.select(id)
    return render_template("/climbers/edit.html", climber=climber)


# update
@climbers_blueprint.route("/climbers/<id>", methods=["POST"])
def update_climber(id):
    name = request.form["name"]
    climber = Climber(name, id)
    climber_repo.update(climber)
    return redirect("/climbers")


# delete
@climbers_blueprint.route("/climbers/<id>/delete", methods=["POST"])
def delete_climber(id):
    climber_repo.delete(id)
    return redirect("/climbers")


# show
@climbers_blueprint.route("/climbers/<id>")
def show_climber(id):
    climber = climber_repo.select(id)
    ascents = ascent_repo.select_all()
    climbs = ascent_repo.climbers_climbs(id)
    hills = hill_repo.select_all()
    total_m_climbed = climber_repo.total_climbing_height(id)
    percent_completed = climber_repo.amount_completed(id)
    climber_repo.monthly_heat(id)
    return render_template("/climbers/show.html", climber=climber, ascents=ascents, climbs=climbs, hills=hills, total_m_climbed=total_m_climbed, percent_completed=percent_completed)
