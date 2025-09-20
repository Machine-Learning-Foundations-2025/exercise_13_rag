# Retrieval augmented generation (RAG) exercise

1. Create a new environment and install the requirements via `pip install requirements.txt`. 


2. Navigate to source and resolve the `TODO`s in the `wiki_download.py` as well as the `index.py` files.

    - To set up the index evaluate $d(z)^T q(x)$. When document and question embeddings are gatherd in matrices, the computations can be expressed as a matrix product, which will lead to a number of entries by number of queries matrix.  
    - When does the dot product turn into cosine distance?


2. Download a copy of `https://wiki.hpc.uni-bonn.de/` by running 
    ```bash
    python src/wiki_download.py
    ```

3. Test you index by running 
    ``` bash
    nox -s test
    ```
    - run a full RAG with your index via
    ``` bash
    python src/query_rag.py --csv_path data_dir/hpc_wiki.csv --question 'Can we run Anaconda on Marvin?'
    ```
    - Result:
    ```bash
    INFO:__main__:Step 4 - Processing Question
    INFO:__main__:Q: Can we run Anaconda on Marvin?
    INFO:__main__:A:  not allowed
    ```

    - what do you observe if you replace the hpc-wiki crawl with random unrelated information? Run
    ``` bash
    python src/query_rag.py --csv_path data_dir/random_info.csv --question 'Can we run Anaconda on Marvin?'
    ```

    - Result:
    ``` bash
    INFO:__main__:Step 4 - Processing Question
    INFO:__main__:Q: Can we run Anaconda on Marvin?
    INFO:__main__:A:  how far can we run
    ```


### See also 
- the original RAG paper
    - https://arxiv.org/pdf/2005.11401
- example code at 
    - https://github.com/huggingface/transformers-research-projects/tree/main/rag


