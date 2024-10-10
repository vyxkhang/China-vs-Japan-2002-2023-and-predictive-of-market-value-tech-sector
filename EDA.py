import pandas as pd
import numpy as np

df = pd.read_csv("D:\Project\Data\Big_Japan_vs_China_Technology.csv")
print(df.head(10))

#Check NaN values

df.isnull().sum()


