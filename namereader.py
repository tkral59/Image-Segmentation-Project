import os
import csv
from PIL import Image, UnidentifiedImageError
import PIL
PIL.Image.MAX_IMAGE_PIXELS = 933120000  #fixes PIL.Image.DecompressionBombError
#a folder of folders
og_folder_path = 'G:\\.shortcut-targets-by-id\\12ZvEqQ2NxkXViA9sw36IrcUcoVsGsVM1\\Deep Learning Images_Labeled'  #tbd

def listDir(dir):
    f = open("C:\\Users\\joekr\\Documents\\SBU general\\Research Project\\brainImages.csv", 'a', newline='')
    if f.closed:
        print("Unable to open csv file.")
    files = os.listdir(dir)  #for some reason this gives a list in non-alphabetical order
    files = sorted(files)
    writer = csv.writer(f)
    writer.writerow([dir])
    writer.writerow(["File Name", "File Type", "Dimensions", "Memory size (MB)", "Validated Label", "Thick or Thin", "Blue or Yellow", "Has Marker"])
    for filename in files:
        if os.path.isdir(dir + "//" + filename):
            listDir(dir + "//" + filename)
        elif filename != "desktop.ini":
            try:
                img = Image.open(dir + "//" + filename)  # giving PIL.Image.DecompressionBombError
            except FileNotFoundError:
                print("Unable to open image file:", filename)
            except UnidentifiedImageError:
                print("Ignoring roi file:", filename)
                continue
            dims = str(img.width) + "x" + str(img.height)
            size = os.path.getsize(dir + "//" + filename) / 1000000
            writer.writerow([img.filename, img.format, dims, size])
            print("added: " + filename)
    writer.writerow([''])
    f.close

listDir(og_folder_path)
