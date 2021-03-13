#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:04:22 2018

@author: iswariya
"""

import argparse
import random
import timeit
import os
import matplotlib.pyplot as plt
from helper import *


def hill_climb_simple(start_seq, coordinates):
    """ Function to implement simple hill climbing algorithm
    for the travelling salesman problem.
    Run the hill climbing algorithm for 10000 iterations and
    randomly restarting at every 2000 iterations.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    start_seq : list
        random initial sequence of traverse between cities
    coordinates : list
        longitude,latitude coordinates for each city

    Returns
    -------
    cost: list
        total travelled distance for each iteration
    least_distance: float
        Least possible travelled distance
    current_seq: list
        best sequence to traverse cities
    """

    counter = 1
    #calculate distances between cities 
    dist_matrix = get_distance_matrix(coordinates)
    #initialize some variables
    cost = []    
    seen_states = []
    curr_seq = start_seq
    curr_seq_list = []

    while counter <= 2000: 
        print("Iteration: ", counter)
        if counter == 1:
                        
            seen_states.append(start_seq)
            #calculate distance of current sequence
            seq_dist = get_distance(dist_matrix, curr_seq)
            cost.append(seq_dist)
            current_cost = seq_dist
            curr_seq_list.append(curr_seq)
       
        #get 100 random successors
        successors = get_successors(curr_seq_list[-1])
        #Evaluate the total distance for each successor 
        for i in successors:
            if i not in seen_states:
                seen_states.append(i)
                seq_dist = get_distance(dist_matrix, i)
                #if the proposed sequence has less distance then the current then adopt it
                if seq_dist < current_cost:
                    current_cost = seq_dist
                    current_seq = i
                    break #Once found a sequence better than the current, then stop checking the rest and break
                  
        
        cost.append(current_cost)
        curr_seq_list.append(current_seq)
        counter += 1
        os.system('clear')

    return cost[-1], curr_seq_list[-1], cost[:counter-1]


if __name__ == '__main__':

    # Reading txt file path from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str)
    args = parser.parse_args()
    file_path = os.path.join(os.getcwd(), args.filename)
    with open(file_path) as file:
        data = file.readlines()

    # Getting the list of cities and their coordinates
    list_of_cities = [i.strip().split(',') for i in data]
    city_names = [row[0] for row in list_of_cities[1:]]
    coordinates = [[row[1], row[2]] for row in list_of_cities[1:]]    

    
    start_time = timeit.default_timer()
    #initializing some variables
    current_cost = 99999
    #best cost for each 2000 trial
    cost_every_2000 = []
    seq_every_2000 = []
    cost_plot = []
    # Generating a random intial sequence
    random_start_seq = random.sample(range(0, len(list_of_cities[1:])),
                                         len(list_of_cities[1:]))
    # Calculating the least dist using simple hill climbing (5 Iterations, same initial sequence)
    for i in range(5):

        least_distance, current_seq, cost = hill_climb_simple(random_start_seq,          
                                                     coordinates)        
        cost_plot.append(cost)
        cost_every_2000.append(least_distance)
        seq_every_2000.append(current_seq)
        #get best performing sequence among the 5 trials
        if least_distance < current_cost:
            best_cost_ever = least_distance
            current_cost = best_cost_ever
            best_seq_ever = current_seq
                                                    
    end_time = timeit.default_timer()
    
    #plotting
    flat_list = [item for first_dim in cost_plot for item in first_dim]
    plot_cost_function(flat_list)
    
    #writing to file
    cwd = os.getcwd()
    #output_path =  cwd + "/results/Hill_climbing_simple_49_cities.txt"
    output_path =  cwd + "/results/Hill_climbing_simple_cities_full.txt"
    L = ["cost every 2000 iteration: " + str(cost_every_2000), 
    "\n\nLeast distance from Simple hill climbing:"+ str(int(best_cost_ever)),
     "\n\nBest Sequence:" + str(best_seq_ever), "\n\nTime: " + str(end_time - start_time)]
    f =  open(output_path, 'w')
    f.writelines(L)

    #Terminal Printing
    print("Best Sequence:", best_seq_ever)
    print("Least distance from Simple hill climbing:", best_cost_ever)
    print("Time: {}".format(end_time - start_time))