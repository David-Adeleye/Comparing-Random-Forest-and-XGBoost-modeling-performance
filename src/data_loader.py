"""
A function to load the dataset
"""
from sklearn.datasets import fetch_california_housing

def load_dataset():
    """
    Function to load the dataset from sklearn
    The function returns an object housing the dataset and its attributes
    """
    
    return fetch_california_housing()
