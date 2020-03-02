class Singleton(object):
    _instance = None
    __iterator = 1

    def __new__(cls):
        print('++++++++++++++++++++++++++++++++++++++++++')
        if not cls._instance:
            Singleton.__iterator = Singleton.__iterator + 4
            cls._instance = super(Singleton, cls).__new__(cls)

    def getIncrementedValue(cls):

        if Singleton.__iterator is not 0:
            print('######################')
            Singleton.__new__(cls)
            Singleton._instance = None
        return Singleton.__iterator


if __name__ == '__main__':
    for i in range(60):
        # s1 = Singleton()
        print(Singleton.getIncrementedValue(Singleton))
###################################################################################################
# Using Python version 3.8.1
import sys
from numpy.random import shuffle
import numpy as np
import matplotlib.pyplot as plt
import unittest

"""
Calculate the moving average and plot

Args:
  f: input Values
  w : number of values over which to average. 
Returns:
   x :The moving average of a set of values 
Raises:
  Exception: System exception
"""
def movavg(f, w):
    try:
        x = []

        #Check for non-zero input
        if len(f) <= 0:
            return x

        #Check for value over to average
        if w <= 0 or w > len(f):
            return x

        x = np.convolve(f, np.ones(w), 'same') / w
        y = [i + 1 for i in range(len(f))]
        print("Moving average of f with value w over to average : " + str(x))
        # Create a figure canvas with X axis as Points and Y axis as sequence indexes
        fig, axs = plt.subplots()
        axs.plot(x, y, label="Moving average")
        axs.plot(f, y, label="Original")

        # Add legend to plot
        axs.legend()
        plt.show(block=False)
        plt.pause(3)
        plt.close()
        return x
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


"""
Calculate the number of oranges purchasd with money m using linear function

Args:
  m: Money less than sys.maxsize
Returns:
  n: the number of oranges purchased with money m
Raises:
  Exception: System exception
"""
def orangePurchase1(m):
    try:
        # Check for sys maxsize as Ints are unbounded
        if m >= sys.maxsize:
            print("Too large value received, exiting")
            return None
        if m <= 0:
            print("Zero or negative value received, exiting")
            return None
        n = 0
        price = 1
        sum = 0
        while sum <= m:
            sum += price
            price += 1
            if sum <= m:
                n += 1
        print('No. of oranges you can buy :' + str(n) + ' using  orangePurchase1 function')
        return n
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

"""
Calculate the number of oranges purchased with money m using exponential function

Args:
  m: Money less than sys.maxsize
Returns:
  n: the number of oranges purchased with money m
Raises:
  Exception: System exception
"""
def orangePurchase2(m):
    try:
        # Check for sys maxsize as Ints are unbounded
        if m >= sys.maxsize:
            print("Too large value received, exiting")
            return None
        if m <= 0:
            print("Negative value received, exiting")
            return None
        n = 0
        price = 1
        sum = 0
        powerOf2 = 1
        while sum <= m:
            sum += price
            # print("PowerOf2:" + str(2 ** price-1))
            price += 2 ** (powerOf2 - 1)
            powerOf2 += 1
            if sum <= m:
                n += 1
        print('No. of oranges you can buy :' + str(n) + ' using  orangePurchase2 function')
        return n
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

"""
Calculate the price of nth orange using linear function

Args:
  n: Nth orange item whose price is needed
Returns:
  n: Price of nth orange
Raises:
  Exception: System exception
"""
def priceFunction1(n):
    try:
        # Check for sys maxsize as Ints are unbounded
        if n <= 0 or n >= sys.maxsize:
            print("Value out of range, exiting: ", n)
            return None
        else:
            print("Price of {}th orange is : {} using priceFunction1".format(n, n))
            return n
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

"""
Calculate the price of nth orange using exponential function

Args:
  n: Nth orange item whose price is needed
Returns:
  n: Price of nth orange
Raises:
  Exception: System exception
"""
def priceFunction2(n):
    try:
        # Check for values in range of 1 to 2**31 ( value less than sys maxsize)
        if n <= 0 or n > 31:
            print("Value out of range, exiting")
            return None
        else:
            result = 2 ** n
            print("Price of {}th orange is : {} using priceFunction1".format(n, result))
            return result
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


"""
Calculate the price of nth orange using linear & exponential function passed as 2nd argument

Args:
  m: Money to buy oranges
  priceFunction: Calls priceFunction1 or priceFunction2 depending upon the call
Returns:
  n: the number of oranges purchased with money m
Raises:
  Exception: System exception
"""
def orangePurchase3(m, priceFunction):
    try:
        n = 0
        if priceFunction == priceFunction1:
            n = orangePurchase1(m)
            print("Calling orangePurchase1")
        elif priceFunction == priceFunction2:
            n = orangePurchase2(m)
        print('No. of items you can buy :' + str(n) + ', now calling ' + str(priceFunction))
        priceFunction(n)
        return n
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


"""
Unit testing using unittest

Test cases to test all requirements with posiive and negative scenarios.
"""
class TestSolution(unittest.TestCase):
    def test_moving_average(self):
        # prepare a sequence of values and shuffle
        f = [i for i in range(20)]
        shuffle(f)
        print("Random values array: " + str(f))

        #1) Positive scenario - Moving average plot
        ma = movavg(f, 4)
        #Assert for length of random values and moving average values to be equal for plotting.
        self.assertEqual(len(ma), len(f))

        #2) Negative scenario - Zero Length array
        self.assertEqual(len(movavg([], 4)), 0)

        #2) Negative scenario - Zero Length array
        self.assertEqual(len(movavg(f, len(f)+1)), 0)


    def test_orangePurchase1(self):
        #Negative Testcases
        self.assertEqual(orangePurchase1(-5), None)
        self.assertEqual(orangePurchase1(0), None)
        self.assertEqual(orangePurchase1(sys.maxsize), None)

        # Positve Testcases
        self.assertEqual(orangePurchase1(sys.maxsize - 1), 65535)
        self.assertEqual(orangePurchase1(12), 4)


    def test_orangePurchase2(self):
        #Negative Testcases
        self.assertEqual(orangePurchase2(-5), None)
        self.assertEqual(orangePurchase2(0), None)
        self.assertEqual(orangePurchase2(sys.maxsize), None)

        # Positve Testcases
        self.assertEqual(orangePurchase2(sys.maxsize - 1), 30)
        self.assertEqual(orangePurchase2(12), 3)


    def test_orangePurchase3(self):
        # Negative Testcases
        self.assertEqual(priceFunction1(-5), None)
        self.assertEqual(priceFunction1(0), None)
        self.assertEqual(priceFunction1(sys.maxsize), None)

        # Positive Testcases
        self.assertEqual(priceFunction1(sys.maxsize-1), 2147483646)
        self.assertEqual(priceFunction1(44), 44)

        # Negative Testcases
        self.assertEqual(priceFunction2(-5), None)
        self.assertEqual(priceFunction2(0), None)
        self.assertEqual(priceFunction2(32), None)

        # Positive Testcases
        self.assertEqual(priceFunction2(30), 1073741824)
        self.assertEqual(priceFunction2(31), 2147483648)
        self.assertEqual(priceFunction2(9), 512)

        # Positive Testcases
        self.assertEqual(orangePurchase3(1000, priceFunction1), 44)
        self.assertEqual(orangePurchase3(1000, priceFunction2), 9)


# Main with call to unittest class
if __name__ == '__main__':
    unittest.main()
