

'''
Importing libraries
'''

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

def getTotalCountAndLabelFromValueFeatureByGroup(feature):
  count = data_copy[feature].value_counts()
  label = data_copy[feature].value_counts().index.tolist()
  return count, label
