import datetime, random

def getBirthdays(numberOfBirthdays):

    birthdays = []

    for i in range(numberOfBirthdays):

        startOfTheYear = datetime.date(2001,1,1)

        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfTheYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays
def getMatch(birthdays):

    if len(birthdays) ==len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthayB:
                return birthdayA
            
