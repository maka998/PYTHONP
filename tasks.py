import importlib, importlib.util
import os  # (ugradjeni modul)
import repositoryUtils as ru
import networkx as nx

from tkinter import *
from tkinter.filedialog import askopenfilename
import htmlpage as model
from collections import defaultdict

n = -1
workingDir = "none"


# Metoda za ucitavanja modula
def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


trie = module_from_file("TrieNode", "Trie.py")
# G = graph.Graph()


T = []


def parseFolders(root):
    global T

    for file in os.listdir(root):  # iz radnog direktorijuma sve izlistavamo
        if os.path.isdir(os.path.join(root, file)):  # provjera da li je taj faljl folder (ako jeste udji u njega)
            for subfile in os.listdir(os.path.join(root, file)):  # provjeri je li html
                if subfile.endswith(".html"):
                    node = parseOnePage(root, os.path.join(root,subfile))  # pozivamo sledecu funkciju(koja ce da parsira sadrzaj jedne srtanice)
                    t = trie.TrieNode('')
                    t.name = node.name   #punimo trie sa rijecima
                    for word in node.content:
                        trie.add(t, word.upper())

                    T.append(t)

        if file.endswith(".html"):
            node = parseOnePage(root, file)
            t = trie.TrieNode('')
            t.name = node.name
            for word in node.content:
                trie.add(t, word.upper())
            T.append(t)

        # [1] odabir direktorijuma


def directorySelection():
    Tk().withdraw()  # otvara dijalog za biranje direktorijuma
    filename = askopenfilename()
    ru.cls()

    workingDir = ru.getDir(filename)  #radni direktorijum,onaj koji smo odabrali koristimo u zadatku
    print("parsiramo foldere i podfoldere\n")
    # contains all files and subfolders NAMES
    pages = parseFolders(workingDir)


mc = module_from_file("Parser", "parser.py")


# fullpath = path + "\\" + filename
def parseOnePage(path, filename):#struktura koja nam daje informaciju koji svor ima koje linkove i sadrzaj cvora
    global mc
    parser = mc.Parser()
    [links, words] = parser.parse(path + "\\" + filename)
    page = model.HTMLpage(filename, path, words, links)
    return page


def exit():
    return
