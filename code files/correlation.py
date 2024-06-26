# -*- coding: utf-8 -*-
"""Correlation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p_uTHFoyHPspud68OTXj27dOpp88faCr
"""

import pandas as pd
from google.colab import files
import matplotlib.pyplot as plt

uploaded = files.upload()

data = pd.read_csv('heart.csv')

data.head()

correlation_df = data[["Cholesterol","RestingBP"]]
correlation = correlation_df["Cholesterol"].corr(correlation_df["RestingBP"])
print(f"correlation Between Cholesterol and Blood Pressure: {correlation}")
plt.figure(figsize=(8,6))
plt.scatter(correlation_df["Cholesterol"],correlation_df["RestingBP"], color="red", alpha=0.5)
plt.title("Correlation Between Cholesterol and Blood Pressure")
plt.xlabel("Cholesterol")
plt.ylabel("Blood Pressure")
plt.grid(True)
plt.show