# Split days
def split_days(option):
    return f"{option.split()[0]}, {option.split()[1]}"

# Cohort number certificate directory name
def certificates_directory(num):
    return f"Cohort #{num} Certificates"

# Cohort directory name
def cohort_directory_name(number, month, year, days):
    return f"(#{number} SPANISH) {split_days(days)} {month} {year} Workshop 360 Valencia"

# Enrollment form name
def enrollment(number, month, year, days):
    return f"Cohort #{number} {split_days(days)} - Spanish Digital Literacy Enrollment Form {month} {year}.docx"

# Agreement form name
def agreement(number, days):
    return f"Cohort #{number} - Spanish Basic Digital Literacy Agreement {split_days(days)}.docx"

# Syllabus file name
def syllabus(number, days):
    return f"Cohort #{number} {split_days(days)} - Syllabus"

# Roster file name
def roster(number, month, year):
    return f"(#{number} Spanish) {month} {year} Cohort 360 Valencia St Roster.xlsx"

# Schedule file name
def schedule(number, month, year, days):
    return f"Dev_Mission Digital Literacy Schedule - {month} {year} #{number} ({split_days(days)}) (360 Valencia St Roster).xlsx"

# Report file name
def report(number, month, year):
    return f"Report Cohort #{number} - SBDL Summary Report {month} {year} (Cohort #{number}).docx"

# File names based of cohort number, month, and year
def create_file_names(number, month, year, days):
    return [
            enrollment(number, month, year, days), 
            agreement(number, days), 
            syllabus(number, days), 
            roster(number, month, year),
            schedule(number, month, year, days)
            ]


