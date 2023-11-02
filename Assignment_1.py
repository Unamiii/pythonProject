import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis
from scipy.stats import shapiro
# Question 1
df = pd.read_csv('Assignment_1.csv')
# Assuming 0 for male and 1 for female
df['Gender_label'] = df['Gender'].replace({'Male': 0, 'Female': 1})
print(df)
# Generate a histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=20, kde=True)
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Generate a box-and-whisker plot
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['Age'])
plt.title('Box-and-Whisker Plot of Age')
plt.xlabel('Age')
plt.show()

# Calculate skewness and kurtosis
skewness = skew(df['Age'])
kurt = kurtosis(df['Age'])

print(f'Skewness: {skewness}')
print(f'Kurtosis: {kurt}')

# Question 2
# The Distribution carries more of a left skewness which may suggest outliers on the histogram.
# Also on the box-plot it seems to have more of an outlier on the left side . The skewness number and Kurtosis support
# this claim

# Question 3 (Shapiro test)

stat, p_value = shapiro(df['Age'])

print(f'Statistic: {stat}, p-value: {p_value}')

alpha = 0.5

if p_value > alpha:
    print('Fail to reject the null hypothesis. The data follows a normal distribution')
else:
    print('Reject the null hypothesis. The data does not follow a normal distribution')

