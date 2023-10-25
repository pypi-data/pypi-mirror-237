import os
import sys
import numpy as np
import torch
from transformers import BertModel, BertTokenizer

def bert_setup():
    model_name = "bert-base-uncased"
    model_dir = "./" + model_name
    
    if os.path.exists(model_dir):
        config_file_path = os.path.join(model_dir, "config.json")
        
        if os.path.exists(config_file_path) and os.path.getsize(config_file_path) > 0:
            model = BertModel.from_pretrained(model_dir)
            tokenizer = BertTokenizer.from_pretrained(model_dir)
            print(f"'{model_name}' model found in the current directory. Pipelines have been set up.")
        else:
            print(f"'{model_name}' directory is empty or missing critical files. Please delete the folder and rerun the script to set up BERT correctly.")
            sys.exit(1)
    else:
        model = BertModel.from_pretrained(model_name)
        tokenizer = BertTokenizer.from_pretrained(model_name)
        model.save_pretrained(model_dir)
        tokenizer.save_pretrained(model_dir)
        print(f"'{model_name}' downloaded to the current directory. Pipelines have been set up.")

    return model, tokenizer


def create_embeddings(model, tokenizer, dataset:list):
    if not isinstance(dataset, list) or not all(isinstance(text, str) for text in dataset):
        raise ValueError("The 'dataset' should be a list of strings, e.g., ['text 1', 'text 2']")

    uncased_texts = [text.lower() for text in dataset]
    embeddings = []

    inputs = tokenizer(uncased_texts[0], return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        output = model(**inputs)
    cls_embedding = output.last_hidden_state[:, 0, :].numpy()
    embedding_dimensions = cls_embedding.shape

    for text in uncased_texts:
        inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
        
        with torch.no_grad():
            output = model(**inputs)

        cls_embedding = output.last_hidden_state[:, 0, :].numpy()

        l2_norm = np.linalg.norm(cls_embedding, 2)
        normalized_vector = cls_embedding / l2_norm
        normalized_vector = normalized_vector.reshape((1, 768))

        embeddings.append(normalized_vector)

    num_embeddings = len(embeddings)
    print(f"Embedding Dimensions: {embedding_dimensions}")
    print(f"Number of embeddings generated: {num_embeddings}")
    return embeddings
