from flask import Blueprint, Flask, render_template
from repositories import task_repository

tasks_blueprint = Blueprint("tasks", __name__)

#declare a route for the list of tasks
@tasks_blueprint.route("/tasks")
def tasks():
    tasks = task_repository.select_all()
    return render_template("tasks/index.html", all_tasks = tasks)

