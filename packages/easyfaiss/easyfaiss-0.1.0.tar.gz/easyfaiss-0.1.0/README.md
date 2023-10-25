# Vector Vault

Vector Vault is a small package that allows you to create vector index that can be used as a knowledge base for LLM chatbots.

Example script:

```python

from vectorvault.vectorembeddings import bert_setup, create_embeddings
from vectorvault.vectorspace import FlatIndex, HNSWFlatIndex
import time

# Set up BERT model and tokenizer
model, tokenizer = bert_setup()

# Sample data
data = [
    "Hello, how are you?",
    "What's the weather today?",
    "How does photosynthesis work?",
    "What's the capital of France?",
    "Tell me about the history of the Roman Empire.",
    "How can I improve my coding skills?",
    "What's the recipe for a classic margarita?",
    "Explain the theory of relativity.",
    "What's the population of Tokyo?",
    "How can I learn a new language quickly"
]

# Create embeddings for the sample data
embeddings = create_embeddings(model=model, tokenizer=tokenizer, dataset=data)

# Define a user query
user_query = "What's the population in Tokyo, Japan?"

# Create embeddings for the user query
query_vector = create_embeddings(model=model, tokenizer=tokenizer, dataset=[user_query])

# Create a FlatIndex and update it with embeddings
flat_index = FlatIndex(name='flat_index')
flat_index.create_index(dimensions=768)
flat_index.update_index(embeddings=embeddings, dataset=data)

# Print details of the index
print("FlatIndex Details:")
print(flat_index.details())

# Perform similarity search on FlatIndex
print("\nFlatIndex Similarity Search:")
start_time = time.time()
indices, distances = flat_index.similarity_search(query_vector=query_vector, k=3)
end_time = time.time()
print("Time taken for kNN search in FlatIndex: {:.4f} seconds".format(end_time - start_time))

# Create an HNSWFlatIndex and update it with embeddings
hnsw_index = HNSWFlatIndex(name='hnsw_index')
hnsw_index.create_index(dimensions=768)
hnsw_index.update_index(embeddings=embeddings, dataset=data)

# Print details of the HNSWFlatIndex
print("\nHNSWFlatIndex Details:")
print(hnsw_index.details())

# Perform similarity search on HNSWFlatIndex
print("\nHNSWFlatIndex Similarity Search (Approximate Nearest Neighbors - ANN):")
start_time = time.time()
indices, distances = hnsw_index.similarity_search(query_vector=query_vector, k=3)
end_time = time.time()
print("Time taken for ANN search in HNSWFlatIndex: {:.4f} seconds".format(end_time - start_time))

```

## Vector vault currently provides 2 types of faiss indexes

**faiss.IndexFlatL2:**

- **Speed:** This index is relatively slower for nearest neighbor search, especially as the number of vectors increases.
- **Scale:** Suitable for smaller datasets with low to moderate memory requirements.
- **Accuracy:** Provides exact nearest neighbor search, making it the most accurate option.

**faiss.IndexHNSWFlat:**

- **Speed:** Hierarchical Navigable Small World (HNSW) allows for fast approximate nearest neighbor search, especially on large datasets.
- **Scale:** Well-suited for large datasets, as it uses approximate nearest neighbor search, which makes it more memory-efficient.
- **Accuracy:** Provides approximate results that might have a small trade-off in accuracy compared to faiss.IndexFlatL2.

The choice between these two index types depends on your specific use case:

- Use faiss.IndexFlatL2 when you have a relatively small dataset and need precise, exact nearest neighbor search.
- Use faiss.IndexHNSWFlat when you have a larger dataset, and you can tolerate a small reduction in accuracy in exchange for faster search and lower memory requirements.

For faiss.IndexFlatL2, an upper limit for the number of vectors depends on the available memory, but it's typically suitable for a few thousand vectors (e.g., up to 10,000 or more, depending on the dimension of the vectors and available RAM). Beyond that, you might start experiencing memory limitations. faiss.IndexHNSWFlat is a good choice for larger datasets, including millions of vectors, provided you can accept the trade-offs in accuracy.
