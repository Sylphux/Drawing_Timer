import os
import sys

action = ""
arguments = ""
dir_path = os.getcwd()

def help():
    print("This script modifies all the files in the directory with different operations. It is used to add keywords in a large volume of files.\nadd: Use 'add your_string' to add a string\nrem: use 'rem string_to_remove' to remove a string\nrep: use 'rep old_string new_string' to replace a string with another\nbeg: use 'beg new_beginning' to concatenate a string at the beginning")
    exit()

def verify_command():
    if len(sys.argv) < 3:
        exit("Not enough arguments")
    elif not ("ren" in sys.argv[1] or "add" in sys.argv[1] or "rem" in sys.argv[1] or "rep" in sys.argv[1] or "beg" in sys.argv[1]):
        exit("Unknown argument : " + sys.argv[1])

if sys.argv[1] == "help" or sys.argv[1] == 'h':
    help()

verify_command()
action = sys.argv[1]
arguments = " ".join(sys.argv[2:])

def list_files(path):
    files_list = []
    for e in os.scandir(path):
        if e.is_file():
            files_list.append(e.name)
    return files_list
    
def rename_file(file, new_name):
    while new_name[len(new_name) - 1] == "_":
        new_name = new_name[:-1]
    i = 0
    temp_name = ""
    new_name = new_name.replace(" ", "_")
    for c in new_name:
        if not (new_name[i] == "_" and new_name[i-1] == "_"):
            temp_name = temp_name + c
        i += 1
    new_name = temp_name
    os.rename(os.path.join(dir_path, file), os.path.join(dir_path, new_name))

print("Loading files in " + dir_path + "...")
files_list = list_files(dir_path)
print("Found " + str(len(files_list)) + " files.")

print("This will apply", action, "with arguments", arguments, "on", str(len(files_list)), "files...")
if input("Press enter to commit: ") != "":
    exit

i = 0
for file in files_list:
    if action == "add":
        rename_file(file, (file + "_" + arguments))
    if action == "ren":
        rename_file(file, (arguments + "(" + str(i)) + ")")
    i += 1
    if action == "rem":
        if arguments in file:
            to_remove_index = file.index(arguments)
            new_name = file[0:to_remove_index] + file[(to_remove_index + len(arguments)):len(file)]
            rename_file(file, new_name)
    if action == "rep":
        if sys.argv[2] in file:
            to_remove_index = file.index(sys.argv[2])
            to_remove_end_index = to_remove_index + len(sys.argv[2])
            new_name = file[0:to_remove_index] + sys.argv[3] + file[to_remove_end_index:]
            rename_file(file, new_name)
    if action == "beg":
        rename_file(file, arguments + "_" + file)

print("Done.")
