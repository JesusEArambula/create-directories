import prompt, names, directories, cohort, message, shutil, os, dates, string, open_files
from cohort import Cohort
from datetime import date
from operator import methodcaller

# List of subdifectories to create for each cohort folder
subdirectories = ["Class Documents", "Files", "Flyer", "Report", "Schedule", "Roster"]
# The Files subdirectory contains its own list of subdirectories
files_subdirectories = ["Attendance Agreement", "Enrollment Form", "Laptop Waiver", "Sign-in Sheets"]

# Dictionary to choose day options
# 1) Monday/Wednesday
# 2) Tuesday/Thursday
day_options = {1: "Mon Wed", 2: "Tue Thu"}

# List to store cohorts' information
cohort_list = []

# Get user input for month and year
# Both will be used to create any cohorts created
month = prompt.enter_cohort_month()
year = prompt.enter_cohort_year()
count = prompt.enter_cohort_count()

# Loop to create cohort objects
for i in range(count):
    # Print out Cohort Number Banner divider
    message.info_banner(i)

    # Get user cohort information
    num = prompt.enter_cohort_number()
    option = prompt.enter_cohort_days()
    start = prompt.enter_cohort_start_date()
    end = prompt.enter_cohort_end_date()

    # Create a start and end date format 
    start_date = date(int(year), int(start.split('/')[0]), int(start.split('/')[1]))
    end_date = date(int(year), int(end.split('/')[0]), int(end.split('/')[1]))

    # Create a list of the cohorts dates
    dates_list = dates.get_dates(start_date, end_date)
    print(dates_list)
    
    # Add cohort certificates name for Files' subdirectory
    files_subdirectories.append(names.certificates_directory(num))
    
    # Root of cohort folder
    # Change for every cohort number
    directory = names.cohort_directory_name(num, month, year, day_options[option])
    
    # Create the parent cohort folder if it doesn't already exist
    directories.create_directory(directory)
    
    # Create enrollment, agreement, syllabus, and roster files
    # based on user cohort number, month, and year input
    files = names.create_file_names(num, month, year, day_options[option])
    
    # Debuggin for loop
    # Display all files created for cohort
    for file in files:
        print("File Created: " + file)
    # Create paths to sub directories
    directories.create_path(directory, subdirectories, files_subdirectories)
    # Remove the previous cohort Files subdirectory
    files_subdirectories.pop()

    # Change directory to /class document
    # To loop through each file and copy it 
    # to the cohort parents directory 
    # and its subdirectories
    os.chdir('class documents')

    # Get the list of files
    documents_list = os.listdir()
    # Loop through each file
    for document in documents_list:
        # Copy the file to their respective locations based on its name
        # and give the new copied file a new name
        if document == 'roster.xlsx':
            # Roster subdirectory
            shutil.copyfile(document, f"../{directory}/{subdirectories[5]}/{names.roster(num, month, year)}")
        elif document == 'schedule.xlsx':
            # Schedule subdirectory
            shutil.copyfile(document, f"../{directory}/{subdirectories[4]}/{names.schedule(num, month, year, day_options[option])}")
        elif document == 'report.docx':
            # Report subdirectory
            shutil.copyfile(document, f"../{directory}/{subdirectories[3]}/{names.report(num, month, year)}")  
        elif document == 'flyer.jpg':
            # Flyer subdirectory
            shutil.copyfile(document, f"../{directory}/{subdirectories[2]}/{string.capwords(document)}")
        elif document == 'certificate.docx':
            # Certificates subdirectory
            shutil.copyfile(document, f"../{directory}/{subdirectories[1]}/{names.certificates_directory(num)}/{document}")
        else:
            # Any other file goes in the Class Documents subdirectory
            shutil.copyfile(document, f"../{directory}/{subdirectories[0]}/Cohort #{num} {string.capwords(document)}")

    # Change between Mon/Wed and Tue/Thu
    if option == 1:
        workshop_days_spanish = ["Lunes", "Miercoles"]
        workshop_days_english = ["Mon", "Wed"]
    else:
        workshop_days_spanish = ["Martes", "Jueves"]
        workshop_days_english = ["Tue", "Thu"]

    
    # Determine season of the cohort
    if start_date >= date(int(year), 1, 1) and start_date <= date(int(year), 4, 30):
        cohort_season = "Spring"
    if start_date >= date(int(year), 5, 1) and start_date <= date(int(year), 8, 31):
        cohort_season = "Summer"
    if start_date >= date(int(year), 9, 1) and start_date <= date(int(year), 12, 31):
        cohort_season = "Fall"

    # Dictionary for replacement values
    replacements = {
        "{Day1}": workshop_days_spanish[0],
        "{Day2}": workshop_days_spanish[1],
        "{Season}": cohort_season,
        "{Date1}": dates_list[0],
        "{Date2}": dates_list[1],
        "{Date3}": dates_list[2],
        "{Date4}": dates_list[3],
        "{Date5}": dates_list[4],
        "{Date6}": dates_list[5],
        "{Date7}": dates_list[6],
        "{Date8}": dates_list[7],
        "{Month}": month,
        "{Year}": year,        
        "{Start}": start,
        "{End}": end,
        "{Num}": num
        }

    # Return to /create-directories folder 
    # and move to /Class Documents subdirectory
    # Loop through each file in the subdirectory
    # and replace all the needed text in the docx files
    os.chdir(f"../{directory}/{subdirectories[0]}")
    documents_list = os.listdir()
    for document in documents_list:
        open_files.replace_text_in_docx(document, document, replacements)
    
    # Move to the /Report subdirectory
    # and replace all needed text in the "Schedule" xlsx file
    os.chdir(f"../{subdirectories[3]}")
    documents_list = os.listdir()
    for document in documents_list:
        open_files.replace_text_in_docx(document, document, replacements)

    # Move to the /Roster subdirectory
    # and replace all needed text in the "Schedule" xlsx file
    os.chdir(f"../{subdirectories[5]}")
    documents_list = os.listdir()
    for document in documents_list:
        open_files.replace_text_in_excel(document, document, replacements)
    
    # Move to the /Schedule subdirectory
    # and replace all needed text in the "Schedule" xlsx file
    os.chdir(f"../{subdirectories[4]}")
    documents_list = os.listdir()
    for document in documents_list:
        open_files.replace_text_in_excel(document, document, replacements)

    # Move to the /Files/Cohort # Certificates subdirectory
    # and replace all needed text in the "Schedule" xlsx file
    os.chdir(f"../{subdirectories[1]}/Cohort #{num} Certificates")
    documents_list = os.listdir()
    for document in documents_list:
        open_files.replace_text_in_docx(document, document, replacements)

    # Return to "create-directories" folder
    os.chdir("../../../")

results = list(map(methodcaller('get_directory'), cohort_list))
print(results)
