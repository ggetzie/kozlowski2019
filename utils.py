import numpy as np

import word_pairs as wp

def get_vectors(model, words):
    """
    Return a list of pairs of word vectors corresponding to a list
    of antonym pairs
    """
    result = []
    for pair in words:
        try:
            result.append((model[pair[0]], model[pair[1]]))
        except KeyError:
            # skip words that do not appear in corpus
            continue
    return result

def get_dimension(model, words):
    """
    Calculate the cultural dimension of a list of antonym pairs
    Per Kozlowski 2019 this is the mean of the differences
    of the word pairs
    """
    # Calculate the cultural dimension of a list of antonym pairs
    
    vectors = get_vectors(model, words)
    return sum([v[0]-v[1] for v in vectors]) / len(vectors)

def vector_projection(vector, dimension):
    """
    Calculate the vector projection of vector along the specified dimension
    """

    return (dimension / np.linalg.norm(dimension)) * np.dot(vector, dimension)


def scalar_projection(vector, dimension):
    """
    Calculate the scalar projection of vector along the specified dimension
    """

    return np.dot(vector, dimension) / np.linalg.norm(dimension)
