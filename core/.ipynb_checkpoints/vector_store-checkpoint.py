# core/vector_store.py

from pathlib import Path
from typing import List

import faiss
import numpy as np
import pickle

from sentence_transformers import SentenceTransformer


class PolicyVectorStore:
    """
    AVCA Policy Knowledge Base

    Responsibilities:
    ------------------
    - Load enterprise policy files
    - Generate embeddings
    - Build FAISS index
    - Save / Load index
    - Semantic retrieval
    """

    def __init__(
        self,
        policy_dir: str = "data/raw_policies",
        index_dir: str = "data/faiss_index",
        embedding_model: str = "all-MiniLM-L6-v2"
    ):

        self.policy_dir = Path(policy_dir)
        self.index_dir = Path(index_dir)

        self.embedding_model = SentenceTransformer(
            embedding_model
        )

        self.index = None
        self.documents = []

    # ====================================================
    # Load Policy Files
    # ====================================================

    def load_documents(self):

        documents = []

        if not self.policy_dir.exists():

            raise FileNotFoundError(
                f"Policy directory not found: {self.policy_dir}"
            )

        for file_path in self.policy_dir.glob("*"):

            if file_path.suffix.lower() not in [
                ".txt",
                ".md"
            ]:
                continue

            content = file_path.read_text(
                encoding="utf-8"
            )

            chunks = self.chunk_text(
                content
            )

            documents.extend(chunks)

        self.documents = documents

        return documents

    # ====================================================
    # Chunking
    # ====================================================

    def chunk_text(
        self,
        text: str,
        chunk_size: int = 1000,
        overlap: int = 150
    ):

        chunks = []

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunks.append(
                text[start:end]
            )

            start += (
                chunk_size - overlap
            )

        return chunks

    # ====================================================
    # Build Index
    # ====================================================

    def build_index(self):

        docs = self.load_documents()

        if not docs:

            raise ValueError(
                "No policy documents found."
            )

        embeddings = self.embedding_model.encode(
            docs,
            convert_to_numpy=True,
            show_progress_bar=True
        )

        dimension = embeddings.shape[1]

        index = faiss.IndexFlatL2(
            dimension
        )

        index.add(
            embeddings.astype(
                np.float32
            )
        )

        self.index = index

        self.save_index()

        return len(docs)

    # ====================================================
    # Save Index
    # ====================================================

    def save_index(self):

        self.index_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        faiss.write_index(
            self.index,
            str(
                self.index_dir /
                "policy.index"
            )
        )

        with open(
            self.index_dir /
            "documents.pkl",
            "wb"
        ) as f:

            pickle.dump(
                self.documents,
                f
            )

    # ====================================================
    # Load Index
    # ====================================================

    def load_index(self):

        index_file = (
            self.index_dir /
            "policy.index"
        )

        doc_file = (
            self.index_dir /
            "documents.pkl"
        )

        if not index_file.exists():

            raise FileNotFoundError(
                "FAISS index not found."
            )

        self.index = faiss.read_index(
            str(index_file)
        )

        with open(
            doc_file,
            "rb"
        ) as f:

            self.documents = pickle.load(
                f
            )

    # ====================================================
    # Search
    # ====================================================

    def search(
        self,
        query: str,
        k: int = 5
    ) -> List[str]:

        if self.index is None:

            self.load_index()

        query_embedding = (
            self.embedding_model.encode(
                [query],
                convert_to_numpy=True
            )
        )

        distances, indices = (
            self.index.search(
                query_embedding.astype(
                    np.float32
                ),
                k
            )
        )

        results = []

        for idx in indices[0]:

            if (
                idx >= 0 and
                idx < len(self.documents)
            ):
                results.append(
                    self.documents[idx]
                )

        return results

    # ====================================================
    # Search With Scores
    # ====================================================

    def search_with_scores(
        self,
        query: str,
        k: int = 5
    ):

        if self.index is None:

            self.load_index()

        query_embedding = (
            self.embedding_model.encode(
                [query],
                convert_to_numpy=True
            )
        )

        distances, indices = (
            self.index.search(
                query_embedding.astype(
                    np.float32
                ),
                k
            )
        )

        results = []

        for score, idx in zip(
            distances[0],
            indices[0]
        ):

            if (
                idx >= 0 and
                idx < len(self.documents)
            ):

                results.append(
                    {
                        "score": float(score),
                        "content":
                            self.documents[idx]
                    }
                )

        return results


# ========================================================
# Local Testing
# ========================================================

if __name__ == "__main__":

    store = PolicyVectorStore()

    chunks = store.build_index()

    print(
        f"\n✅ Indexed {chunks} policy chunks"
    )

    print(
        "\n🔎 Searching...\n"
    )

    results = store.search(
        "SQL Injection prevention"
    )

    for i, item in enumerate(
        results,
        start=1
    ):

        print(
            f"\nResult {i}"
        )

        print(
            "-" * 50
        )

        print(
            item[:500]
        )