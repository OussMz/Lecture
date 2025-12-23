import os
import shutil

current_working_directory = os.getcwd()
print("Current Working Directory:", current_working_directory)

current_dir = os.path.dirname(os.path.abspath(__file__))
lab_files_path = os.path.join(current_dir, "Lab files")
lab_files = os.makedirs(lab_files_path, exist_ok = True)

for file_name in ["text1.txt", "text2.txt", "text3.txt"]:
    file_path = os.path.join(lab_files_path, file_name)
    with open(file_path, 'w'):
        pass

print("Files created in 'Lab files' directory:\n")
for file_name in os.listdir(lab_files_path):
    print(file_name)

os.rename(
    os.path.join(lab_files_path, "text1.txt"),
    os.path.join(lab_files_path, "renamed_text1.txt")
)
print("\nAfter renaming 'text1.txt' to 'renamed_text1.txt':\n")

shutil.rmtree(lab_files_path)
print("\n'Lab files' directory and its contents have been deleted.")       