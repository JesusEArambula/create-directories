# Enrollment form name
def enrollment(number, month, year):
    return f"Cohort #{number} MonWed - Spanish Digital Literacy Enrollment Form {month} {year}"
# Agreement form name
def agreement(number):
    return f"Cohort #{number} - Spanish Basic Digital Literacy Agreement MonWed"
# Syllabus file name
def syllabus(number):
    return f"Cohort #{number} MonWed - Syllabus"
# Roster file name
def roster(number, month, year):
    return f"{month} {year} Cohort #{number} (SPANISH) 360 Valencia St Roster"

def create_file_names(number, month, year):
    return [
            enrollment(number, month, year), 
            agreement(number), 
            syllabus(number), 
            roster(number, month, year)
            ]

# Forms Names
# enrollment_form_1 = f"Cohort #{cohort_number_1} MonWed - Spanish Digital Literacy Enrollment Form {cohort_month} {cohort_year}"
# enrollment_form_2 = f"Cohort #{cohort_number_2} TueThu - Spanish Digital Literacy Enrollment Form {cohort_month} {cohort_year}"
# agreement_form_1 = f"Cohort #{cohort_number_1} - Spanish Basic Digital Literacy Agreement MonWed"
# agreement_form_2 = f"Cohort #{cohort_number_2} - Spanish Basic Digital Literacy Agreement TueThu"
# syllabus_1 = f"Cohort #{cohort_number_1} MonWed - Syllabus"
# syllabus_2 = f"Cohort #{cohort_number_2} TueThu - Syllabus"
# roster_1 = f"{cohort_month} {cohort_year} Cohort #{cohort_number_1} (SPANISH) 360 Valencia St Roster"
# roster_2 = f"{cohort_month} {cohort_year} Cohort #{cohort_number_2} (SPANISH) 360 Valencia St Roster"
