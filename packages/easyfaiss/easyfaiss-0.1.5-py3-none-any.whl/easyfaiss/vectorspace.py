import faiss
import numpy as np
import json

class VectorSpace:
    def __init__(self, name='vector_space'):
        self.dimensions = None
        self.index = None
        self.name = name
        self.next_id = 0
        self.vector_ids = {}

    def create_index(self, dimensions=768):
        raise NotImplementedError("Child classes must implement this method.")

    def update_index(self, embeddings, dataset):
        num_embeddings = len(embeddings)
        ids = np.arange(self.next_id, self.next_id + num_embeddings, dtype=np.int64)
        self.next_id += num_embeddings
        if self.index is not None:
            embeddings_array = np.concatenate(embeddings, axis=0)
            self.index.add_with_ids(embeddings_array, ids)
            for i, text in enumerate(dataset):
                self.vector_ids[int(ids[i])] = text
            vector_mappings = json.dumps(self.vector_ids, indent=4)
            return vector_mappings
        else:
            return "Index not created yet."

    def details(self):
        if self.index is not None:
            index_name = self.name
            num_vectors = self.index.ntotal
            vector_dimensions = self.dimensions
            return {
                "Name": index_name,
                "Number of Vectors": num_vectors,
                "Dimensions": vector_dimensions
            }
        else:
            return "Index not created yet."

    def save_index(self):
        if self.index is not None:
            index_file = f"{self.name}.index"
            faiss.write_index(self.index, index_file)
            return f"Index saved as {index_file}"
        else:
            return "Index not created yet."
        
    def similarity_search(self, query_vector, k=5):
        if self.index is not None:
            query_vector = np.array(query_vector, dtype=np.float32)
            query_vector = query_vector.reshape(1, self.dimensions)

            distances, indices = self.index.search(query_vector, k)

            print(f"Nearest Neighbors (Indices):\n{indices}")
            print(f"Distances:\n{distances}")

            return indices, distances
        else:
            return "Index not created yet."


class FlatIndex(VectorSpace):
    def __init__(self, name='vector_space'):
        super().__init__(name)

    def create_index(self, dimensions=768):
        self.dimensions = dimensions
        self.index = faiss.IndexIDMap(faiss.IndexFlatL2(dimensions))

class HNSWFlatIndex(VectorSpace):
    def __init__(self, name='vector_space'):
        super().__init__(name)

    def create_index(self, dimensions=768):
        self.dimensions = dimensions
        self.index = faiss.IndexIDMap(faiss.IndexHNSWFlat(dimensions, 32))