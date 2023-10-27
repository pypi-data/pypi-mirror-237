import numpy as np
import pandas as pd
from sklearn.manifold import MDS
from logs import logger


def reduce_dimensionality_with_mds(data, n_components=2, dissimilarity="euclidean"):
    try:
        if not isinstance(data, (np.ndarray, pd.DataFrame)):
            raise ValueError("Input data should be a numpy array or a pandas DataFrame.")

        mds = MDS(n_components=n_components, dissimilarity=dissimilarity)
        reduced_data = mds.fit_transform(data)

        logger.info(f"MDS: Reduced data to {n_components} dimensions using {dissimilarity} dissimilarity.")
        return reduced_data
    except Exception as e:
        logger.error(f"MDS Error: {str(e)}")
        raise
