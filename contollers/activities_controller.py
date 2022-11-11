from flask import Blueprint, redirect, render_template
from models.activity import Activity
import repositories.activity_repository as activity_repo

activities_controller = Blueprint('activities', __name__)

# index
@activities_controller.route('/activities')
def activities():
    activities = activity_repo