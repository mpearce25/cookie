import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Read in CSV of BLEU scores and parse important columns
fn = "blue.csv"
cols = ["victim BLEU (before)", "victim BLEU (after)", "attacker BLEU (before)", "attacker BLEU (after)"]
df = pd.read_csv(fn)[cols]
print(df.head())

# Plot
vb, va = df[cols[0]], df[cols[1]]
ab, aa = df[cols[2]], df[cols[3]]
vy = [0] * len(vb)
ay = [1] * len(ab)

plt.scatter(vb, vy, s = 20, label="Victim BLEU Original")
plt.scatter(va, vy, s  = 20, label="Victim BLEU After Stylized")
plt.scatter(ab, ay, s = 20, label="Attacker BLEU Original")
plt.scatter(aa, ay, s = 20, label = "Attacker BLEU 5%")
plt.legend()
plt.show()


# Cluster with scikit. Try n clusters 1, 2, 3, 4
# Kmean = KMeans(n_clusters=2)
# Kmean.fit(X)
