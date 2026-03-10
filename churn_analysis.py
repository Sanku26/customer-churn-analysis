import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Dataset Loaded Successfully")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nDataset Shape:")
print(data.shape)

print("\nMissing Values:")
print(data.isnull().sum())

print("\nChurn Distribution:")
print(data['Churn'].value_counts())

sns.countplot(x='Churn', data=data)
plt.title("Customer Churn Distribution")
plt.show()

sns.countplot(x='Contract', hue='Churn', data=data)
plt.title("Churn by Contract Type")
plt.show()

sns.boxplot(x='Churn', y='MonthlyCharges', data=data)
plt.title("Monthly Charges vs Churn")
plt.show()