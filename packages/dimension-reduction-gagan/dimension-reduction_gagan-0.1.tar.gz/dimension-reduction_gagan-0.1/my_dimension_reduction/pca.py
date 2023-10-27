import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from logs import logger


def reduce_dimensionality_with_pca(data, n_components=2):
    """
    Reduce the dimensionality of the input data using Principal Component Analysis (PCA).

    Parameters:
    - data: The input dataset (numpy array or pandas DataFrame).
    - n_components: The number of principal components to retain (default is 2).

    Returns:
    - Reduced dimensionality data.
    """
    try:
        if not isinstance(data, (np.ndarray, pd.DataFrame)):
            raise ValueError("Input data should be a numpy array or a pandas DataFrame.")

        # Initialize a PCA object
        pca = PCA(n_components = n_components)

        # Fit the PCA model to the data and transform the data to the new feature space
        reduced_data = pca.fit_transform(data)

        logger.info(f"PCA: Reduced data from {data.shape[1]} to {n_components} dimensions.")
        return reduced_data
    except Exception as e:
        logger.error(f"PCA Error: {str(e)}")
        raise
