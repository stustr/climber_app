from flask import Blueprint, redirect, render_template, request
import pdb

from models.hill import Hill
import repositories.hill_repository as hill_repo
import repositories.rating_repository as rating_repo

hills_blueprint = Blueprint("hills", __name__)

# index
@hills_blueprint.route("/hills")
def hills():
    args = request.args
    getargs = args.get("order_by")
    if getargs == None:
        hills = hill_repo.select_all()
        return render_template("hills/index.html", hills=hills)
    else: 
        hills = hill_repo.select_all(getargs)
        return render_template("hills/index.html", hills=hills)

# create
@hills_blueprint.route("/hills", methods=["POST"])
def create_hill():
    name = request.form["name"]
    height = request.form["height"]
    area = request.form["area"]
    new_hill = Hill(name, height, area)
    hill_repo.save(new_hill)
    return redirect("/hills")


# new
@hills_blueprint.route("/hills/new")
def new_hill():
    return render_template("hills/new.html")


# edit
@hills_blueprint.route("/hills/<id>/edit")
def edit_hill(id):
    hill = hill_repo.select(id)
    return render_template("/hills/edit.html", hill=hill)


# update
@hills_blueprint.route("/hills/<id>", methods=["POST"])
def update_hill(id):
    name = request.form["name"]
    height = request.form["height"]
    area = request.form["area"]
    hill = Hill(name, height, area, id)
    hill_repo.update(hill)
    return redirect("/hills")


# delete
@hills_blueprint.route("/hills/<id>/delete", methods=["POST"])
def delete_hill(id):
    hill_repo.delete(id)
    return redirect("/hills")


# show
@hills_blueprint.route("/hills/<id>")
def show_hill(id):
    hill = hill_repo.select_by_id(id)
    return render_template("/hills/show.html", hill=hill)
