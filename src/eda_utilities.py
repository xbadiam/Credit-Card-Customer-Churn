

# Importing libraries

# Data manipulation and visualization.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Debugging.
from src.exception import CustomException
import sys

# Warnings.
from warnings import filterwarnings
filterwarnings('ignore')


def getTotalCountAndLabelFromValueFeatureByGroup(data, feature):
    """
    Devuelve el recuento y las etiquetas únicas de una característica dada.
    Args:
        data (pd.DataFrame): Dataset donde buscar los valores.
        feature (str): Nombre de la columna a analizar.
    Returns:
        tuple: (count, label)
    """
    count = data[feature].value_counts()
    label = data[feature].value_counts().index.tolist()
    return count, label
