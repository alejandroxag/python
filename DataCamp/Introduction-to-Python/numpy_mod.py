# DataCamp
# Introduction to Python
# Numpy

import numpy as np

# Numpy

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

# Create array height_in
height_in = np.array([74, 74, 72, 72, 73, 69, 69, 71, 76, 71])

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = 0.0254*np_height_in

# Print np_height_m
print(np_height_m)

# Create array weight_lb
weight_lb = np.array([180, 215, 210, 210, 188, 176, 209, 200, 231, 180])

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = 0.453592*np.array(weight_lb)

# Calculate the BMI: bmi
bmi = np_weight_kg/(np_height_m**2)

# Print out bmi
print(bmi)

# Create the light array
light = bmi < 25

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[5])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[3:8])

# 2D Numpy Arrays

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)


# Print out the 50th row of np_baseball
print(np_baseball[2,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]
print(np_weight_lb)

# Print out height of 124th player
print(np_baseball[3,0])

baseball = [[74.0, 180.0, 22.99], 
            [74.0, 215.0, 34.69], 
            [72.0, 210.0, 30.78], 
            [72.0, 210.0, 35.43], 
            [73.0, 188.0, 35.71], 
            [69.0, 176.0, 29.39], 
            [69.0, 209.0, 30.77], 
            [71.0, 200.0, 35.07], 
            [76.0, 231.0, 30.19], 
            [71.0, 180.0, 27.05]]

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

updated = np.array([[  1.2303559 , -11.16224898,   1.        ],
                  [  1.02614252,  16.09732309,   1.        ],
                  [  1.1544228 ,   5.08167641,   1.        ],
                  [  0.64427532,  -5.09538071,   1.        ],
                  [  1.00590086,   2.24342718,   1.        ],
                  [  0.97953547,  12.19841763,   1.        ],
                  [  0.62874324,  13.72324216,   1.        ],
                  [  1.27075194,  -8.87946313,   1.        ],
                  [  0.47655945, -10.82495536,   1.        ],
                  [  0.91699376,  -7.01116249,   1.        ]])

print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254,0.453592,1])

# Print out product of np_baseball and conversion
print(conversion*np_baseball)

# Basics statistics

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: \n" + str(corr))

positions = ['GK', 'M', 'A', 'D', 'M', 'D', 'M', 'M', 'M', 'A']
heights = [191, 184, 185, 180, 181, 187, 170, 179, 183, 186]

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']
    
# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
