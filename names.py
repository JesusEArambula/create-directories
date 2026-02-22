# Split days
def split_days(option):
    return f"{option.split()[0]}/{option.split()[1]}"

# Cohort directory name
def cohort_directory_name(number, month, year, days):
    return f"(#{number} SPANISH) {days} {month} {year} Workshop 360 Valencia"

# Enrollment form name
def enrollment(number, month, year, days):
    return f"Cohort #{number} {split_days(days)} - Spanish Digital Literacy Enrollment Form {month} {year}"

# Agreement form name
def agreement(number, days):
    return f"Cohort #{number} - Spanish Basic Digital Literacy Agreement {split_days(days)}"

# Syllabus file name
def syllabus(number, days):
    return f"Cohort #{number} {split_days(days)} - Syllabus"

# Roster file name
def roster(number, month, year):
    return f"{month} {year} Cohort #{number} (SPANISH) 360 Valencia St Roster"

# Schedule file name
def schedule(number, month, year):
    return f"{month} {year} Cohort #{number} (SPANISH) 360 Valencia St Roster"

# File names based of cohort number, month, and year
def create_file_names(number, month, year, days):
    return [
            enrollment(number, month, year, days), 
            agreement(number, days), 
            syllabus(number, days), 
            roster(number, month, year),
            schedule(number, month, year)
            ]


