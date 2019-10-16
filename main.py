#!/usr/local/bin/python3

import sys
from tools import *

def estimatePrice(mileage):
    assert (type(mileage) == float)
    return (theta0 + theta1 * mileage)

def cost_function(data):
    err = 0
    for row in data:
        err = err + (row[1] - estimatePrice(row[0])) ** 2
    return (err / len(data))

def learningFunction(data):
    global theta0
    global theta1
    learningRate = float(0.01)
    loss = []

    for row in data:
        for elem in row: assert (type(row[0]) == float)
    for _ in range(0, 10000):
        tmpTheta0 = float(0)
        tmpTheta1 = float(0)

        for row in data:
            tmpTheta0 = tmpTheta0 + (estimatePrice(row[0]) - row[1])
            tmpTheta1 = tmpTheta1 + ((estimatePrice(row[0]) - row[1]) * row[0])
        theta0 = theta0 - (learningRate * (1 / len(data)) * tmpTheta0)
        theta1 = theta1 - (learningRate * (1 / len(data)) * tmpTheta1)
        loss.append(cost_function(data))
    return (loss)

def main():
    global theta0
    global theta1
    data = []

    try:
        assert (len(sys.argv) == 2)
    except:
        print('usage: ./main.py [data.csv]')
        sys.exit(1)
    data = load_file(sys.argv[1])
    minmax = dataset_minmax(data)
    normalize_data(data, minmax)
    loss = learningFunction(data)
    theta0 = rev_normalize_elem(theta0, minmax)
    #theta1 = rev_normalize_elem(theta1, minmax)
    print(loss[-1])
    print(theta0, theta1)
    rev_normalize_data(data, minmax)
    printGraph([row[0] for row in data], [row[1] for row in data], theta0, theta1)

theta0 = float(0)
theta1 = float(0)

if __name__ == '__main__':
    main()
