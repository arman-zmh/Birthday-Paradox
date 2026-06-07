import datetime, random

def getBirthdays(numberOfBirthdays):

    birthdays = []

    for i in range(numberOfBirthdays):

        startOfTheYear = datetime.date(2001,1,1)

        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfTheYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays
