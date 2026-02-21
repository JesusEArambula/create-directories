import os, prompts, names

# Function to create paths to subfolder
def create_path(cohort_folder, sub_folder):
    # Create paths for subfolder
    path_to_create = os.path.join(cohort_folder, sub_folder)
    os.makedirs(path_to_create, exist_ok=True)
    print(f"Folder '{path_to_create}' created successfully.")


# List of subfolder to create for each cohort folder
sub_folders = ["Class Documents", "Files", "Flyer", "Report", "Schedule", "Roster"]

# Get user input for the cohort numbers, month, and year
cohort_number_1 = prompts.enter_cohort_1()
cohort_number_2 = prompts.enter_cohort_2()
cohort_month = prompts.enter_cohort_month()
cohort_year = prompts.enter_cohort_year()

# Create enrollment, agreement, syllabus, and roster files
# based on user cohort number, month, and year input
cohort_1_files = names.create_file_names(cohort_number_1, cohort_month, cohort_year)
cohort_2_files = names.create_file_names(cohort_number_2, cohort_month, cohort_year)

# Root of cohort folder
# Change for every cohort number
cohort_folder_1 = f"(#{cohort_number_1} SPANISH) MonWed {cohort_month} {cohort_year} Workshop 360 Valencia"
cohort_folder_2 = f"(#{cohort_number_2} SPANISH) TueThu {cohort_month} {cohort_year} Workshop 360 Valencia"

# Create the parent folder if it doesn't already xist
os.makedirs(cohort_folder_1, exist_ok=True)
os.makedirs(cohort_folder_2, exist_ok=True)

# Create subfolders
for folder in sub_folders:
    create_path(cohort_folder_1, folder)
    create_path(cohort_folder_2, folder)
