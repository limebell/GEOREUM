import glob
import os

root_dir = "manager_tests"


def visitall(root_dir):
    for filename in glob.iglob(root_dir + '**/**', recursive=True):
        if os.path.isfile(filename):
            print(filename)
            with open(filename, 'r') as file:
                print(file.read())
