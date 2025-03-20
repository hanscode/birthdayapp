from dateutil import relativedelta
import datetime

# Helper function to parse the date string into a datetime object
# It takes a string as input, which is the birthdate of the person
# It returns a datetime object
def date_parsing(birthdate):
    date = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
    return date

# This function is used to calculate the age of a person
# It takes a string as input, which is the birthdate of the person
# It returns the age of the person
def calculate_age(birthdate):
    birthday_dt = date_parsing(birthdate)
    today = datetime.datetime.today()
    age = relativedelta.relativedelta(today, birthday_dt) # returns a relativedelta object e.g. relativedelta(years=0, months=0, days=0)
    return age

def upcoming_birthdays(people_list, days):
    # TODO: write code that finds all upcoming birthdays in the next 90 days
    # 90 is passed in as a parameter from menus.py
    # Template:
    # PERSON turns AGE in X days on MONTH DAY
    # PERSON turns AGE in X days on MONTH DAY
    for person in people_list:
        # birthday_dt represents the birthday of the person
        birthday_dt = date_parsing(person['birthday'])
        now = datetime.datetime.now()

        birthday_this_year =birthday_dt.replace(year=now.year)
        difference = birthday_this_year - now

        age_now = calculate_age(person['birthday'])
        turning_age = age_now.years + 1

        if 0 < difference.days < days:
            print(f"{person['name']} turns {turning_age} in {difference.days} days on {birthday_dt.strftime('%B %d')}")

def display_age(person):
    # TODO: write the code to display the age of a person
    # Template:
    # PERSON is X years, X months, and X days old
    #print("Display Age function")
    
    #  age variable is a relativedelta object and contains years, months, days. It uses the calculate_age function.
    age = calculate_age(person['birthday'])
    #print age variable
    #print(age)
    # print the age of the person using the format string, e.g. "John is 25 years, 3 months, and 2 days old"
    print(f"{person['name']} is {age.years} years, {age.months} months, and {age.days} days old")


def display_age_difference(people):
    # TODO: write the code to display the age difference between people
    # Template:
    # PERSON is older
    # PERSON and PERSON's age difference is: X years, X months, and X days

    p0_dt = date_parsing(people[0]['birthday'])
    p1_dt = date_parsing(people[1]['birthday'])

    if p0_dt < p1_dt:
        difference = relativedelta.relativedelta(p1_dt, p0_dt)
        print(f"{people[0]['name']} is older")
    else:
        difference = relativedelta.relativedelta(p0_dt, p1_dt)
        print(f"{people[1]['name']} is older")

    print(f"{people[0]['name']} and {people[1]['name']}'s age difference is: {difference.years} years, {difference.months} months, and {difference.days} days ")

