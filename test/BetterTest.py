"""
State-based Testing Approach
Thesis:
	An improved and rather automated method of state-based
	testing.
"""


from hypothesis import given
from hypothesis import settings
from hypothesis import strategies as ST
from hypothesis.extra.pandas import data_frames, column
import unittest
import pandas as pd
import PandasTransforms as transforms
import Math


# hypothesis.given: main entry point for using Hypothesis.
	# A wrapper utility for tests.
	# Takes "SearchStrategy" objects (can define your own. More detail on that in the docs)

# hypothesis.settings: test settings
	# Can define test settings like number of examples, hypothesis health_checks and other settings

# hypothesis.strategies: SearchStrategies
	# What kind of data is generated for the test.
	# Can refine the parameters.

# hypothesis.extra
	# Extra tools for popular Data Science and math packages.
	# More details in the docks


class Test(unittest.TestCase):

	# Test fibonnaci sequence on first 10 integers
	@given(
		ST.integers(0, 10)
	)
	def test_00_fib_first_10(self, n):
		Math.fib(n)


	# Test fibonnaci sequence on negative numbers,
	# breaking one of the assumptions of the function
	# (no negative values)
	@given(
		ST.integers(max_value=-1)
	)
	def test_01_fib_negative_values(self, n):
		Math.fib(n)

	# Test BetaCoefficient functionality
	@given(
		n=ST.integers(),
		Y=ST.lists(ST.floats()),
		X1=ST.lists(ST.floats())
	)
	def test_03_BetaCoefficient(self, n, Y, X1):
		beta = Math.GetBetaCoefficient(Y, X1)
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
		Math.EuclideanDistance(coord1, coord2)


	# Test simple pandas transpose
	@given(data_frames(
		[
			column('a', dtype=int),
			column('b', dtype=int),

		]))
	def test_05_transpose(self, df):
		transforms.transpose(df)


	# Test the creation of a geographic distance matrix
	# Building on euclidean distance, let's test a higher order function.
	@given(data_frames([
		column('lat', dtype=float),
		column('lon', dtype=float)
	]))
	def test_06_DistanceMatrixGeneration(self, df):
		df['store_id'] = [_ for _ in range(len(df))]
		transforms.CreateDistanceMatrix(df)


if __name__ == '__main__':
	unittest.main()
