from typing import List


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]


if __name__ == '__main__':
    twoSum = Solution()
    print(twoSum.two_sum([3, 2, 4], 6))
    
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Crisil question test cases.
Author: Ikram Ulhaq
"""

import unittest
from solutions import *


class Testing(unittest.TestCase):

    def setUp(self):
        self.movavg = movavg
        self.orangePurchase1 = orangePurchase1
        self.orangePurchase2 = orangePurchase2
        self.orangePurchase3 = orangePurchase3

    def test_movavg_100randomnumbers_over5(self):
        """Run standard moving average graph for 100 numbers over 5 pts to avg:ok"""
        f = [value for value in np.random.randint(0, 100, size=50)]
        self.assertEqual( self.movavg(f,5), "ok")

    def test_movavg_100randomnumbers_invalidAvgValues(self):
        """Run standard moving average graph for 100 numbers use invalid avg values:Exception"""
        f = [value for value in np.random.randint(0, 100, size=50)]
        self.assertEqual( self.movavg(f,"x"), "Exception")

    def test_movavg_100randomnumbers_invalidDataSet(self):
        """Run standard moving average graph for 100 numbers use invalid dataset:Exception"""
        f = [100,200,300,400,'x']
        self.assertEqual( self.movavg(f,5), "Exception")

    def test_orangePurchase1_0(self):
        """Run orangePurchase1 test for money value of 0"""
        self.assertEqual( self.orangePurchase1(0), 0)

    def test_orangePurchase1_1(self):
        """Run orangePurchase1 test for money value of 1"""
        self.assertEqual( self.orangePurchase1(1), 1)

    def test_orangePurchase1_1000(self):
        """Run orangePurchase1 test for money value of 1000"""
        self.assertEqual( self.orangePurchase1(1000), 44)

    def test_orangePurchase2_0(self):
        """Run orangePurchase2 test for money value of 0"""
        self.assertEqual( self.orangePurchase2(0), 0)

    def test_orangePurchase1_2(self):
        """Run orangePurchase2 test for money value of 1"""
        self.assertEqual( self.orangePurchase2(1), 1)

    def test_orangePurchase2_1000(self):
        """Run orangePurchase2 test for money value of 1000"""
        self.assertEqual( self.orangePurchase2(1000), 9)

    def test_orangePurchase3_0_PriceFunction1(self):
        """Run orangePurchase3 test for money value of 0"""
        priceFunction1 = lambda x: x
        self.assertEqual( self.orangePurchase3(0,priceFunction1), 0)

    def test_orangePurchase3_2_PriceFunction1(self):
        """Run orangePurchase3 test for money value of 1"""
        priceFunction1 = lambda x: x
        self.assertEqual( self.orangePurchase3(1,priceFunction1), 1)

    def test_orangePurchase3_1000_PriceFunction1(self):
        """Run orangePurchase3 test for money value of 1000"""
        priceFunction1 = lambda x: x
        self.assertEqual( self.orangePurchase3(1000,priceFunction1), 44)

    def test_orangePurchase3_0_PriceFunction2(self):
        """Run orangePurchase3 test for money value of 0"""
        priceFunction2 = lambda x: 1 * 2 ** (x - 1)
        self.assertEqual( self.orangePurchase3(0,priceFunction2), 0)

    def test_orangePurchase3_2_PriceFunction2(self):
        """Run orangePurchase3 test for money value of 1"""
        priceFunction2 = lambda x: 1 * 2 ** (x - 1)
        self.assertEqual( self.orangePurchase3(1,priceFunction2), 1)

    def test_orangePurchase3_1000_PriceFunction2(self):
        """Run orangePurchase3 test for money value of 1000"""
        priceFunction2 = lambda x: 1 * 2 ** (x - 1)
        self.assertEqual( self.orangePurchase3(1000,priceFunction2), 9)

if __name__ == '__main__':
    unittest.main()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def movavg(f,w):
    """
    Function which returns the moving average of a randomly generated set of values f, where w is the number of values over which to average.
    Plot the result together with the original values.

    :param f: numpy array of random integers between 0 and 100
    :param w: number of values to average over
    :return: ok if processed, exception if invalid input
    """

    if not isinstance(w, int):
        print('number of values to average over is not an integer')
        return 'Exception'

    dataset={}
    dataset['datapoints'] = [posn for posn in range(len(f))]
    dataset['randomdata'] = f
    df = pd.DataFrame(dataset)

    # Create on the fly key and label
    ma_key   = 'SMA_' + str(w)
    ma_label = 'SMA ' + str(w) + ' Months'

    # Work out moving Average based on number of values to average over
    try:
        df[ma_key] = df.iloc[:, 1].rolling(window=w).mean()
    except:
        print("DataFrame could not be generated - invalid data set")
        return 'Exception'

    plt.plot(df['randomdata'], linestyle='--', marker='.', label='Original Data')
    plt.plot(df[ma_key], marker='o', linewidth=3, label=ma_label)

    plt.xlabel('Data Point')
    plt.ylabel('Moving Average')
    plt.title("Moving Average over Data Points")
    plt.legend(loc=2)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return "ok"


def orangePurchase1(m):
    """
    Calculate how many oranges can be bought with a set amount of
    money. The first orange costs 1, and each subsequent costs 1 more than the previous
    (the second costs 2, the third costs 3, and so on).

    :param m:total amount of money available (nb m<2,147,483,647)
    :return:total number of oranges which can be purchased
    """
    if m in [0, 1]:
        return m
    total = 0
    #first term in series
    value = 1
    #difference between each term
    difference=1
    #calculate sum of arithmetic progression of prices until money limit is broken
    for number_of_oranges in range(m):
        total = total + value
        value = value + difference
        if total > m:
             break
    return number_of_oranges


def orangePurchase2(m):
    """
    Calculate how many oranges can be bought with a set amount of
    money. The first orange costs 1, and each subsequent exponentially costs more than the previous
    (the second costs 2, the third costs 4, and so on).

    :param m:total amount of money available (nb m<2,147,483,647)
    :return:total number of oranges which can be purchased
    """
    if m in [0, 1]:
        return m
    total = 0
    #first term in series
    value = 1
    #calculate sum of Geometric sequence of prices until money limit is broken
    for number_of_oranges in range(0, m):
        total = total + value
        value = 2 ** number_of_oranges-1
        if total == m:
             return number_of_oranges
        elif total>m:
            #Current total breaks the money limit, hence use previous  orange count which didnt break limit
            return number_of_oranges-1


def orangePurchase3(m,priceFunction):
    """
     Calculate number of oranges that can be purchased for quantity of money m
     given the (user-defined) price function priceFunction for each orange.

     :param m:total amount of money available (nb m<2,147,483,647)
     :param priceFunction: points to a pricer function = price of nth orange
     :return:total number of oranges which can be purchased
     """
    if m in [0, 1]:
        return m
    total = 0
    no_of_oranges = 1
    while total <= m:
         total = total + priceFunction(no_of_oranges)
         if total == m:
             return no_of_oranges
         elif total > m:
             # Current total breaks the money limit, hence use previous  orange count which didnt break limit
             return no_of_oranges - 1
         no_of_oranges=no_of_oranges+1
    return no_of_oranges


print(orangePurchase1(3))
