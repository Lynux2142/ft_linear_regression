#!/usr/local/bin/python3

import sys
from tools import *
from math import *

def estimatePrice(value):
    return (theta0 + theta1 * value)

def cost_function(data):
    sum_value = sum([((estimatePrice(row[0]) - row[1]) ** 2) for row in data])
    return ((1.0 / (2.0 * float(len(data))))) * sum_value

def learningFunction(data):
    global theta0
    global theta1
    learningRate = 0.01
    cost = []

    for _ in range(0, 10000):
        tmpTheta0 = 0.0
        tmpTheta1 = 0.0

        cost.append(cost_function(data))
        for row in data:
            tmpTheta0 += (estimatePrice(row[0]) - row[1])
            tmpTheta1 += ((estimatePrice(row[0]) - row[1]) * row[0])
        theta0 -= ((learningRate * tmpTheta0) / float(len(data)))
        theta1 -= ((learningRate * tmpTheta1) / float(len(data)))
    cost.append(cost_function(data))
    return (cost)

def rev_theta(minmax, size):
    global theta0
    global theta1

    a = normalize_elem(minmax[0][0], minmax[0], size)
    b = normalize_elem(minmax[0][1], minmax[0], size)
    point_a = [minmax[0][0], rev_normalize_elem(estimatePrice(a), minmax[1], size)]
    point_b = [minmax[0][1], rev_normalize_elem(estimatePrice(b), minmax[1], size)]
    theta1 = (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])
    theta0 = point_a[1] - theta1 * point_a[0]

def main():
    global theta0
    global theta1
    size = (-1.0, 1.0)
    point = None

    try:
        assert (len(sys.argv) == 2 or len(sys.argv) == 3)
    except:
        print('usage: ./main.py data_set.csv [value]')
        sys.exit(1)
    data = load_file(sys.argv[1])
    print('coefficient of determination: {}'.format(linear_correlation(data[1:])))
    minmax = dataset_minmax(data)
    normalize_data_set(normalize_elem, data, minmax, size)
    cost = learningFunction(data[1:])
    rev_theta(minmax, size)
    save_thetas(theta0, theta1)
    print('theta0 = {}\ntheta1 = {}'.format(theta0, theta1))
    normalize_data_set(rev_normalize_elem, data, minmax, size)
    if (len(sys.argv) == 3):
        value = float(sys.argv[2])
        predict = estimatePrice(value)
        print('{0} ({2}) --> {1} ({3} predicted)'.format(value, predict, data[0][0], data[0][1]))
        point = [value, predict]
    printGraph(data, cost, theta0, theta1, point)

theta0 = 0.0
theta1 = 0.0

if __name__ == '__main__':
    main()
