import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import ggplot

df = pd.read_csv('movie.csv',sep=",",encoding="ISO-8859-1")

df.head()
plt.figure(figsize=(12,8))
plt.bar(df["movie"],df["rating"])


#ciao