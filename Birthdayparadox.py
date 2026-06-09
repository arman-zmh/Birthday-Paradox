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
            
print('''Birthday Paradox, by Arman-zmh

The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large. ''')

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True: 
    print('How many birthdays shall I generate? (Max 100)')

    respone = input('> ')
    if respone.isdecimal() and ( 0 < int(respone) =< 100):
        numBDays = int(respone)
        break

print('Here are', numBDays, 'birthdays:')

birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')

    monthName = MONTHS(birthday.month - 1)
    dateText = '{} {}'.format(monthName, birthday.day)

    print(dateText, end='')

print()

match = getMatch(birthdays)

print('In this simulation, ', end='')

