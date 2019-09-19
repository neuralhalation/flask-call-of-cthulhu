from flask import render_template
from app import app
from app.forms.character_sheet import BackstoryForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Lyon"}
    return render_template("main.html", title="Home", user=user)


@app.route("/backstory")
def new():
    sig_people = []
    meaningful_locations = []
    treasured_possessions = []
    traits = []
    injuries = []
    phobias = []
    arcane_items = []
    encounters = []

    def add_to_list(entry, old_list):
        new_list = old_list.__add__(entry)
        return new_list

    def add_significant_people():
        new_people = add_to_list({"name": "", "description": ""}, sig_people)
        form = BackstoryForm(significant_people=new_people)
        return render_template("backstory.html", form=form)

    form = BackstoryForm(
        significant_people=sig_people,
        meaningful_locations=meaningful_locations,
        treasured_possessions=treasured_possessions,
        traits=traits,
        injuries_and_scars=injuries,
        phobias_and_manias=phobias,
        arcane_items=arcane_items,
        encounters=encounters,
    )
    return render_template("backstory.html", form=form)

