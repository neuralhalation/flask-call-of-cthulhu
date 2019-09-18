from app.functions.difficulty_calculator import (
    calculate_extreme_difficulty,
    calculate_hard_difficulty,
)


def build_skillsheet(
    accounting=5,
    anthropology=1,
    appraise=5,
    archeology=1,
    arts_crafts=5,
    charm=15,
    climb=20,
    credit_rating=0,
    cthulu_mythos=0,
    disguise=5,
    dodge=0,
    drive_auto=20,
    electric_repair=10,
    fast_talk=5,
    fighting_brawl=25,
    fighting_other=0,
    firearms_handgun=20,
    firearms_rifle=25,
    first_aid=30,
    history=5,
    intimidate=15,
    jump=20,
    language_other=1,
    language_own=0,
    law=5,
    library_use=20,
    listen=20,
    locksmith=1,
    mech_repair=10,
    medicine=1,
    natural_world=10,
    navigate=10,
    occult=5,
    op_heavy_machinery=1,
    persuade=10,
    pilot=1,
    psychology=10,
    psychoanalysis=1,
    ride=5,
    science=1,
    sleight_of_hand=10,
    spot_hidden=25,
    stealth=20,
    survival=10,
    swim=20,
    throw=20,
    track=10,
):
    """Builds the skill list with difficulties for a character.

    Args:
        accounting (int): The whole number representing the percentile
        accounting score.
        anthropology (int): The whole number representing the percentile
        anthropology score.
        appraise (int): The whole number representing the percentile
        appraise score.
        archeology (int): The whole number representing the percentile
        archeology score.
        arts_crafts (int): The whole number representing the percentile
        arts and crafts score.
        charm (int): The whole number representing the percentile charm score.
        climb (int): The whole number representing the percentile climb score.
        credit_rating (int): The whole number representing the percentile
        credit rating.
        cthulhu_mythos (int): The whole number representing the percentile
        Cthulhu Mythos score.
        disguise (int): The whole number representing the percentile
        disguise score.
        dodge (int): The dodge score.
        drive_auto (int): The whole number representing the percentile
        drive automobile score.
        electric_repair (int): The whole number representing the percentile
        electric repair score.
        fast_talk (int): The whole number representing the percentile fast
        talk score.
        fighting_brawl (int): The whole number representing the percentile
        fighting (brawl) score.
        fighting_other (int): The whole number representing the percentile
        fighting (other) score.
        firearms_handgun (int): The whole number representing the percentile
        firearms (handgun) score.
        firearms_rifle (int): The whole number representing the percentile
        firearms (rifle) score.
        first_aid (int): The whole number representing the percentile first
        aid score.
        history (int): The whole number representing the percentile history
        score.
        intimidate (int): The whole number representing the percentile
        history score.
        jump (int): The whole number representing the percentile jump score.
        language_other (int): The whole number representing the percentile
        language (other) score.
        language_other (int): The whole number representing the percentile
        language (other) score.
        law (int): The whole number representing the percentile law score.
        library_use (int): The whole number representing the percentile
        library use score.
        listen (int): The whole number representing the percentile listen
        score.
        locksmith (int): The whole number representing the percentile
        locksmith score.
        mech_repair (int): The whole number representing the percentile
        mechanical repair score.
        medicine (int): The whole number representing the percentile medicine
        score.
        natural_world (int): The whole number representing the percentile
        natural world score.
        navigate (int): The whole number representing the percentile navigate
        score.
        occult (int): The whole number representing the percentile occult
        score.
        op_heavy_machinery (int): The whole number representing the percentile
        operate heavy machinery score.
        persuade (int): The whole number representing the percentile persuade
        score.
        pilot (int): The whole number representing the percentile pilot score.
        psychology (int): The whole number representing the percentile
        psychology score.
        psychoanalysis (int): The whole number representing the percentile
        psychoanalysis score.
        ride (int): The whole number representing the percentile ride score.
        science (int): The whole number representing the percentile science
        score.
        sleight_of_hand (int): The whole number representing the percentile
        sleight of hand score.
        spot_hidden (int): The whole number representing the percentile spot
        hidden score.
        stealth (int): The whole number representing the percentile stealth
        score.
        survival (int): The whole number representing the percentile survival
        score.
        swim (int): The whole number representing the percentile swim score.
        throw (int): The whole number representing the percentile throw score.
        track (int): The whole number representing the percentile track score.

    Return:
        dict: A character's skills with calculated difficulty.
    """
    return {
        "accounting": {
            "normal": accounting,
            "hard": calculate_hard_difficulty(accounting),
            "extreme": calculate_extreme_difficulty(accounting),
        },
        "anthropology": {
            "normal": anthropology,
            "hard": calculate_hard_difficulty(anthropology),
            "extreme": calculate_extreme_difficulty(anthropology),
        },
        "appraise": {
            "normal": appraise,
            "hard": calculate_hard_difficulty(appraise),
            "extreme": calculate_extreme_difficulty(appraise),
        },
        "archeology": {
            "normal": archeology,
            "hard": calculate_hard_difficulty(archeology),
            "extreme": calculate_extreme_difficulty(archeology),
        },
        "arts_crafts": {
            "normal": arts_crafts,
            "hard": calculate_hard_difficulty(arts_crafts),
            "extreme": calculate_extreme_difficulty(arts_crafts),
        },
        "charm": {
            "normal": charm,
            "hard": calculate_hard_difficulty(charm),
            "extreme": calculate_extreme_difficulty(charm),
        },
        "climb": {
            "normal": climb,
            "hard": calculate_hard_difficulty(climb),
            "extreme": calculate_extreme_difficulty(climb),
        },
        "credit_rating": credit_rating,
        "cthulu_mythos": {
            "normal": cthulu_mythos,
            "hard": calculate_hard_difficulty(cthulu_mythos),
            "extreme": calculate_extreme_difficulty(cthulu_mythos),
        },
        "disguise": {
            "normal": disguise,
            "hard": calculate_hard_difficulty(disguise),
            "extreme": calculate_extreme_difficulty(disguise),
        },
        "dodge": calculate_hard_difficulty(dodge),
        "drive_auto": {
            "normal": drive_auto,
            "hard": calculate_hard_difficulty(drive_auto),
            "extreme": calculate_extreme_difficulty(drive_auto),
        },
        "electric_repair": {
            "normal": electric_repair,
            "hard": calculate_hard_difficulty(electric_repair),
            "extreme": calculate_extreme_difficulty(electric_repair),
        },
        "fast_talk": {
            "normal": fast_talk,
            "hard": calculate_hard_difficulty(fast_talk),
            "extreme": calculate_extreme_difficulty(fast_talk),
        },
        "fighting_brawl": {
            "normal": fighting_brawl,
            "hard": calculate_hard_difficulty(fighting_brawl),
            "extreme": calculate_extreme_difficulty(fighting_brawl),
        },
        "fighting_other": {
            "normal": fighting_other,
            "hard": calculate_hard_difficulty(fighting_other),
            "extreme": calculate_extreme_difficulty(fighting_other),
        },
        "firearms_handgun": {
            "normal": firearms_handgun,
            "hard": calculate_hard_difficulty(firearms_handgun),
            "extreme": calculate_extreme_difficulty(firearms_handgun),
        },
        "firearms_rifle": {
            "normal": firearms_rifle,
            "hard": calculate_hard_difficulty(firearms_rifle),
            "extreme": calculate_extreme_difficulty(firearms_rifle),
        },
        "first_aid": {
            "normal": first_aid,
            "hard": calculate_hard_difficulty(first_aid),
            "extreme": calculate_extreme_difficulty(first_aid),
        },
        "history": {
            "normal": history,
            "hard": calculate_hard_difficulty(history),
            "extreme": calculate_extreme_difficulty(history),
        },
        "intimidate": {
            "normal": intimidate,
            "hard": calculate_hard_difficulty(intimidate),
            "extreme": calculate_extreme_difficulty(intimidate),
        },
        "jump": {
            "normal": jump,
            "hard": calculate_hard_difficulty(jump),
            "extreme": calculate_extreme_difficulty(jump),
        },
        "language_other": {
            "normal": language_other,
            "hard": calculate_hard_difficulty(language_other),
            "extreme": calculate_extreme_difficulty(language_other),
        },
        "language_own": {
            "normal": language_own,
            "hard": calculate_hard_difficulty(language_own),
            "extreme": calculate_extreme_difficulty(language_own),
        },
        "law": {
            "normal": law,
            "hard": calculate_hard_difficulty(law),
            "extreme": calculate_extreme_difficulty(law),
        },
        "library_use": {
            "normal": library_use,
            "hard": calculate_hard_difficulty(library_use),
            "extreme": calculate_extreme_difficulty(library_use),
        },
        "listen": {
            "normal": listen,
            "hard": calculate_hard_difficulty(listen),
            "extreme": calculate_extreme_difficulty(listen),
        },
        "locksmith": {
            "normal": locksmith,
            "hard": calculate_hard_difficulty(locksmith),
            "extreme": calculate_extreme_difficulty(locksmith),
        },
        "mech_repair": {
            "normal": mech_repair,
            "hard": calculate_hard_difficulty(mech_repair),
            "extreme": calculate_extreme_difficulty(mech_repair),
        },
        "medicine": {
            "normal": medicine,
            "hard": calculate_hard_difficulty(medicine),
            "extreme": calculate_extreme_difficulty(medicine),
        },
        "natural_world": {
            "normal": natural_world,
            "hard": calculate_hard_difficulty(natural_world),
            "extreme": calculate_extreme_difficulty(natural_world),
        },
        "navigate": {
            "normal": navigate,
            "hard": calculate_hard_difficulty(navigate),
            "extreme": calculate_extreme_difficulty(navigate),
        },
        "occult": {
            "normal": occult,
            "hard": calculate_hard_difficulty(occult),
            "extreme": calculate_extreme_difficulty(occult),
        },
        "op_heavy_machinery": {
            "normal": op_heavy_machinery,
            "hard": calculate_hard_difficulty(op_heavy_machinery),
            "extreme": calculate_extreme_difficulty(op_heavy_machinery),
        },
        "persuade": {
            "normal": persuade,
            "hard": calculate_hard_difficulty(persuade),
            "extreme": calculate_extreme_difficulty(persuade),
        },
        "pilot": {
            "normal": pilot,
            "hard": calculate_hard_difficulty(pilot),
            "extreme": calculate_extreme_difficulty(pilot),
        },
        "psychology": {
            "normal": psychology,
            "hard": calculate_hard_difficulty(psychology),
            "extreme": calculate_extreme_difficulty(psychology),
        },
        "psychoanalysis": {
            "normal": psychoanalysis,
            "hard": calculate_hard_difficulty(psychoanalysis),
            "extreme": calculate_extreme_difficulty(psychoanalysis),
        },
        "ride": {
            "normal": ride,
            "hard": calculate_hard_difficulty(ride),
            "extreme": calculate_extreme_difficulty(ride),
        },
        "science": {
            "normal": science,
            "hard": calculate_hard_difficulty(science),
            "extreme": calculate_extreme_difficulty(science),
        },
        "sleight_of_hand": {
            "normal": sleight_of_hand,
            "hard": calculate_hard_difficulty(sleight_of_hand),
            "extreme": calculate_extreme_difficulty(sleight_of_hand),
        },
        "spot_hidden": {
            "normal": spot_hidden,
            "hard": calculate_hard_difficulty(spot_hidden),
            "extreme": calculate_extreme_difficulty(spot_hidden),
        },
        "stealth": {
            "normal": stealth,
            "hard": calculate_hard_difficulty(stealth),
            "extreme": calculate_extreme_difficulty(stealth),
        },
        "survival": {
            "normal": survival,
            "hard": calculate_hard_difficulty(survival),
            "extreme": calculate_extreme_difficulty(survival),
        },
        "swim": {
            "normal": swim,
            "hard": calculate_hard_difficulty(swim),
            "extreme": calculate_extreme_difficulty(swim),
        },
        "throw": {
            "normal": throw,
            "hard": calculate_hard_difficulty(throw),
            "extreme": calculate_extreme_difficulty(throw),
        },
        "track": {
            "normal": track,
            "hard": calculate_hard_difficulty(track),
            "extreme": calculate_extreme_difficulty(track),
        },
    }
