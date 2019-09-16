class Characteristics:
    """The character's base characteristic scores.
    """

    def __init__(
        self,
        strength,
        dexterity,
        intelligence,
        constitution,
        apptitude,
        power,
        size,
        education,
        move_rate,
    ):
        """Initialization method. Stores the base character statistics.

        Args:
            strength (float): A whole number representing the character's base
                strength percentage score.
            dexterity (float): A whole number representing the character's base
                dexterity percentage score.
            intelligence (float): A whole number representing the character's
                base intelligence percentage score.
            constitution (float): A whole number representing the character's
                base constitution percentage score.
            apptitude (float): A whole number represesnting the character's
                base apptitude percentage score.
            power (float): A whole number representing the character's base
                power percentage score.
            size (float): A whole number representing the character's base size
                percentage score.
            education (float): A whole number representing the character's base
                education percentage score.
            move_rate (float): A whole number representing the character's base
                move rate percentage score.
         Return:
            A new set of base character characteristics.
        """
        self.strength = strength
        self.dexterity = dexterity
        self.inteligence = intelligence
        self.constitution = constitution
        self.apptitude = apptitude
        self.power = power
        self.size = size
        self.education = education
        self.move_rate = move_rate
