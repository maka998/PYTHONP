import os


def printSelectedFolder(path):
    print("Selected folder: " + path)

    for file in os.listdir(path):
        if os.path.isdir(path + "/" + file):
            print("FOLDER: " + file)
        if file.endswith(".html"):
            print("FILE: " + file)


def getDir(path):
    return os.path.dirname(path)


def cls():
    os.system('cls')