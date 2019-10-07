from flask_wtf import FlaskForm
from wtforms import (
    FieldList,
    FormField,
    StringField,
    TextAreaField,
    SubmitField,
    IntegerField,
)
from wtforms.validators import DataRequired
import app.functions.difficulty_calculator as dc
from app.functions.key_formatter import format_from_name
from app.models.model_functions.with_fields import with_fields


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
    age = IntegerField("Age", validators=[DataRequired()])
    gender = StringField("Gender", validators=[DataRequired()])
    residence = StringField("Residence", validators=[DataRequired()])
    birthplace = StringField("Birthplace", validators=[DataRequired()])
    submit = SubmitField("Save Basic Information")


class CharacteristicsForm(FlaskForm):
    strength = with_fields("STR", 0)
    dexterity = with_fields("DEX", 0)
    intelligence = with_fields("INT", 0)
    constitution = with_fields("CON", 0)
    apptitude = with_fields("APP", 0)
    power = with_fields("POW", 0)
    size = with_fields("SIZ", 0)
    education = with_fields("EDU", 0)
    move_rate = IntegerField("Move Rate", 0)
    submit = SubmitField("Save Characteristics")


class SkillsForm(FlaskForm):
    accounting = with_fields("Accounting", 5)
    anthropology = with_fields("Anthropology", 1)
    appraise = with_fields("Appraise", 5)
    archeology = with_fields("Archeology", 1)
    arts_and_crafts = with_fields("Arts & Crafts", 5)
    charm = with_fields("Charm", 15)
    climb = with_fields("Climb", 20)
    credit_rating = with_fields("Credit Rating")
    cthulhu_mythos = with_fields("Cthulhu Mythos", 0)
    disguise = with_fields("Disguise", 5)
    dodge = {
        "dodge": {
            "base": IntegerField(
                "Base - Dodge", default=dc.calculate_hard_difficulty(0)
            )
        },
        "hard": IntegerField(
            "Hard - Dodge",
            default=dc.calculate_hard_difficulty(dc.calculate_hard_dificullty(0)),
        ),
        "extreme": IntegerField(
            "Extreme - Dodge",
            default=dc.calculate_extreme_difficulty(dc.calculate_hard_difficulty(0)),
        ),
    }
    drive_auto = with_fields("Drive Auto.", 20)
    electric_repair = with_fields("Electric Repair", 10)
    fast_talk = with_fields("Fast Talk", 5)
    fighting_brawl = with_fields("Fighting (Brawl)", 25)
    fighting_other = with_fields("Fighting (Other)", 0)
    firearms_handgun = with_fields("Firearms (Handgun)", 20)
    firearms_rifle = with_fields("Firearms (Rifle)", 25)
    first_aid = with_fields("First Aid", 30)
    history = with_fields("History", 5)
    intimidate = with_fields("Intimidate", 15)
    jump = with_fields("Jump", 20)
    language_other = with_fields("Language (Other)", 1)
    language_own = with_fields("Language (Own)", 0)
    law = with_fields("Law", 5)
    library_use = with_fields("Library Use", 20)
    listen = with_fields("Listen", 20)
    locksmith = with_fields("Locksmith", 1)
    mech_repair = with_fields("Mech. Repair", 10)
    medicine = with_fields("Medicine", 1)
    natural_world = with_fields("Natural World", 10)
    navigate = with_fields("Navigate", 10)
    occult = with_fields("Occult", 5)
    operate_heavy_machinery = with_fields("Operate Heavy Machinery", 1)
    persuade = with_fields("Persuade", 10)
    pilot = with_fields("Pilot", 1)
    psychoanalysis = with_fields("Psychoanalysis", 1)
    psychology = with_fields("Psychology", 10)
    ride = with_fields("Ride", 5)
    science = with_fields("Science", 1)
    sleight_of_hand = with_fields("Sleight of Hand", 10)
    spot_hidden = with_fields("Spot Hidden", 25)
    survival = with_fields("Survival", 10)
    swim = with_fields("Swim", 20)
    throw = with_fields("Throw", 20)
    track = with_fields("Track", 10)
