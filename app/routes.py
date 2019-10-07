from flask import render_template, flash, redirect
from app import app
from app.forms.character_sheet import BaseInfoForm, CharacteristicsForm


@app.route("/")
@app.route("/index")
def index():
    return render_template("main.html", title="Home")


@app.route("/base-info")
def base_info():
    form = BaseInfoForm()
    if form.validate_on_submit():
        flash(f"Time to roll for characteristics, {form.character_name}.")
        return redirect("/characteristics")
    return render_template("base_info.html", form=form, title="Basic Info")


@app.route("/characteristics")
def characteristics():
    form = CharacteristicsForm()
    if form.validate_on_submit():
        flash(f"Pray to the elder gods your stats are accurate.")
        return redirect("/skills")
    return render_template("characteristics.html", form=form, title="Characteristics")
