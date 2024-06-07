# -*- coding: utf-8 -*-
"""DiabetesCorrelation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wTZpNgZsf2GbfddusRyiPT1DX72ZS015
"""

import pandas as pd
import matplotlib.pyplot as plt

from google.colab import files

uploaded = files.upload()

data = pd.read_csv('diabetes.csv')

data.head()

glucose_insulin_df = data[["Glucose","Insulin"]]
glucose_insulin_df = glucose_insulin_df.dropna()
correlation = glucose_insulin_df["Glucose"].corr(glucose_insulin_df["Insulin"])
print("Correlation between glucose and insulin:", correlation)
plt.figure(figsize=(8,6))
plt.scatter(glucose_insulin_df["Glucose"],glucose_insulin_df["Insulin"], alpha=0.5)
plt.title("Glucose vs Insulin")
plt.xlabel("Glucose")
plt.ylabel("Insulin")
plt.grid(True)
plt.show()