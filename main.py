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
        tmpTheta0 = 0.0
        tmpTheta1 = 0.0

        for row in data:
            tmpTheta0 += (estimatePrice(row[0]) - row[1])
            tmpTheta1 += ((estimatePrice(row[0]) - row[1]) * row[0])
        theta0 -= ((learningRate * tmpTheta0) / float(len(data)))
        theta1 -= ((learningRate * tmpTheta1) / float(len(data)))

def aim(data):
    data_X = [row[0] for row in data]
    data_Y = [row[1] for row in data]
    sum_X = sum(data_X)
    sum_Y = sum(data_Y)
    mean_X = mean(data_X)
    mean_Y = mean(data_Y)
    Sum_of_Square_X = sum([((elem - mean_X) ** 2) for elem in data_X])
    Sum_of_Products = sum([((row[0] - mean_X) * (row[1] - mean_Y)) for row in data])
    aim_theta1 = Sum_of_Products / Sum_of_Square_X
    aim_theta0 = mean_Y - aim_theta1 * mean_X
    return (aim_theta0, aim_theta1)

def main():
    global theta0
    global theta1
    size = (0.0, 1.0)

    try:
        assert (len(sys.argv) == 2)
    except:
        print('usage: ./main.py [data.csv]')
        sys.exit(1)
    data, title = load_file(sys.argv[1])
    aim_theta0, aim_theta1 = aim(data)
    minmax = dataset_minmax(data)
    normalize_data_set(normalize_elem, data, minmax, size)
    learningFunction(data)
    theta0 = rev_normalize_elem(theta0, minmax, size)
    print(theta0, theta1)
    normalize_data_set(rev_normalize_elem, data, minmax, size)
    printGraph([row[0] for row in data], [row[1] for row in data], title, theta0, theta1, aim_theta0, aim_theta1)

theta0 = 0.0
theta1 = 0.0

if __name__ == '__main__':
    main()
