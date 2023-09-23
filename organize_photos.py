import os
def extract_places(filename):
    return filename.split("_")[1]

def make_place_directories(places):
    for place in places:
        os.mkdir(place)

os.chdir("Photos")
originals = os.listdir()
places = []
for filename in originals:
    place = extract_places(filename)
    if place not in places:
        places.append(place)

make_place_directories(places)
print(os.listdir())