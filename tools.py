#!/usr/local/bin/python3

from csv import reader
from pylab import *

def printGraph(km, price, theta0, theta1):
    scatter(km, price)
    xlabel('km')
    ylabel('price')
    lineX = [min(km), max(km)]
    lineY = [theta1 * float(i) + theta0 for i in lineX]
    plot(lineX, lineY)
    show()

def dataset_minmax(data):
    for row in data:
        for elem in row: assert (type(elem) == float)
    all_data = [elem for row in data for elem in row]
    return (min(all_data), max(all_data))

def normalize_elem(elem, minmax):
    assert (type(elem) == float)
    for row in minmax: assert (type(row) == float)
    return ((elem - minmax[0]) / (minmax[1] - minmax[0]))

def rev_normalize_elem(elem, minmax):
    assert (type(elem) == float)
    for row in minmax: assert (type(row) == float)
    return (elem * (minmax[1] - minmax[0]) + minmax[0])

def normalize_data(data, minmax):
    for row in data:
        for elem in row: assert (type(elem) == float)
    for row in range(len(data)):
        for elem in range(len(data[row])):
            data[row][elem] = normalize_elem(data[row][elem], minmax)

def rev_normalize_data(data, minmax):
    for row in data:
        for elem in row: assert (type(elem) == float)
    for row in range(len(data)):
        for elem in range(len(data[row])):
            data[row][elem] = rev_normalize_elem(data[row][elem], minmax)

def load_file(filename):
    try:
        file = open(filename, "r")
    except IOError as e:
        print('error: {}'.format(e.strerror))
        sys.exit(2)
    lines = reader(file)
    data = list(lines)
    del data[0]
    for row in data:
        for i in range(len(row)):
            row[i] = float(row[i].strip())
    return (data)