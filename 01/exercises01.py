#!/usr/bin/env python3
"""
Matmod exercise 01

ported to python by https://github.com/SpaceLenore
"""
import math

def mean(numbers):
    """
    Calculate the mean of an array of numbers
    """
    sumOfNumbers = 0
    for number in numbers:
        sumOfNumbers += number
    res = sumOfNumbers / len(numbers)
    return round(res, 2)

def variance(numbers):
    """
    Calculate the sample variance of an array of numbers
    """
    xMean = mean(numbers)
    totalSum = 0

    for x in numbers:
        tmp = (x - xMean)**2
        totalSum += tmp

    final = totalSum / (len(numbers) - 1)


    return round(final, 2)


def stddev(numbers):
    """
    Calculate the sample standard deviation of an array of numbers
    """

    return round(math.sqrt(variance(numbers)), 2)
