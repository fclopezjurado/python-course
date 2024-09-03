"""Random number generator"""
__author__ = "Fran López"
__version__ = "1.0"

from math import exp


def uniform():
    """Generate a random_numbers number between 0 and 1"""
    a, m = 16807, 2147483647
    q = m // a
    r = m % a
    global z
    g = a * (z % q) - r * (z // q)

    if g > 0:
        z = g
    else:
        z = g + m

    return z / m


def exponential(tao):
    x = uniform()

    return exp(-(x / tao))


def normal(med, var):
    x = uniform()

    return exp(-(x - med) / var)


def initSeed(seed):
    global z
    z = seed


if __name__ == "__main__":
    z = int(input("Seed initial value: "))
