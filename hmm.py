# Author: Ethan Song
# Last Revised: Mar 24
# Hidden Markov Model Localizaiton Problem

import numpy as np
import grid
import random
import time
import robot

print("Welcome to the magic robot world!")
print("Please set up the grids world. Size should be at least 4*4.")
check = True


class ShortInput(Exception):
    """Check the size of the grids"""
    pass

while check:
    row, col = map(int, input("Enter the #rows and # cols of the grids: ").split(" "))
    try:
        if row < 4 or col < 4:
            raise ShortInput()
    except ShortInput:
        print("The size of grids is too small. It should be at least 4*4.")
    else:
        check = False

hmmgrids = np.ones((row, col))
# Initialize the grids
x0, y0 = [random.choice(list(range(row))), random.choice(list(range(col)))]
# Initialize the start position
neigh1_init, dir_init_valid = grid.grids_neighbor1(x0, y0, hmmgrids)
dir_pre = random.choice(dir_init_valid)
# Initialize the start direction

prob_filter = np.ones((row, col)) / (row * col)
prob_temp = np.zeros((row, col))
prob_sensor = np.zeros((row, col))
# Initialize the initial probability matrix

# Note the the transition matrix may change at each step
# We directly calculate the product of the transition and filter matrices

myrobot = robot.Robot(x0, y0, dir_pre)

# Now let's do filtering:
timer = 1
guess_error = []
local_error = []
while True: # timer <= 100:
    print("Iteration steps ", timer)
    neigh1, dir_valid = grid.grids_neighbor1(x0, y0, hmmgrids)
    location, location_guess, dir_next, prob_pre, prob_switch = myrobot.movement(x0, y0, hmmgrids, dir_pre)
    # Get the product of transition and filtering:
    for i in range(row):
        for j in range(col):
            neigh1_test, dir_test = grid.grids_neighbor1(i, j, hmmgrids)
            l_test, lguess_test, dnext_test, ppre_test, pswitch_test = myrobot.movement(i, j, hmmgrids, dir_pre)
            if ppre_test == 0.8:
                coor = np.array([i, j]) + np.array(dir_pre)
                prob_temp[coor[0], coor[1]] += prob_filter[i, j] * 0.8
                dir_test.remove(dir_pre)
                for item in dir_test:
                    coor = np.array([i, j]) + np.array(item)
                    prob_temp[coor[0], coor[1]] += prob_filter[i, j] * pswitch_test
            elif ppre_test == 0:
                for item in dir_test:
                    coor = np.array([i, j]) + np.array(item)
                    prob_temp[coor[0], coor[1]] += prob_filter[i, j] * pswitch_test
    # Get the sensor matrix:
    for i in range(row):
        for j in range(col):
            neigh1_test1, dir_test_2 = grid.grids_neighbor1(i, j, hmmgrids)
            neigh2_test2 = grid.grids_neighbor2(i, j, hmmgrids)
            if location_guess == [i, j]:
                prob_sensor[i, j] = 0.1
            elif location_guess in neigh1_test1:
                prob_sensor[i, j] = 0.05
            elif location_guess in neigh2_test2:
                prob_sensor[i, j] = 0.025
            elif location_guess is None:
                prob_sensor[i, j] = 0.1
            else:
                prob_sensor[i, j] = 0
    raw_filter = np.multiply(prob_sensor, prob_temp)
    [x0, y0] = location
    dir_pre = dir_next
    prob_filter = raw_filter / (raw_filter.sum())    # normalize
    prob_temp = np.zeros((row, col))

    # output
    view_filter = np.round(prob_filter, 6)
    flat_view = view_filter.flatten()
    max3_index = np.argsort(-flat_view)[:3]

    max1 = flat_view[max3_index[0]]
    cor_max1 = np.unravel_index(max3_index[0], (row, col))
    max2 = flat_view[max3_index[1]]
    cor_max2 = np.unravel_index(max3_index[1], (row, col))
    max3 = flat_view[max3_index[2]]
    cor_max3 = np.unravel_index(max3_index[2], (row, col))

    print("Robot is now in ", location)
    print("Robot senses it's in ", location_guess)
    if location_guess is None:
        location_guess = [random.choice(list(range(row))), random.choice(list(range(col)))]
        # Else you may rewrite the function robot.movement
        # To store the previous location guess and used it as the value here
    guess_err = sum(np.absolute((np.array(location_guess) - np.array(location))))
    guess_error.append(guess_err)
    # print(view_filter, "\n")
    print("Robot thinks it's in {0} with probability {1}".format(cor_max1, max1))
    print("Robot thinks it's in {0} with probability {1}".format(cor_max2, max2))
    print("Robot thinks it's in {0} with probability {1}".format(cor_max3, max3))
    local_err = sum(np.absolute((np.array(cor_max1) - np.array(location))))
    local_error.append(local_err)
    print("Sensor guess error is ", guess_err)
    print("Localization error is ", local_err, "\n")
    timer += 1
    time.sleep(1)

# print(guess_error)
# print(local_error)
# print(timer)
