#!/usr/local/bin/python3

import sys
from tools import get_thetas

def estimatePrice(value):
    return (theta0 + theta1 * value)

def main():
    global theta0
    global theta1

    theta0, theta1 = get_thetas()
    try:
        value = float(input('value: '))
    except:
        print('error: value')
        sys.exit(3)
    print(estimatePrice(value))

theta0 = 0.0
theta1 = 0.0

if __name__ == '__main__':
    main()
