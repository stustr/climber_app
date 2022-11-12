from flask import Blueprint, redirect, render_template, request
from models.ascent import Ascent
from repositories import (
    ascent_repository as ascent_repo,
    climber_repository as climber_repo,
    hill_repository as hill_repo,
)

ascents_blueprint = Blueprint("ascents", __name__)

# index
@ascents_blueprint.route("/ascents")
def ascents():
    ascents = ascent_repo.select_all()
    climbers = climber_repo.select_all()
    all_time_summits = ascent_repo.climbing_comm_summits_alltime()
    all_time_heights = ascent_repo.climbing_comm_height_alltime()
    return render_template(
        "ascents/index.html",
        ascents=ascents,
        climbers=climbers,
        all_time_summits=all_time_summits, all_time_heights=all_time_heights
    )


# new
@ascents_blueprint.route("/ascents/new")
def new_ascent():
    climbers = climber_repo.select_all()
    hills = hill_repo.select_all()
    return render_template("ascents/new.html", climbers=climbers, hills=hills)


# create
@ascents_blueprint.route("/ascents", methods=["POST"])
def create_ascent():
    climber_id = request.form["climber_id"]
    hill_id = request.form["hill_id"]
    date = request.form["date"]
    description = request.form["description"]
    climber = climber_repo.select(climber_id)
    hill = hill_repo.select(hill_id)
    new_ascent = Ascent(date, description, climber, hill)
    ascent_repo.save(new_ascent)
    return redirect("/ascents")


# edit
@ascents_blueprint.route("/ascents/<id>/edit")
def edit_ascent(id):
    ascent = ascent_repo.select(id)
    climbers = climber_repo.select_all()
    hills = hill_repo.select_all()
    return render_template(
        "ascents/edit.html", ascent=ascent, climbers=climbers, hills=hills
    )


# update
@ascents_blueprint.route("/ascents/<id>", methods=["POST"])
def update_ascent(id):
    climber_id = request.form["climber_id"]
    hill_id = request.form["hill_id"]
    date = request.form["date"]
    description = request.form["description"]
    climber = climber_repo.select(climber_id)
    hill = hill_repo.select(hill_id)
    updated_ascent = Ascent(date, description, climber, hill, id)
    ascent_repo.update(updated_ascent)


# delete
@ascents_blueprint.route("/ascents/<id>/delete", methods=["POST"])
def delete_ascents(id):
    ascent_repo.delete(id)
    return redirect("/ascents")


# show
@ascents_blueprint.route("/ascents/<id>")
def show_ascents(id):
    ascent = ascent_repo.select(id)
    climbers = climber_repo.select_all()
    all_time_stats = ascent_repo.climbing_comm_stats_alltime()
    return render_template(
        "/ascents/show.html",
        ascent=ascent,
        climbers=climbers,
        all_time_stats=all_time_stats,
    )
