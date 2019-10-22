#!/usr/local/bin/python3

import sys
from tools import *

def estimatePrice(mileage):
    return (theta0 + theta1 * mileage)

def learningFunction(data):
    global theta0
    global theta1
    learningRate = 0.01

    for _ in range(0, 10000):
        tmpTheta0 = 0.0
        tmpTheta1 = 0.0

        for row in data:
            tmpTheta0 += (estimatePrice(row[0]) - row[1])
            tmpTheta1 += ((estimatePrice(row[0]) - row[1]) * row[0])
        theta0 -= ((learningRate * tmpTheta0) / float(len(data)))
        theta1 -= ((learningRate * tmpTheta1) / float(len(data)))

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

    try:
        assert (len(sys.argv) == 2 or len(sys.argv) == 3)
    except:
        print('usage: ./main.py data_set.csv [value]')
        sys.exit(1)
    data = load_file(sys.argv[1])
    minmax = dataset_minmax(data)
    normalize_data_set(normalize_elem, data, minmax, size)
    learningFunction(data[1:])
    rev_theta(minmax, size)
    save_thetas(theta0, theta1)
    normalize_data_set(rev_normalize_elem, data, minmax, size)
    if (len(sys.argv) == 3):
        mileage = float(sys.argv[2])
        predict_price = estimatePrice(mileage)
        printGraph(data, theta0, theta1, [mileage, predict_price])
    else:
        printGraph(data, theta0, theta1)

theta0 = 0.0
theta1 = 0.0

if __name__ == '__main__':
    main()
