from MyMath import EuclideanDistance
import pandas as pd
import numpy as np

def transpose(df):
	return df.T


def CreateDistanceMatrix(df):
	# A dataframe of stores and geographic coordinates
	store_count = len(df.store_id.unique())
	result_array = np.empty((store_count, store_count))
	zipped_vector = zip(df.store_id, df.lat, df.lon)
	for store, lat, lon in zipped_vector:
		for store2, lat2, lon2 in zipped_vector:
			if store != store2:
				result_array[store][store2] = \
					EuclideanDistance((lat, lon), (lat2, lon2))
	result_array = pd.DataFrame(result_array)
	return result_array
