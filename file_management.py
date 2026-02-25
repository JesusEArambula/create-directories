import os, shutil, cohort
from cohort import Cohort

# print(os.getcwd())
# os.chdir(os.getcwd() + '/class documents')
# print(os.getcwd())
# print(os.listdir())

# Copy a file using shutil
# copyfile() = copies contents of a file
# copy()     = copyfile() + permission mode + destination can be a directory
# copy2()    = copy() + copies metadata (file's creation and modification times)
print("<<<<<<<<<< Inside Cohort #20/Class Documents")
os.chdir(os.getcwd()+ '/class documents')
documents_list = os.listdir()
for document in documents_list:
    if document == 'agreement form.docx' or document == 'enrollment form.docx' or document == 'syllabus.docx':
        shutil.copyfile(document, f"../(#20 SPANISH) Mon, Wed March 2026 Workshop 360 Valencia/Class Documents/Cohort #20 {document.title()}")
    if document == 'roster.xlsx':
        shutil.copyfile(document, f"../(#20 SPANISH) Mon, Wed March 2026 Workshop 360 Valencia/Roster/Cohort #20 {document.title()}")
    if document == 'schedule.xlsx':
        shutil.copyfile(document, f"../(#20 SPANISH) Mon, Wed March 2026 Workshop 360 Valencia/Schedule/Cohort #20 {document.title()}")
    if document == 'certificate.docx':
        shutil.copyfile(document, f"../(#20 SPANISH) Mon, Wed March 2026 Workshop 360 Valencia/Files/Cohort #20 Certificates/Cohort #20 {document.title()}")

    
    # debugging print statement
    # print(document)
    
# function to copy a file to another directory
# shutil.copyfile('agreement form.docx', '../(#20 SPANISH) Mon, Wed March 2026 Workshop 360 Valencia/Class Documents/Cohort #20 Agreement Form.docx')
print(os.listdir())

os.chdir("..")
print(os.getcwd())

os.chdir("(#20 SPANISH) Mon, Wed March 2026 Workshop 360 Valencia/Files/")
print("<<<<<<<<<< Inside Files subdirectory >>>>>>>>>>")
print(os.listdir())


