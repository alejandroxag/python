# DataCamp
# Introduction to Python
# Python Lists

# Ex 1

# Lists

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

areas = [hall,kit,liv,bed,bath]
print(areas)

areas2 = ["hallway",hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]
print(areas2)

house = house = [["hallway", hall],
                 ["kitchen", kit],
                 ["living room", liv],
                 ["bedroom",bed],
                 ["bathroom",bath]]
print(house)
print(type(house))

# Filtering lists

areas3 = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
print(areas3[1])
print(areas3[-1])
print(areas3[6-1])

eat_sleep_area = areas3[3] + areas3[-3]
print(eat_sleep_area)

downstairs = areas3[:6]
upstairs = areas3[-4:]

print(downstairs,upstairs)

print(house[-1][1])

# Manipulating lists

areas3[-1] = 10.50
areas3[4] = 'chill zone'

areas3_1 = areas3 + ['poolhouse',24.5]
areas3_2 = areas3_1 + ['garage',15.45]

print(areas3_1)
print(areas3_2)

del(areas3_2[-4:-2])
print(areas3_2)

areas4 = [11.25, 18.0, 20.0, 10.75, 9.50]
areas4_copy = areas4[:]
areas4_copy[0] = 5.0
print(areas4,areas4_copy)