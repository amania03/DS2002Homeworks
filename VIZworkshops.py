# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'heart_failure_clinical_records_dataset.csv'
data = pd.read_csv(file_path)

# Preview the dataset
print(data.head())

# Setting the style for seaborn
sns.set(style="whitegrid")

# 1. Distribution of age with respect to death events
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x="age", hue="DEATH_EVENT", kde=True, palette="husl", bins=20)
plt.title("Age Distribution by Death Event")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.legend(["Survived", "Death"])
plt.show()

# 2. Correlation heatmap
plt.figure(figsize=(12, 8))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# 3. Relationship between ejection fraction and death events
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x="DEATH_EVENT", y="ejection_fraction", palette="Set2")
plt.title("Ejection Fraction vs Death Event")
plt.xlabel("Death Event")
plt.ylabel("Ejection Fraction")
plt.xticks([0, 1], ['Survived', 'Death'])
plt.show()

# 4. Platelet levels and age
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x="age", y="platelets", hue="DEATH_EVENT", palette="viridis")
plt.title("Platelet Levels vs Age")
plt.xlabel("Age")
plt.ylabel("Platelets")
plt.legend(["Survived", "Death"], title="Death Event")
plt.show()


#I used a data set provided to me from my machine learning class I take at UVA. I have uploaded the data set onto my repo
#I also used stack overflow and chat to help me clean my code up and make my visualization appear cleaner 