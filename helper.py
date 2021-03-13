#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 19:49:06 2018

@author: iswariya
"""
import copy
import math
import random
import matplotlib.pyplot as plt
import numpy as np


def plot_cost_function(cost):
    """ Function to plot the no. of iterations (x-axis) vs
    cost (y-axis). X-axis of the plot should contain xticks
    from 0 to 10000 in steps of 2000.
    Use matplotlib.pyplot to generate the plot as .png file and store it
    in the results folder. An example plot is
    there in the results folder.

    Parameters
    ----------
    cost : [type]
        [description]
    """

    x = np.arange(1,10001,1)
    plt.plot(x,cost)
    plt.xticks(np.arange(0,10001,2000))
    plt.xlabel("# of Iterations")
    plt.ylabel("Distance")
    
    #plt.title('Hill_climbing_simple_49_cities')
    #plt.savefig('results/plots/Hill_climbing_simple_49_cities.png')
    plt.title('Hill_climbing_simple_cities_full')
    plt.savefig('results/plots/Hill_climbing_simple_cities_full.png')

    #plt.title('Hill_climbing_steepest_descent_49_cities')
    #plt.savefig('results/plots/Hill_climbing_steepest_descent_49_cities.png')
    #plt.title('Hill_climbing_steepest_descent_cities_full')
    #plt.savefig('results/plots/Hill_climbing_steepest_descent_cities_full.png')

    return 


def get_successors(curr_seq):
    """ Function to generate a list of 100 random successor sequences
    by swapping any TWO cities randomly. Please note that the first and last city
    should remain unchanged since the traveller starts and ends in
    the same city.

    Parameters
    ----------
    curr_seq : list
        current traverse sequence between cities

    Returns
    -------
    list
        New 100 random traverse sequences
        """

    rand_successor = []
    for i in range(100):
        new_seq = curr_seq.copy()
        #chooosing random pair & ensuring that start and end cities are not changed
        rand_idx = random.sample(range(1, len(curr_seq)-1), 2)
        #swapping
        new_seq[rand_idx[0]] = curr_seq[rand_idx[1]]
        new_seq[rand_idx[1]] = curr_seq[rand_idx[0]]
        rand_successor.append(new_seq)


    return rand_successor


def get_distance(distance_matrix, seq):
    """ Function to get the distance while travelling along
    a particular sequence of cities.
    HINT : Keep adding the distances between the cities in the
    sequence by referring the distances from the distance matrix

    Parameters
    ----------
    distance_matrix : array
        square matrix of distances between all coordinate points
    seq : list
        random initial sequence of traverse between cities
    
    Returns
    -------
    float
        total travelled distance for the given traverse sequence 
    """
    travelled_distance = 0
    for i in range(len(seq)-1):
        dist_bet_2cities = distance_matrix[seq[i]][seq[i+1]]
        travelled_distance += dist_bet_2cities

    return travelled_distance


def get_distance_matrix(coordinates):
    """ Function to generate a distance matrix. The distance matrix
    is a square matrix.
    For eg: If there are 3 cities then the distance
    matrix has 3 rows and 3 colums, with each city representing a row
    and a column. Each element of the matrix represents the euclidean
    distance between the coordinates of the cities. Thus, the diagonal
    elements will be zero (because it is the distance between the same city).

    Parameters
    ----------
    coordinates : list
        longitude,latitude coordinates for each city

    Returns
    -------
    array
        square matrix of distances between all coordinate points
    """
    dist_matrix = np.empty((len(coordinates),len(coordinates)))
    
    for i in range(len(coordinates)):      
        city_1 = ( float(coordinates[i][0]), float(coordinates[i][1]) )
        for j in range(len(coordinates)):     
            city_2 = ( float(coordinates[j][0]), float(coordinates[j][1]) )
            dist_matrix[i][j] = math.dist(city_1, city_2)

    return dist_matrix