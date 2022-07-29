class AgeError(Exception):
    pass


class HumanAgeError(AgeError):
    pass


class PlayerAgeError(AgeError):
    pass


class PlayerSalaryError(Exception):
    pass


class PlayerRateError(Exception):
    pass


class CoachAgeError(AgeError):
    pass


class CoachStartDateError(Exception):
    pass
