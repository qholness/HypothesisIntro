def fib(n):
    if n == 0:
        return n
    if n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


def EuclideanDistance(coord1, coord2):
	x_dif = coord2[0] - coord1[0]
	y_dif = coord2[1] - coord1[1]
	return (x_dif ** 2 + y_dif ** 2) * .5


def GetMean(array):
	return sum(array)/len(array)


def GetStdev(array, mean: int=None):
	if mean is None:
		mean = GetMean(array)
	n = len(array)
	SumSquares = sum(map(lambda x: (x - mean) ** 2, array))
	return (SumSquares/(n - 1)) ** .5


def GetBetaCoefficient(yarray, xarray):
	n = len(xarray)
	SumProduct = sum(y * x for y, x in zip(yarray, xarray))
	SumSquaresX = sum(x * x for x in xarray)
	SquareOfSum = (1/n) * sum(xarray) ** 2
	CovarianceXY = SumProduct - ((1/n)*sum(xarray)*sum(yarray))
	VarianceX = SumSquaresX - SquareOfSum
	return CovarianceXY / VarianceX

# Come up with a few more mathematical expressions to test