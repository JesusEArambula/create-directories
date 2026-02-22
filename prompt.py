import message

# Take user input for cohort month
def enter_cohort_month():
    return str(input("Enter cohort month: "))

# Tak user inpur for cohort year
def enter_cohort_year():
    return int(input("Enter cohort year: "))

# Take user input for count of cohorts to create
def enter_cohort_count():
    return int(input("Enter amount of cohorts: "))

# Take user input for cohort number
def enter_cohort_number():
    return int(input("Enter first Cohort number: "))

# Take user input for first cohort days
# 1) Mondays/Wednesdays
# 2) Tuesdays/Thursdays
def cohort_days():
    print(message.day_options())
    return int(input("Enter cohort days: "))

# Take user input for cohort start date
def cohort_start_date():
    return int(input("Enter cohort start date: "))

def cohort_end_date():
    return int(input("Enter cohort end date: "))

