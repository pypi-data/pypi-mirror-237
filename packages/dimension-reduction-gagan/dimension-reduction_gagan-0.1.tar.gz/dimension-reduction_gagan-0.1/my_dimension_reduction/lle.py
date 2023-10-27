import numpy as np
import pandas as pd
from sklearn.manifold import LocallyLinearEmbedding
from logs import logger


def reduce_dimensionality_with_lle(data, n_components=2, n_neighbors=10):
    try:
        if not isinstance(data, (np.ndarray, pd.DataFrame)):
            raise ValueError("Input data should be a numpy array or a pandas DataFrame.")

        lle = LocallyLinearEmbedding(n_neighbors=n_neighbors, n_components=n_components)
        reduced_data = lle.fit_transform(data)

        logger.info(f"LLE: Reduced data to {n_components} dimensions with {n_neighbors} neighbors.")
        return reduced_data
    except Exception as e:
        logger.error(f"LLE Error: {str(e)}")
        raise
