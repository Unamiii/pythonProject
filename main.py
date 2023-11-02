import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np
import seaborn as sns

df = pd.read_csv('Assignment_1.csv')
df.head(1)
df['Age'].plot(kind='hist', bins=15)





plt.show()