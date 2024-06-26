# -*- coding: utf-8 -*-
"""p1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KxmyCkiTj5mezo8Jf0lCCgYvU9GUT5rq
"""

import pandas as pd

data = {
    "Cholesterol": [190, 250, 220, 260, 210, 180, 240, 230, 270, 200],
    "BloodPressure": [120, 150, 130, 160, 125, 110, 145, 135, 170, 115]
}

df = pd.DataFrame(data)

def check(Cholesterol, Blood_Pressure):
  if Cholesterol > 240 or Blood_Pressure > 140:
    return "Risky"
  else:
    return "Normal"

df["HealthCondition"] = df.apply(lambda row: check(row['Cholesterol'], row['BloodPressure']), axis=1)
print(df)