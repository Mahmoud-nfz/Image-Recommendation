import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def find_closest_lines(embeddings_matrix, line_embedding, top_n=5):
    # Compute cosine similarity between the line embedding and all other embeddings
    similarity_scores = cosine_similarity(embeddings_matrix, line_embedding.reshape(1, -1))

    # Sort the similarity scores and get the indices of the top N closest lines
    top_indices = np.argsort(similarity_scores.flatten())[::-1][:top_n]

    return top_indices
