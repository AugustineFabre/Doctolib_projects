import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set(style="whitegrid")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))

# Load the example car crash dataset
#crashes = sns.load_dataset("point1").sort_values("total", ascending=False)
# Load the data
crashes = pd.read_csv("/Users/apple/PycharmProjects/Doctolib/MVP4/point1.csv")

# Plot the total crashes
sns.set_color_codes("pastel")
sns.barplot(x="total", y="critère", data=crashes, label="100", color="b")

# Plot the crashes where alcohol was involved
sns.set_color_codes("muted")
sns.barplot(x="valeur", y="critère", data=crashes, label="note", color="b")

# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 100), ylabel="", xlabel="note du candidat")
sns.despine(left=True, bottom=True)

plt.show()