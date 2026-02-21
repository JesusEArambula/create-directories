import os, shutil

print(os.getcwd())
os.chdir(os.getcwd() + '/class documents')
print(os.getcwd())
print(os.listdir())

# Copy a file using shutil
# copyfile() = copies contents of a file
# copy()     = copyfile() + permission mode + destination can be a directory
# copy2()    = copy() + copies metadata (file's creation and modification times)
shutil.copyfile('agreement form.docx', '../(#20 SPANISH) Mon/Cohort #20 Agreement Form.docx')

print(os.listdir())
