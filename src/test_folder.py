import os


folder = 'CarData/TestImages'

for (dirname, path, filenames) in os.walk(folder):
    print(dirname)
    print(path)
    print(filenames)
