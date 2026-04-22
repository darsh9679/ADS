import matplotlib.pyplot as plt
import seaborn as sns

scores = [10, 15, 12, 18, 20, 25, 30, 16, 22, 14, 80]
idx    = range(len(scores))  # x-axis for scatter

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
ax = axes.flatten()         # treat as flat list of 6 axes

sns.histplot (scores,               color="skyblue",   ax=ax[0]).set_title("Histogram")
sns.boxplot  (x=scores,                        color="lightgreen", ax=ax[1]).set_title("Box Plot")
sns.kdeplot  (scores,                 color="salmon",     ax=ax[2]).set_title("Density")
sns.scatterplot(x=idx, y=scores,               color="orchid",     ax=ax[3]).set_title("Scatter")
sns.stripplot(x=scores,                         color="steelblue",  ax=ax[4]).set_title("Strip Plot")
sns.violinplot(x=scores,                        color="gold",       ax=ax[5]).set_title("Violin Plot")

plt.tight_layout()
plt.show()






# import matplotlib.pyplot as plt
# import seaborn as sns

# scores = [10, 15, 12, 18, 20, 25, 30, 16, 22, 14, 80, 90 , ]

# fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# sns.histplot(scores, kde=True,  color="skyblue",   ax=axes[0]).set_title("Histogram")
# sns.boxplot (x=scores,          color="lightgreen", ax=axes[1]).set_title("Box Plot")
# sns.kdeplot (scores, fill=True,   color="salmon",     ax=axes[2]).set_title("Density")

# plt.tight_layout()
# plt.show()
