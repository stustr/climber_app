from flask import Blueprint, redirect, render_template, request
from models.activity import Activity
from repositories import (
    activity_repository as activity_repo,
    climber_repository as climber_repo,
    hill_repository as hill_repo,
)

activities_blueprint = Blueprint("activities", __name__)

# index
@activities_blueprint.route("/activities")
def activities():
    activities = activity_repo.select_all()
    return render_template("activities/index.html", activities=activities)


# new
@activities_blueprint.route("/activites/new")
def new_activity():
    climbers = climber_repo.select_all()
    hills = hill_repo.select_all()
    return render_template("activities/new.html", climbers=climbers, hills=hills)


# create
@activities_blueprint.route("/activities", methods=["POST"])
def create_activity():
    climber_id = request.form["climber_id"]
    hill_id = request.form["hill_id"]
    name = request.form["name"]
    time = request.form["time"]
    description = request.form["description"]
    climber = climber_repo.select(climber_id)
    hill = hill_repo.select(hill_id)
    new_activity = Activity(name, time, description, climber, hill)
    activity_repo.save(new_activity)
    return redirect("/activities")


# edit
@activities_blueprint.route("/activities/<id>/edit")
def edit_activity(id):
    activity = activity_repo.select(id)
    climbers = climber_repo.select_all()
    hills = hill_repo.select_all()
    return render_template(
        "activities/edit.html", activity=activity, climbers=climbers, hills=hills
    )


# update
@activities_blueprint.route("/activities/<id>", methods=["POST"])
def update_activity(id):
    climber_id = request.form["climber_id"]
    hill_id = request.form["hill_id"]
    name = request.form["name"]
    time = request.form["time"]
    description = request.form["description"]
    climber = climber_repo.select(climber_id)
    hill = hill_repo.select(hill_id)
    updated_activity = Activity(name, time, description, climber, hill, id)
    activity_repo.update(updated_activity)


# delete
@activities_blueprint.route("/activities/<id>", methods=["POST"])
def delete_activity(id):
    activity_repo.delete(id)
    return redirect("/activities")
