#program to find keywords from one directory, and find their corresponding images in another directory with said keywords.

import os
import collections
#import re

labeleddir = "G:\\My Drive\\Brain Image Segmentation\\ESE 440-1\\Deep Learning Images_Labeled"
fileso = os.listdir(labeleddir)
fileso = sorted(fileso)
wordsearch = []
def nameextract(dir, name):
    files = os.listdir(dir)
    l = [0, 0]
    for filename in files:
        if(os.path.isdir(dir + '\\' + filename) and type(filename) == type(l)):
            files.append(os.listdir(dir + "\\" + filename))
        elif((filename == 'desktop.ini')):
            print('skipping .ini')
        else:
            if(name == ['Piliocolobus', 'badius']):
                print('break')
            filenamec = filename
            filenamec = filenamec[0:len(filenamec) - 4]
            filenamec = filenamec.replace(' ', '_')
            filenamec = filenamec.split('_')
            flag = 0
            for x in filenamec:
                for character in x:
                    if((ord(character) < ord('0')) or (ord(character) > ord('9'))):
                        flag = 1
                        break  
                if((flag != 1) and x != ''):
                    name.append(x)
                flag = 0
            duplist = [item for item, count in collections.Counter(name).items() if count > 1]
            for x in duplist:
                name.remove(x)
    wordsearch.append(name)


for filenameo in fileso:
    print(type(filenameo))
    name = filenameo.split()
    if(os.path.isdir(labeleddir + "\\" + filenameo)):
        nameextract(labeleddir + "\\" + filenameo, name)

print("")
print(wordsearch)

unlabeled = 'G:\\.shortcut-targets-by-id\\1HDEiXLZ0MhVVdCCWfum8gbgG2IesFJM5\\TIFF'
matches = []

uldir = os.listdir(unlabeled)
cnt=[]
def iterdir(dir):
    ndir = os.listdir(dir)
    for file in ndir:
        if(os.path.isdir(dir + '\\' + file)):
            iterdir(dir + '\\' + file)
        elif(file == 'desktop.ini'):
            print('ignoring .ini')
        else:
            for entry in wordsearch:
                if((entry[0] in file) and (entry[1] in file)):
                    for index in entry[2:len(entry)-1]:
                        if(index in file):
                            matches.append(file)
                            break

iterdir(unlabeled)

print("test list:")
print(matches)
print(len(matches))
print(len(set(matches)))
matches = set(matches)
#total = 0
#for entry in wordsearch:
#    for item in entry:
#        total += 1
total = 909
print(total)
