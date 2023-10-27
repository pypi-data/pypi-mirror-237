from my_dimension_reduction.pca import reduce_dimensionality_with_pca
from my_dimension_reduction.random_projection import reduce_dimensionality_with_random_projection
from my_dimension_reduction.lle import reduce_dimensionality_with_lle
from my_dimension_reduction.mds import reduce_dimensionality_with_mds
from my_dimension_reduction.isomap import reduce_dimensionality_with_isomap
from my_dimension_reduction.tsne import reduce_dimensionality_with_tsne
from logs import logger
# Define a dictionary to map technique names to their corresponding functions
techniques = {
    "pca": reduce_dimensionality_with_pca,
    "random_projection": reduce_dimensionality_with_random_projection,
    "lle": reduce_dimensionality_with_lle,
    "mds": reduce_dimensionality_with_mds,
    "isomap": reduce_dimensionality_with_isomap,
    "tsne": reduce_dimensionality_with_tsne,
}


def reduce_dimensionality(data, technique="pca", n_components=2):
    try:
        if technique not in techniques:
            raise ValueError("Invalid technique. Choose from: " + ", ".join(techniques.keys()))

        reducer = techniques[technique]
        reduced_data = reducer(data, n_components)

        logger.info(f"{technique.upper()}: Reduced data to {n_components} dimensions.")
        return reduced_data
    except Exception as e:
        logger.error(f"Dimension Reduction Error: {str(e)}")
        raise
