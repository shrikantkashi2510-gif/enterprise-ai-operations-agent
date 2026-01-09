from typing import List


class VectorStore:
    """
    Interface for vector-based retrieval.

    Guarantees:
    - Encapsulation of embedding + similarity logic
    - Replaceable backend (pgvector, OpenSearch, etc.)
    """

    def similarity_search(self, query: str, k: int = 5) -> List[str]:
        """
        Perform a similarity search for the given query.

        Args:
            query: Natural language query
            k: Number of results to return

        Returns:
            List of retrieved text chunks
        """
        raise NotImplementedError
