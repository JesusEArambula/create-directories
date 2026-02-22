import message

# Take user input for cohort month
def enter_cohort_month():
    return str(input("Enter cohort month: ")).title()

# Tak user inpur for cohort year
def enter_cohort_year():
    return str(input("Enter cohort year: "))

# Take user input for count of cohorts to create
def enter_cohort_count():
    return int(input("Enter amount of cohorts: "))

# Take user input for cohort number
def enter_cohort_number():
    return str(input("Enter first Cohort number: "))

# Take user input for first cohort days
# 1) Mondays/Wednesdays
# 2) Tuesdays/Thursdays
def enter_cohort_days():
    message.day_options()
    return str(input("Enter cohort days: "))

# Take user input for cohort start date
def enter_cohort_start_date():
    return str(input("Enter cohort start date: "))

# Take user input for cohort end date
def enter_cohort_end_date():
    return str(input("Enter cohort end date: "))

