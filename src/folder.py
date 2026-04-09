# Folder class 
# Initiates folder class object
class folder():
    def __init__(self, name, files):
        self.name = name
        self.files = files
    
    def get_name(self):
        return self.name
    
    def get_files(self):
        return self.files
    
    def add_file(self, file):
        return self.files.append(file)
    
    def remove_file(self, file):
        return self.files.remove(file)
    
    # Debugging function
    def get_folder(self):
        return f'** Files in "{self.name}":\n** Files: {self.files}'


# folder1 = folder("Music", ["Bay City.mp3", "Santeria.mp3"])

# print(folder1.get_folder())

# i = 1
# for file in folder1.get_files():
#     print(f'>> File {i}: {file}')
#     i += 1
folder_name = input(">> Enter folder name: ")
folder_name = folder(folder_name, [])

while True:
    entry = input(">> Enter file name: ")
    if entry == 'exit':
        break
    if entry == '':
        print(">> ERROR: A file name cannot be blank!")
        continue

    folder_name.add_file(entry)

print(folder_name.get_folder())
