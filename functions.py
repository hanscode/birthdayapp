from dateutil import relativedelta
import datetime

# This function is used to calculate the age of a person
# It takes a string as input, which is the birthdate of the person
# It returns the age of the person
def calculate_age(birthdate):
    format_string = "%Y-%m-%d"
    birthday_dt = datetime.datetime.strptime(birthdate, format_string)
    today = datetime.datetime.today()
    age = relativedelta.relativedelta(today, birthday_dt) # returns a relativedelta object e.g. relativedelta(years=0, months=0, days=0)
    return age

def upcoming_birthdays(people_list, days):
    # TODO: write code that finds all upcoming birthdays in the next 90 days
    # 90 is passed in as a parameter from menus.py
    # Template:
    # PERSON turns AGE in X days on MONTH DAY
    # PERSON turns AGE in X days on MONTH DAY
    #print("Upcoming Birthdays function")
    #print(people_list)
    #pass
    for person in people_list:
        format_string = "%Y-%m-%d"
        # birthday_dt represents the birthday of the person
        birthday_dt = datetime.datetime.strptime(person['birthday'], format_string)
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

    format_string = "%Y-%m-%d"
    p0_dt = datetime.datetime.strptime(people[0]['birthday'], format_string)
    p1_dt = datetime.datetime.strptime(people[1]['birthday'], format_string)

    if p0_dt < p1_dt:
        difference = relativedelta.relativedelta(p1_dt, p0_dt)
        print(f"{people[0]['name']} is older")
    else:
        difference = relativedelta.relativedelta(p0_dt, p1_dt)
        print(f"{people[1]['name']} is older")
    
    #print(difference)

    print(f"{people[0]['name']} and {people[1]['name']}'s age difference is: {difference.years} years, {difference.months} months, and {difference.days} days ")
    #print(people)
    #pass
