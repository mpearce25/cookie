import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Read in CSV of BLEU scores and parse important columns
fn = "blue.csv"
cols = ["victim BLEU (before)", "victim BLEU (after)", "attacker BLEU (before)", "attacker BLEU (after)", "% watermarked", "p value"]
df = pd.read_csv(fn)[cols]
print(df)

# Plot data
vb, va = df[cols[0]], df[cols[1]]
ab, aa = df[cols[2]], df[cols[3]]
y = df[cols[4]]

plt.scatter(vb, y, s = 20, label="Victim BLEU Original")
plt.scatter(va, y, s  = 20, label="Victim BLEU Stylized")
plt.scatter(ab, y, s = 20, label="Attacker BLEU Original training")
plt.scatter(aa, y, s = 20, label = "Attacker BLEU Mixed (Stylized / Original) Training")
plt.legend(bbox_to_anchor=(.04, -.50), loc='center left')
plt.title("Victim / Attacker BLEU Scores")
plt.ylabel("% of Stylized Attacker Training Data ")
plt.xlabel("BLEU4 Score")
plt.tight_layout() #tight margins
plt.yticks(range(0, 25, 5))
plt.xticks(range(30, 36, 1))

# Calculate means
ps = [5, 10, 15]
# 5%


# 10%

# 15%

plt.show()


# Cluster with scikit. Try n clusters 1, 2, 3, 4
# Kmean = KMeans(n_clusters=2)
# Kmean.fit(X)
