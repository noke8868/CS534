# Author: Ethan Song
# Last Revised: Mar 24
# Hidden Markov Model Localizaiton Problem


def grids_neighbor1(x, y, hmmgrids):
    basic_neigh1 = [[x+1, y], [x-1, y], [x, y+1], [x, y-1], [x+1, y+1], [x+1, y-1], [x-1, y+1], [x-1, y-1]]
    valid_neigh1 = [[x+1, y], [x-1, y], [x, y+1], [x, y-1], [x+1, y+1], [x+1, y-1], [x-1, y+1], [x-1, y-1]]
    basic_direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    # Be aware of the fact here: from (x,y) to (x+1, y) the robot actually goes down
    # Since we are using matrix index, so [1,0] doesn't mean goes right
    valid_direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    size = hmmgrids.shape
    for neigh in basic_neigh1:
        if neigh[0] < 0 or neigh[1] < 0 or neigh[0] >= size[0] or neigh[1] >= size[1]:
            valid_neigh1.remove(neigh)
    for item in basic_direction:
        if item[0] + x < 0 or item[1] + y < 0 or x + item[0] > size[0] - 1 or y + item[1] > size[1] - 1:
            valid_direction.remove(item)
    return valid_neigh1, valid_direction


def grids_neighbor2(x, y, hmmgrids):
    basic_neigh2 = [[x, y+2], [x, y-2], [x+1, y+2], [x+1, y-2], [x+2, y], [x+2, y+1], [x+2, y-1], [x+2, y+2],
                    [x+2, y-2], [x-1, y+2], [x-1, y-2], [x-2, y], [x-2, y+1], [x-2, y-1], [x-2, y+2], [x-2, y-2]]
    valid_neigh2 = [[x, y+2], [x, y-2], [x+1, y+2], [x+1, y-2], [x+2, y], [x+2, y+1], [x+2, y-1], [x+2, y+2],
                    [x+2, y-2], [x-1, y+2], [x-1, y-2], [x-2, y], [x-2, y+1], [x-2, y-1], [x-2, y+2], [x-2, y-2]]
    size = hmmgrids.shape
    for neigh in basic_neigh2:
        if neigh[0] < 0 or neigh[1] < 0 or neigh[0] >= size[0] or neigh[1] >= size[1]:
            valid_neigh2.remove(neigh)
    return valid_neigh2
