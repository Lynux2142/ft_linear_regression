#!/usr/bin/python3

import sys
import csv
from printGraph import printGraph

def normalizeData(data):
    newData = []

    for row in data:
        newData.append([row[0] / 100000.0, row[1] / 100000.0])
    return (newData)

def revNormalize(value):
    return (value * 100000)

def estimatePrice(mileage):
    return (theta0 + theta1 * mileage)

def learnFunction(data):
    global theta0
    global theta1
    learningRate = float(0.01)

    for _ in range(0, 10000):
        tmpTheta0 = float(0)
        tmpTheta1 = float(0)

        for row in data:
            tmpTheta0 += (estimatePrice(row[0]) - row[1])
            tmpTheta1 += (estimatePrice(row[0]) - row[1]) * row[0]
        theta0 -= learningRate * (1 / len(data)) * tmpTheta0
        theta1 -= learningRate * (1 / len(data)) * tmpTheta1

def main():
    global theta0
    global theta1
    data = []

    with open('Data.csv', newline='') as f:
        csv_data = list(csv.reader(f, delimiter = ','))
        data_size = float(len(csv_data))
        for row in range(1, len(csv_data)):
            data.append([float(csv_data[row][0]), float(csv_data[row][1])])
    data = normalizeData(data)
    learnFunction(data)
    theta0 = revNormalize(theta0)
    print(theta0, theta1)
    print(estimatePrice(84000.0))
    printGraph([revNormalize(row[0]) for row in data], [revNormalize(row[1]) for row in data], theta0, theta1)
    return (0)

theta0 = float(0)
theta1 = float(0)

if __name__ == "__main__":
    main()
