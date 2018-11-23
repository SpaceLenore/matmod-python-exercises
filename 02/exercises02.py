#!/usr/bin/env python3
"""
Matmod exercise 02

ported to python by https://github.com/SpaceLenore
"""

import math

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

def factorial(n):
    """ Calculate the factorial of the integer n """
    val = 1
    for value in range(1, n + 1):
        val = val * value
    return val

def bin(trials, population, probability):
    """ Calculate the probability binomial distribution Pr(X = x) """
    # x = trials
    # n = population
    # p = probability
    bern = ((1 - probability)**(population-trials))*probability**trials
    bincof = factorial(population) / (factorial(trials) * factorial(population - trials))
    binpro = bern * bincof
    return round(binpro, 3)

def cumulative_bin(trials, population, probability):
    """  Calculate the probability binomial distribution Pr(X <= x) """
    # x = trials
    # n = population
    # p = probability
    sumtotal = 0;
    for xval in range(trials + 1):
        sumtotal += bin(xval, population, probability)
    return round(sumtotal, 3)
