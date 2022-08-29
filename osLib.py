import os

def current_directory():
    cwd= os.getcwd()
    print(cwd)
    

def file_name(name):
    path = os.path.abspath((name))
    print(path)
current_directory()
file_name("osLib.py")