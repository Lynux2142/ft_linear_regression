#!/usr/local/bin/python3

from csv import reader
from pylab import *
from math import *

def printGraph(data, cost, theta0, theta1, point = None):
    scatter([row[0] for row in data[1:]], [row[1] for row in data[1:]], zorder = 1)
    xlabel(data[0][0])
    ylabel(data[0][1])
    lineX = [min([row[0] for row in data[1:]]), max([row[0] for row in data[1:]])]
    lineY = [theta1 * float(i) + theta0 for i in lineX]
    plot(lineX, lineY, 'orange', zorder = 2, label = 'y = {}x + {}'.format(round(theta1, 4), round(theta0, 4)))
    legend(loc = 'upper left')
    if (point):
        scatter(point[0], point[1], c = 'red', zorder = 3)
    show()
    plot(range(len(cost)), cost)
    show()

def dataset_minmax(data):
    minmax = []
    data_x = [row[0] for row in data[1:]]
    data_y = [row[1] for row in data[1:]]
    minmax.append([min(data_x), max(data_x)])
    minmax.append([min(data_y), max(data_y)])
    return (minmax)

def normalize_elem(elem, minmax, size):
    return ((size[1] - size[0]) * ((elem - minmax[0]) /
        (minmax[1] - minmax[0])) + size[0])

def rev_normalize_elem(elem, minmax, size):
    return (((elem - size[0]) * (minmax[1] - minmax[0]) +
        (size[1] - size[0]) * minmax[0]) / (size[1] - size[0]))

def normalize_data_set(norm_funct, data, minmax, size):
    for row in range(1, len(data)):
        for elem in range(0, len(data[row])):
            data[row][elem] = norm_funct(data[row][elem], minmax[elem], size)

def load_file(filename):
    try:
        file = open(filename, "r")
    except IOError as e:
        print('error: {}'.format(e.strerror))
        sys.exit(2)
    try:
        lines = reader(file)
        data = list(lines)
    except:
        print('error: cannot convert data to list')
        exit(4)
    for row in data[1:]:
        try:
            assert (len(row) == 2)
        except:
            print("error: data must have 2 columns")
            sys.exit(5)
        for i in range(len(row)):
            try:
                row[i] = float(row[i].strip())
            except:
                print(f'"{row[i].strip()}" not a float')
                sys.exit(3)
    file.close()
    if (not data or len(data) <= 2):
        print('error: not enough data')
        sys.exit(1)
    return (data)

def save_thetas(theta0, theta1):
    try:
        file = open('thetas', 'w+')
        file.write('{}\n{}\n'.format(str(theta0), str(theta1)))
        file.close()
    except IOError as e:
        print('error: {}'.format(e.strerror))
        sys.exit(1)
    except:
        print('error')
        sys.exit(2)

def get_thetas():
    try:
        file = open('thetas', 'r')
        theta0 = float(file.readline())
        theta1 = float(file.readline())
        file.close()
    except IOError as e:
        print('error: {} {}'.format(e.strerror, "'thetas'"))
        sys.exit(1)
    except:
        print('error')
        sys.exit(2)
    return (theta0, theta1)

def linear_correlation(data):
    data_len = float(len(data))
    data_x = [row[0] for row in data]
    data_y = [row[1] for row in data]
    sum_x = sum(data_x)
    square_sum_x = sum([elem ** 2 for elem in data_x])
    sum_y = sum(data_y)
    square_sum_y = sum([elem ** 2 for elem in data_y])
    sum_x_y = sum([(row[0] * row[1]) for row in data])
    return (((data_len * sum_x_y - (sum_x * sum_y)) /
            (sqrt(data_len * square_sum_x - sum_x ** 2) *
            sqrt(data_len * square_sum_y - sum_y ** 2))) ** 2)
