from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class SignificantPeopleEntryForm(FlaskForm):
    significant_person = StringField("Significant Person")
    description = StringField("Description")


class MeaningfulLocationsEntryForm(FlaskForm):
    location = StringField("Location")
    description = TextAreaField("Description")


class TreasuredPossessionsEntryForm(FlaskForm):
    possession = StringField("Name")
    description = TextAreaField("Description")


class TraitsEntryForm(FlaskForm):
    name = StringField("Name")
    description = TextAreaField("Description")


class InjuriesAndScarsEntryForm(FlaskForm):
    injury_or_scar = TextAreaField("Injuries/Scars")


class PhobiasAndManiasEntryForm(FlaskForm):
    phobia_or_mania = StringField("Phobia/Mania")
    description = TextAreaField("Description")


class ArcaneTomesSpellsArtifactsEntryForm(FlaskForm):
    arcane_item = StringField("Tome/Spell/Artifact Name")
    description = TextAreaField("Description")


class EncountersEntryForm(FlaskForm):
    encounter = TextAreaField("Encounter")


class BackstoryForm(FlaskForm):
    personal_description = TextAreaField("Description", validators=[DataRequired()])
    ideology_beliefs = TextAreaField("Ideology/Beliefs", validators=[DataRequired()])
    significant_people = FieldList(FormField(SignificantPeopleEntryForm), min_entries=0)
    meaningful_locations = FieldList(
        FormField(MeaningfulLocationsEntryForm), min_entries=0
    )
    treasured_possessions = FieldList(
        FormField(TreasuredPossessionsEntryForm), min_entries=0
    )
    traits = FieldList(FormField(TraitsEntryForm), min_entries=0)
    injuries_and_scars = FieldList(FormField(InjuriesAndScarsEntryForm), min_entries=0)
    phobias_and_manias = FieldList(FormField(PhobiasAndManiasEntryForm), min_entries=0)
    arcane_items = FieldList(
        FormField(ArcaneTomesSpellsArtifactsEntryForm), min_entries=0
    )
    encounters = FieldList(FormField(EncountersEntryForm), min_entries=0)


class BaseInfoForm(FlaskForm):
    character_name = StringField("Character Name", validators=[DataRequired()])
    player_name = StringField("Player Name", validators=[DataRequired()])
    occupation = StringField("Occupation", validators=[DataRequired()])
    age = StringField("Age", validators=[DataRequired()])
    gender = StringField("Gender", validators=[DataRequired()])
    residence = StringField("Residence", validators=[DataRequired()])
    birthplace = StringField("Birthplace", validators=[DataRequired()])
