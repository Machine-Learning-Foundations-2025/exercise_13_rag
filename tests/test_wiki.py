"""Test hpc wiki download."""

import sys

sys.path.insert(0, "./src/")

from src.wiki_download import get_hpc_wiki_pages


def test_pages() -> None:
    """See it the function really returns true."""
    page_dict = get_hpc_wiki_pages()
    assert (
        page_dict["getting_started"] == "https://wiki.hpc.uni-bonn.de/getting_started"
    )
