import numpy as np
import pandas as pd
from sklearn.random_projection import GaussianRandomProjection, SparseRandomProjection
from logs import logger

def reduce_dimensionality_with_random_projection(data, n_components=2, dense=True):
    try:
        if not isinstance(data, (np.ndarray, pd.DataFrame)):
            raise ValueError("Input data should be a numpy array or a pandas DataFrame.")

        if dense:
            transformer = GaussianRandomProjection(n_components=n_components)
        else:
            transformer = SparseRandomProjection(n_components=n_components)

        reduced_data = transformer.fit_transform(data)

        if dense:
            logger.info(f"Dense Random Projection: Reduced data to {n_components} dimensions.")
        else:
            logger.info(f"Sparse Random Projection: Reduced data to {n_components} dimensions.")

        return reduced_data
    except Exception as e:
        if dense:
            logger.error(f"Dense Random Projection Error: {str(e)}")
        else:
            logger.error(f"Sparse Random Projection Error: {str(e)}")
        raise
