"""Download the Ubos HPC wiki."""

import ssl
import urllib.request

from bs4 import BeautifulSoup


def get_hpc_wiki_pages() -> list[str]:
    """Get the hpc wikie page links."""
    hpc_wiki_link = "http://wiki.hpc.uni-bonn.de/"
    context = ssl.SSLContext()
    soup = BeautifulSoup(
        urllib.request.urlopen(hpc_wiki_link, context=context), "html.parser"
    )
    internals = list(
        filter(lambda link: "is-internal" in str(link), soup.find_all("a"))
    )
    link_suffix_list = [
        str(s).split("href=")[1].split(">")[0].replace('"', "") for s in internals
    ]
    link_dict = {
        suffix.replace("/", ""): "https://wiki.hpc.uni-bonn.de" + suffix
        for suffix in link_suffix_list
    }
    return link_dict


def download_page(page_link) -> str:
    """Download the wiki page at `page_link`."""
    context = ssl.SSLContext()
    soup = BeautifulSoup(
        urllib.request.urlopen(page_link, context=context), "html.parser"
    )
    # Extracting data for article section
    content = list(filter(lambda div: "content" in str(div), soup.find("div")))[0]
    # Calculating result
    res = " ".join(content.find_all(text=True))
    return res


if __name__ == "__main__":

    page_links = get_hpc_wiki_pages()
    page_links["home"] = "https://wiki.hpc.uni-bonn.de/"

    # TODO: Loop through the page_links dictionary and download every page.
    # Use the page_links items function to get keys and values.
    # download_page accepts page links and lets you download a page.
    page_contents = {} # TODO: fill this dictionary with page downloads.

    # write to file
    with open("./data_dir/hpc_wiki.csv", "w") as wiki_file:
        for key in page_contents.keys():
            wiki_file.write(
                f"{key} \t {page_contents[key].replace("\t", " ").replace("\n", "")}"
            )
            wiki_file.write("\n")
