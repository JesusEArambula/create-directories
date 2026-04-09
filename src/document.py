# Document class 
# Initiates document class object
# Used for all document types:
# docx, xlsx, pptx
class Document():
    def __init__(self, name, file_type):
        self.name = name
        self.file_type = file_type
    
    def get_name(self):
        return self.name
    
    def rename_file(self, new_name):
        self.name = new_name