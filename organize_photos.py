import os

os.chdir("Photos")
originals = os.listdir()

#print out list, just to be sure you are getting the results you expect:
print(originals)


def extract_place(filename):
    first = filename.find("_") #To find posotion of first underscore
    partial = filename[first+1 :]
    second = partial.find("_")
    return partial[:second]
