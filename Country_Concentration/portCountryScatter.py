import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("Port_Data.csv")


countryCounts = data["Country"].value_counts().reset_index()
countryCounts.columns = ["Country", "Number of Seaports"]


plt.figure(figsize=(24, 10))
sns.scatterplot(x="Country", y="Number of Seaports", size="Number of Seaports",
                data=countryCounts, 
                sizes=(100, 1000), 
                alpha=0.7, 
                palette="muted",
                hue = "Number of Seaports",
                )

plt.xticks(rotation=82)
plt.xlabel("Country")
plt.ylabel("Number of Seaports")
plt.title("Number of Seaports by Country")
plt.tight_layout()
plt.show()
