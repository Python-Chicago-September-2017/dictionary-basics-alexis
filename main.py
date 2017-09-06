myself = {
    'name': 'Alexis',
    'age': '34',
    'country of birth': 'Puerto Rico',
    'favorite language': 'spanish'
}

print "this is me testing the length of a dictionary. Length is {}".format(len(myself))

def write_descriptions(person):
    for detail in person:
        print "My {} is {}".format(detail, person[detail])

write_descriptions(myself)

