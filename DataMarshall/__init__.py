def MarshallFib(b):
	if b > 0:
		return True
	return False


def MarshallEuclid(coord1, coord2, max_value=1e7):
	for x, y in zip(coord1, coord2):
		if x > max_value or y > max_value:
			return False
		if x < -max_value or y < -max_value:
			return False
	return True


def MarshallMean(array):
	if len(array) > 0:
		return True
	return False


def MarshallStDev(array):
	return MarshallMean(array)


def MarshallBeta(Y, X):
	if MarshallMean(Y):
		if MarshallMean(X):
			return True
	return False
