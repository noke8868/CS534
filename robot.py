# Author: Ethan Song
# Last Revised: Mar 24
# Hidden Markov Model Localizaiton Problem

import numpy as np
import grid
import random


class Robot:
    def __init__(self, x0, y0, direction):
        self.x0 = x0
        self.y0 = y0
        self.direction = direction

    @staticmethod
    def movement(x, y, hmmgrids, direction_pre):
        neigh1, dir_possible = grid.grids_neighbor1(x,  y, hmmgrids)
        thres_dir = random.uniform(0, 1)
        if direction_pre in dir_possible:
            prob_dir_pre = 0.8
            prob_dir_switch = 0.2 / (len(dir_possible)-1)
            if thres_dir <= 0.8:
                direction_next = direction_pre
            elif thres_dir <= 1:
                direction_next = random.choice(dir_possible)
        else:
            direction_next = random.choice(dir_possible)
            prob_dir_pre = 0
            prob_dir_switch = 1 / len(dir_possible)
        location = np.array([x, y]) + np.array(direction_next)
        location = list(location)

        neigh1, dir_possible = grid.grids_neighbor1(location[0],  location[1], hmmgrids)
        neigh2 = grid.grids_neighbor2(location[0],  location[1], hmmgrids)
        thres_location = random.uniform(0, 1)
        if thres_location <= 0.1:
            location_guess = location
        elif thres_location <= 0.5:
            location_guess = random.choice(neigh1)
        elif thres_location <= 0.9:
            location_guess = random.choice(neigh2)
        else:
            location_guess = None
        return location, location_guess, direction_next, prob_dir_pre, prob_dir_switch

