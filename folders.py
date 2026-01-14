import os

# Take user input for cohort numbers, month, and cohort_year
cohort_number_1 = int(input("Enter first Cohort number: "))
cohort_number_2 = int(input("Enter second Cohort number: "))
cohort_month = str(input("Enter cohort month: "))
cohort_year = int(input("Enter cohort year: "))

# Root of cohort folder
# Change for every cohort number
cohort_folder_1 = f"(#{cohort_number_1} SPANISH) MonWed {cohort_month} {cohort_year} Workshop 360 Valencia"
cohort_folder_2 = f"(#{cohort_number_2} SPANISH) TueThu {cohort_month} {cohort_year} Workshop 360 Valencia"

# Forms Names
enrollment_form_1 = f"Cohort #{cohort_number_1} MonWed - Spanish Digital Literacy Enrollment Form {cohort_month} {cohort_year}"
enrollment_form_2 = f"Cohort #{cohort_number_2} TueThu - Spanish Digital Literacy Enrollment Form {cohort_month} {cohort_year}"
agreement_form_1 = f"Cohort #{cohort_number_1} - Spanish Basic Digital Literacy Agreement MonWed"
agreement_form_2 = f"Cohort #{cohort_number_2} - Spanish Basic Digital Literacy Agreement TueThu"
syllabus_1 = f"Cohort #{cohort_number_1} MonWed - Syllabus"
syllabus_2 = f"Cohort #{cohort_number_2} TueThu - Syllabus"
roster_1 = f"{cohort_month} {cohort_year} Cohort #{cohort_number_1} (SPANISH) 360 Valencia St Roster"
roster_2 = f"{cohort_month} {cohort_year} Cohort #{cohort_number_2} (SPANISH) 360 Valencia St Roster"


# Create the parent folder if it doesn't exist
os.makedirs(cohort_folder_1, exist_ok=True)
os.makedirs(cohort_folder_2, exist_ok=True)

sub_folders = ["Class Documents", "Files", "Flyer", "Report", "Schedule", "Roster"]

def create_path(cohort_folder, sub_folder):
    # Create paths for subfolder
    path_to_create = os.path.join(cohort_folder, sub_folder)
    os.makedirs(path_to_create, exist_ok=True)
    print(f"Folder '{path_to_create}' created successfully.")

# Create subfolders
for folder in sub_folders:
    create_path(cohort_folder_1, folder)
    create_path(cohort_folder_2, folder)




