# DataCamp
# Intermediate Python
# Loops

import numpy as np
import pandas as pd

# while loop

# Initialize offset
offset = 8

# Code the while loop
while offset != 0 :
    print('correcting...')
    offset = offset - 1
    print(offset)

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset - 1
    else : 
      offset = offset + 1
    print(offset)

# for loop

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for a in areas :
    print(a)

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas) :
    print('room ' + str(index) + ': ' + str(a))

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area))

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for sblst in house :
    print('the ' + sblst[0] + ' is ' + str(sblst[1]) + ' sqm')

# Loop Data Structures Part 1

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for k, v in europe.items() :
    print('the capital of ' + k + ' is ' + v)

np_height = np.array([74, 74, 72, 75, 75, 73])

# For loop over np_height
for i in np.nditer(np_height) :
    print(str(i) + ' inches')

# # For loop over np_baseball
# for i in np.nditer(np_baseball) :
#     print(i)

# Loop Data Structures Part 2

cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ':  ' + str(row['cars_per_cap']))
    print(row)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab,'COUNTRY'] = row['country'].upper()

# Print cars
print(cars)

# Use .apply(str.upper)
cars['COUNTRY'] = cars['country'].apply(str.upper)