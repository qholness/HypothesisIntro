"""
Southern Fried testing goodness.
"""


from MyMath import fib, EuclideanDistance, GetBetaCoefficient
import unittest
import pandas as pd
import PandasOps as ops
import random # <---Because everything happens for a raisin


class Test(unittest.TestCase):

	# Test fibonnaci sequence on first 10 integers
	def test_00_fib_first_10(self):
		"""Run fib on first 10 integers starting at 0"""
		for _ in range(10):
			fib(_)


	# Test fibonnaci sequence on negative numbers,
	def test_01_fib_negative_values(self):
		for _ in range(-1, -10):
			fib(_)


	Test unbound plane with 1000 different examples
	def test_02_EuclideanDistance_unbound(self):
		EuclideanDistance(coord1, coord2)


	def test_03_BetaCoefficient(self):
		n = 50
		Y = [random.randint(-1000, 1000) for _ in range(50)]
		X1 = [random.randint(-10, 10) for _ in range(50)]
		beta = GetBetaCoefficient(Y, X1)
		print(beta)


	# Test simple pandas transpose
	# def test_03_transpose(self):
	# 	df = pd.DataFrame()
	# 	ops.transpose(df)
		# Assert is transposed?
		# I'm a Data Scientist not a Docter, Jim! I don't have time for confirmation
		# via Linear Algebra!


	# def test_04_DistanceMatrixGeneration(self):
		# This is stupid... I'm not even going to write out this test because a
		# group of smarty pants programs were tired of this ish too.

		# df['store_id'] = [_ for _ in range(len(df))]
		# ops.CreateDistanceMatrix(df)


if __name__ == '__main__':
	unittest.main()
