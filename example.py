import datetime

class Age:
    def __init__(self):
        pass

    def get_age(self, yob):
        """Calculate age using date of birth.
            Args:
                yob: The year of birth.
            Returns:
                age: indicates how old the person is.
            """
        year_today = datetime.datetime.today().year
        age = year_today-yob
        return yob


def calculate_bmi(weight, height):
    """Calculate body mass index.
        Args:
            wieght: in kilograms.
            height: in meters.
        Returns:
            bmi: body mass index.
    """
    bmi = weight/(height**2)
    return bmi


def main(yob, weight, height):
    """Generate the health credentials of a user based on input.
        Args:
            yob: The year of birth.
            wieght: in kilograms.
            height: in meters.
        Returns:
            age, bmi: as a dictionary.
    """
    ager = Age()
    credentials = dict(
        age=ager.get_age(yob),
        bmi=calculate_bmi(weight, height)
    )
    return credentials
