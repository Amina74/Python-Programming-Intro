import os
#recursive function which iterates when dir_path is a directory
def print_subdirectories(dir_path):
    #storing the contents of dir_path in files
    files = os.listdir(dir_path)
    #iterating the contents of files recursively
    for f in files:
        s = os.path.join(dir_path,f)
        if os.path.isdir(s):
            print(s)
            print_subdirectories(s)
dir_path = '/Users/aminahamza/School/Year3/Semester1/IntroPrograming/1DV501' 
print_subdirectories(dir_path) 