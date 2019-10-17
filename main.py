#!/usr/local/bin/python3

import sys
from tools import *

def estimatePrice(mileage):
    assert (type(mileage) == float)
    return (theta0 + theta1 * mileage)

def learningFunction(data):
    global theta0
    global theta1
    learningRate = 0.01

    for row in data:
        for elem in row: assert (type(row[0]) == float)
    for _ in range(0, 10000):
        tmpTheta0 = float(0)
        tmpTheta1 = float(0)

        for row in data:
            tmpTheta0 = tmpTheta0 + (estimatePrice(row[0]) - row[1])
            tmpTheta1 = tmpTheta1 + ((estimatePrice(row[0]) - row[1]) * row[0])
        theta0 = theta0 - (learningRate * (1.0 / float(len(data))) * tmpTheta0)
        theta1 = theta1 - (learningRate * (1.0 / float(len(data))) * tmpTheta1)

def main():
    global theta0
    global theta1
    data = []
    size = (0.0, 1.0)

    try:
        assert (len(sys.argv) == 2)
    except:
        print('usage: ./main.py [data.csv]')
        sys.exit(1)
    data, title = load_file(sys.argv[1])
    minmax = dataset_minmax(data)
    normalize_data_set(normalize_elem, data, minmax, size)
    learningFunction(data)
    theta0 = rev_normalize_elem(theta0, minmax, size)
    print(theta0, theta1)
    normalize_data_set(rev_normalize_elem, data, minmax, size)
    printGraph([row[0] for row in data], [row[1] for row in data], title, theta0, theta1)

theta0 = float(0)
theta1 = float(0)

if __name__ == '__main__':
    main()
