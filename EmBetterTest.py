"""
State-based Testing Approach
Thesis:
	An improved and rather automated method of state-based
	testing.
"""



from MyMath import fib, EuclideanDistance, GetBetaCoefficient
from hypothesis import strategies as ST
from hypothesis import given, settings
from hypothesis.extra.pandas import data_frames, column
import unittest
import pandas as pd
import PandasOps as ops


class Test(unittest.TestCase):

	# Test fibonnaci sequence on first 10 integers
	@given(
		ST.integers(0, 10)
	)
	def test_00_fib_first_10(self, n):
		fib(n)


	# Test fibonnaci sequence on negative numbers,
	# breaking one of the assumptions of the function
	# (no negative values)
	@given(
		ST.integers(max_value=-1)
	)
	def test_01_fib_negative_values(self, n):
		fib(n)

	# Test BetaCoefficient functionality
	@given(
		n=ST.integers(),
		Y=ST.lists(ST.floats()),
		X1=ST.lists(ST.floats())
	)
	def test_03_BetaCoefficient(self, n, Y, X1):
		beta = GetBetaCoefficient(Y, X1)
		print(beta)


	# Test unbound plane with 1000 different examples
	@settings(
		max_examples=1000
	)
	@given(
		coord1=ST.tuples(ST.floats(), ST.floats()),
		coord2=ST.tuples(ST.floats(), ST.floats())
	)
	def test_04_EuclideanDistance_unbound(self, coord1, coord2):
		EuclideanDistance(coord1, coord2)


	# Test simple pandas transpose
	@given(data_frames(
		[
			column('a', dtype=int),
			column('b', dtype=int),

		]))
	def test_05_transpose(self, df):
		ops.transpose(df)


	# Test the creation of a geographic distance matrix
	# Building on euclidean distance, let's test a higher order function.
	@given(data_frames([
		column('lat', dtype=float),
		column('lon', dtype=float)
	]))
	def test_06_DistanceMatrixGeneration(self, df):
		df['store_id'] = [_ for _ in range(len(df))]
		ops.CreateDistanceMatrix(df)


	def test_10_ShipIt(self):
		# Get some pig ascii art here
		pass


if __name__ == '__main__':
	unittest.main()
