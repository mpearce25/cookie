import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Read in CSV of BLEU scores and parse important columns
fn = "blue.csv"
cols = ["victim BLEU (before)", "victim BLEU (after)", "attacker BLEU (before)", "attacker BLEU (after)", "% watermarked", "p value"]
df = pd.read_csv(fn)[cols]
print(df)

# Pyplot
fig = plt.figure(figsize=(16, 16))
fig, axs = plt.subplots(2, 2)
a1, a2, a3, a4 = [*axs[0], *axs[1]]

# Plot data
vb, va = df[cols[0]], df[cols[1]]
ab, aa = df[cols[2]], df[cols[3]]
y = df[cols[4]]


a1.scatter(vb, y, s = 20, label="Victim BLEU Original")
a1.scatter(va, y, s  = 20, label="Victim BLEU Stylized")
a1.scatter(ab, y, s = 20, label="Attacker BLEU Original training")
a1.scatter(aa, y, s = 20, label = "Attacker BLEU Mixed (Stylized / Original) Training")
a1.legend(bbox_to_anchor=(.04, -.50), loc='center left')
a1.title("Victim / Attacker BLEU Scores")
a1.ylabel("% of Stylized Attacker Training Data ")
a1.xlabel("BLEU4 Score")
a1.tight_layout() #tight margins
a1.yticks(range(0, 25, 5))
a1.xticks(range(30, 36, 1))

# Calculate means
ps = [5, 10, 15]
# 5%


# 10%

# 15%

plt.show()


# Cluster with scikit. Try n clusters 1, 2, 3, 4
# Kmean = KMeans(n_clusters=2)
# Kmean.fit(X)
