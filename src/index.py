"""Implement your own index following https://arxiv.org/abs/2005.11401 equation 2.2."""

import numpy as np


class Index(object):
    """Define the search index class."""

    def __init__(self):
        """Set up the index and creates a list for embedding vectors."""
        self.content_embedding_vectors = []

    def add(self, new_vector_embeddings: np.ndarray):
        """Add new embedding content_embedding_vectors by extending the `content_embedding_vectors` list.

        Args:
            new_vector_embeddings (np.ndarray): New embeddings we want to store.
        """
        # Add content_embedding_vectors to the index
        self.content_embedding_vectors.extend(new_vector_embeddings)

    def search(self, query: np.ndarray, k: int = 5):
        """Compare the similarity of the internal storage and the incoming query vector.

        Args:
            query (np.ndarray): The incoming query embedding of shape (query no. , embedding_size)
            k (int): The number of similar content_embedding_vectors we would like to find.
                Defaults to 5.

        Returns:
            tuple: The dissimilarity values and their positions in the similarity matrix.
        """
        content_embedding_vectors = np.stack(self.content_embedding_vectors, axis=0)

        # Use the @ operator to compute the similarity matrix of embeddings and query matrices.
        # Find the indices of the most similar elements using np.argsort,
        # and use np.take_along_axis to get the corresponding values.
        # Return dissimilarity (1 - similarity) and the indices.
        return None, None # TODO: return proper values instead of None.
