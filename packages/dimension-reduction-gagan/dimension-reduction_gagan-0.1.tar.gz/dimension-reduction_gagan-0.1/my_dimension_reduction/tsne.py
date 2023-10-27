import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
from logs import logger


def reduce_dimensionality_with_tsne(data, n_components=2, perplexity=30, learning_rate=200):
    try:
        if not isinstance(data, (np.ndarray, pd.DataFrame)):
            raise ValueError("Input data should be a numpy array or a pandas DataFrame.")

        tsne = TSNE(n_components=n_components, perplexity=perplexity, learning_rate=learning_rate)
        reduced_data = tsne.fit_transform(data)

        logger.info(
            f"t-SNE: Reduced data to {n_components} dimensions with perplexity {perplexity} and learning rate {learning_rate}.")
        return reduced_data
    except Exception as e:
        logger.error(f"t-SNE Error: {str(e)}")
        raise
