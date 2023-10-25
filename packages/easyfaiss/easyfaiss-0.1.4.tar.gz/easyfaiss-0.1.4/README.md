# Easy Faiss

Easy Faiss is a package for creating vector indexes / knowledge base for LLM chatbots. This provides an easy-to-use alternative over using vector databases such as Pinecone or Weaviate.

Example script:

```python

import easyfaiss as ef

model, tokenizer = ef.bert_setup()

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

# create embeddings to store in index
embeddings = ef.create_embeddings(model=model, tokenizer=tokenizer, dataset=data)

# create a query vector to perform similarity search on the index
user_query = "What's the population in Tokyo, Japan?"
query_vector = ef.create_embeddings(model=model, tokenizer=tokenizer, dataset=[user_query])

# create the index
flat_index = ef.FlatIndex(name='demo')
flat_index.create_index(dimensions=768)
flat_index.update_index(embeddings=embeddings, dataset=data)

print(flat_index.details())

# perform similarity search
indices, distances = flat_index.similarity_search(query_vector=query_vector, k=3)

```

## EasyFaiss currently provides 2 types of faiss indexes

**FlatIndex:**

- **Speed:** This index is relatively slower for nearest neighbor search, especially as the number of vectors increases.
- **Scale:** Suitable for smaller datasets with low to moderate memory requirements.
- **Accuracy:** Provides exact nearest neighbor search, making it the most accurate option.

**HNSWFlatIndex:**

- **Speed:** Hierarchical Navigable Small World (HNSW) allows for fast approximate nearest neighbor search, especially on large datasets.
- **Scale:** Well-suited for large datasets, as it uses approximate nearest neighbor search, which makes it more memory-efficient.
- **Accuracy:** Provides approximate results that might have a small trade-off in accuracy compared to FlatIndex.

The choice between these two index types depends on your specific use case:

- Use FlatIndex when you have a relatively small dataset and need precise, exact nearest neighbor search.
- Use HNSWFlatIndex when you have a larger dataset, and you can tolerate a small reduction in accuracy in exchange for faster search and lower memory requirements.

For FlatIndex, an upper limit for the number of vectors depends on the available memory, but it's typically suitable for a few thousand vectors (e.g., up to 10,000 or more, depending on the dimension of the vectors and available RAM). Beyond that, you might start experiencing memory limitations. HNSWFlatIndex is a good choice for larger datasets, including millions of vectors, provided you can accept the trade-offs in accuracy.