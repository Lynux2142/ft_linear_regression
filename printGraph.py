#!/usr/bin/python3

from pylab import *

def printGraph(km, price, theta0, theta1):
    scatter(km, price)
    xlabel('km')
    ylabel('price')
    lineX = [min(km), max(km)]
    lineY = [theta1 * float(i) + theta0 for i in lineX]
    plot(lineX, lineY)
    show()
