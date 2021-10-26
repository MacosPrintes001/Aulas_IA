#abrir arquivo cvs python
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("Datasets\covid19.csv")
print(data.head())
plt.figure(figsize=(7, 5))
x = range(len(data[]))