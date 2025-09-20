"""Test the document search."""

import sys

sys.path.insert(0, "./src/")

import faiss
import numpy as np

from src.index import Index


def test_index():
    """Test our index by comparing to the faiss implementation."""
    # follow
    # https://github.com/facebookresearch/faiss/wiki/Getting-started
    d = 32  # dimension
    nb = 100  # database size
    nq = 10  # nb of queries
    np.random.seed(42)  # make reproducible
    xb = np.random.random((nb, d)).astype("float32")
    xb[:, 0] += np.arange(nb) / float(nb)
    xq = np.random.random((nq, d)).astype("float32")
    xq[:, 0] += np.arange(nq) / float(nb)

    xb = xb / np.linalg.norm(xb, axis=1, keepdims=True)
    xq = xq / np.linalg.norm(xq, axis=1, keepdims=True)

    my_index = Index()
    fb_index = faiss.IndexFlatL2(d)  # build the index

    fb_index.add(xb)  # add vectors to the fb_index
    my_index.add(xb)

    k = 4  # we want to see 4 nearest neighbors
    _, fb_san_i = fb_index.search(xb[:5], k)  # sanity check
    _, my_san_i = my_index.search(xb[:5], k)

    assert np.allclose(fb_san_i, my_san_i)

    _, fb_i = fb_index.search(xq, k)  # actual search
    _, my_i = my_index.search(xq, k)

    assert np.allclose(fb_i, my_i)
