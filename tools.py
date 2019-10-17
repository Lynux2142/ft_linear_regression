#!/usr/local/bin/python3

from csv import reader
from pylab import *

def printGraph(x, y, title, theta0, theta1, aim_theta0, aim_theta1):
    assert (type(title[0]) == str and type(title[1]) == str)
    scatter(x, y)
    xlabel(title[0])
    ylabel(title[1])
    lineX = [min(x), max(x)]
    lineY = [theta1 * float(i) + theta0 for i in lineX]
    aim_lineY = [aim_theta1 * float(i) + aim_theta0 for i in lineX]
    plot(lineX, lineY)
    plot(lineX, aim_lineY)
    show()

def dataset_minmax(data):
    for row in data:
        for elem in row: assert (type(elem) == float)
    all_data = [elem for row in data for elem in row]
    return (min(all_data), max(all_data))

def normalize_elem(elem, minmax, size):
    assert (type(elem) == float)
    for row in minmax: assert (type(row) == float)
    return ((size[1] - size[0]) * ((elem - minmax[0]) /
            (minmax[1] - minmax[0])) + size[0])
    #return ((elem - minmax[0]) / (minmax[1] - minmax[0]))

def rev_normalize_elem(elem, minmax, size):
    assert (type(elem) == float)
    for row in minmax: assert (type(row) == float)
    return (((elem - size[0]) * (minmax[1] - minmax[0]) +
             (size[1] - size[0]) * minmax[0]) / (size[1] - size[0]))
    #return (elem * (minmax[1] - minmax[0]) + minmax[0])

def normalize_data_set(norm_funct, data, minmax, size):
    for row in data:
        for elem in row: assert (type(elem) == float)
    for row in range(len(data)):
        for elem in range(len(data[row])):
            data[row][elem] = norm_funct(data[row][elem], minmax, size)

def load_file(filename):
    try:
        file = open(filename, "r")
    except IOError as e:
        print('error: {}'.format(e.strerror))
        sys.exit(2)
    lines = reader(file)
    data = list(lines)
    title = data[0]
    del data[0]
    for row in data:
        for i in range(len(row)):
            row[i] = float(row[i].strip())
    return (data, title)
