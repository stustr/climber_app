from flask import Blueprint, redirect, render_template, request

from models.climber import Climber
import repositories.climber_repository as climber_repo

climbers_blueprint = Blueprint("climbers", __name__)

# index
@climbers_blueprint.route("/climbers")
def climbers():
    climbers = climber_repo.select_all()
    return render_template("climber/index.html", climbers=climbers)


# create
@climbers_blueprint.route("/climbers", methods=["POST"])
def create_climber():
    name = request.form["name"]
    new_climber = Climber(name)
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
@climbers_blueprint.route("climbers/<id>/delete", methods=["POST"])
def delete_climber(id):
    climber_repo.delete(id)
    return redirect("/climbers")
