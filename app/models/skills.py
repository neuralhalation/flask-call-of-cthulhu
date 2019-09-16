from functions.difficulty_calculator import (calculate_hard_difficulty,
                                             calculate_extreme_difficulty)


class Skills:
    def __init__(self,
                 accounting=5,
                 anthropology=1,
                 appraise=5,
                 archeology=1,
                 arts_crafts=5,
                 charm=15,
                 climb=20,
                 credit_rating=0,
                 cthulu_mythos=0,
                 disguise=05,
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
        self.accounting = accounting
        self.anthropology = anthropology
        self.appraise = appraise
        self.archeology = archeology
        self.arts_crafts = arts_crafts
        self.charm = charm
        self.climb = climb
        self.credit_rating = credit_rating
        self.cthulu_mythos = cthulu_mythos
        self.disguise = disguise
        self.dodge = calculate_hard_difficulty(dodge)
        self.drive_auto = drive_auto
        self.electric_repair = electric_repair
        self.fast_talk = fast_talk
        self.fighting_brawl = fighting_brawl
        self.fighting_other = fighting_other
        self.firearms_handgun = firearms_handgun
        self.firearms_rifle = firearms_rifle
        self.first_aid = first_aid
        self.history = history
        self.intimidate = intimidate
        self.jump = jump
        self.language_other = language_other
        self.language_own = language_own
        self.law = law
        self.library_use = library_use
        self.listen = listen
        self.locksmith = locksmith
        self.mech_repair = mech_repair
        self.medicine = medicine
        self.natural_world = natural_world
        self.navigate = navigate
        self.occult = occult
        self.op_heavy_machinery = op_heavy_machinery
        self.persuade = persuade
        self.pilot = pilot
        self.psychology = psychology
        self.psychoanalysis = psychoanalysis
        self.ride = ride
        self.science = science
        self.sleight_of_hand = sleight_of_hand
        self.spot_hidden = spot_hidden
        self.stealth = stealth
        self.survival = survival
        self.swim = swim
        self.throw = throw
        self.track = track

    def hard_difficulty(skill):
        return calculate_hard_difficulty(skill)

    def extreme_difficulty(skill):
        return calculate_extreme_difficulty(skill)

    def skillsheet(self):
        skills = {}
        skill_list = [s for s in dir(self) if not callable(getattr(self, s))]
        for s in skill_list:
            skills[s]['normal'] = getattr(self, s)
            skills[s]['hard'] = calculate_hard_difficulty(getattr(self, s))
            skills[s]['extreme'] = calculate_extreme_difficulty(getattr(self, s))
