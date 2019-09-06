#!/usr/bin/python3

import sys
import csv
from printGraph import printGraph

def normalizeData(data):
    newData = []

    for row in data:
        newData.append([row[0] / 100000, row[1] / 100000])
    return (newData)

def revNormalize(value):
    return (value * 100000)

def estimatePrice(mileage):
    return (theta0 + theta1 * mileage)

def learnFunction(data):
    global theta0
    global theta1
    learningRate = float(0.01)

    for _ in range(0, 100):
        tmpTheta0 = float(0)
        tmpTheta1 = float(0)

        for row in data:
            tmpTheta0 += (estimatePrice(row[0]) - row[1])
            tmpTheta1 += (estimatePrice(row[0]) - row[1]) * row[0]
        theta0 = theta0 - learningRate * (1 / len(data)) * tmpTheta0
        theta1 = theta1 - learningRate * (1 / len(data)) * tmpTheta1
        print(theta0, theta1)

def main():
    data = []

    with open('data.csv', newline='') as f:
        csv_data = list(csv.reader(f, delimiter = ','))
        data_size = float(len(csv_data))
        for row in range(1, len(csv_data)):
            data.append([float(csv_data[row][0]), float(csv_data[row][1])])
    data = normalizeData(data)
    learnFunction(data)
    printGraph([row[0] for row in data], [row[1] for row in data], revNormalize(theta0), revNormalize(theta1))
    print(revNormalize(theta0), revNormalize(theta1))
    return (0)

theta0 = float(0)
theta1 = float(0)

if __name__ == "__main__":
    main()
