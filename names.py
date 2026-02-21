# Cohort directory name
def cohort_directory_name(number, month, year):
    return f"(#{number} SPANISH) Mon Wed {month} {year} Workshop 360 Valencia"

# Enrollment form name
def enrollment(number, month, year):
    return f"Cohort #{number} Mon/Wed - Spanish Digital Literacy Enrollment Form {month} {year}"

# Agreement form name
def agreement(number):
    return f"Cohort #{number} - Spanish Basic Digital Literacy Agreement Mon/Wed"

# Syllabus file name
def syllabus(number):
    return f"Cohort #{number} Mon/Wed - Syllabus"

# Roster file name
def roster(number, month, year):
    return f"{month} {year} Cohort #{number} (SPANISH) 360 Valencia St Roster"

# File names based of cohort number, month, and year
def create_file_names(number, month, year):
    return [
            enrollment(number, month, year), 
            agreement(number), 
            syllabus(number), 
            roster(number, month, year)
            ]


