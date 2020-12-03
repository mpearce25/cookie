import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import sys

# Read in CSV of BLEU scores and parse important columns
fn = sys.argv[1]
cols = ["victim BLEU (before)", "victim BLEU (after)", "attacker BLEU (before)", "attacker BLEU (after)", "% watermarked", "p value", "Model"]
df = pd.read_csv(fn)[cols]
print(df)

# Pyplot

fig, axs = plt.subplots(4, 1)
plt.title("Approach 1 Watermarking")
fig.tight_layout()


# Plotting BLEU vs P score for each model
models = ["twitter_cds", "poetry_cds", "lyrics", "formality_314"]
model_names = ["Twitter CDS", "Poetry CDS", "Lyrics CDS", "Formality 314"]
for i in range(4):
    # Twitter
    mdf = df[df['Model'] == models[i]]
    # print(twitter_cds)
    tvb, tva = mdf[cols[0]], mdf[cols[1]]
    tab, taa = mdf[cols[2]], mdf[cols[3]]
    y = mdf[cols[5]] #gets p value
    axs[i].scatter(tvb, y, s = 20, label="Victim BLEU Original")
    axs[i].scatter(tva, y, s  = 20, label="Victim BLEU Stylized")
    axs[i].scatter(tab, y, s = 20, label="Attacker BLEU Original training")
    axs[i].scatter(taa, y, s = 20, label = "Attacker BLEU Mixed (Stylized / Original) Training")
    # axs[i].legend(bbox_to_anchor=(.04, -.50), loc='center left')
    axs[i].title.set_text(model_names[i])
    axs[i].set(xlabel=("BLEU4 Score"), ylabel=("P value"), yticks=([x / 10 for x in range(-1, 5, 1)]), xticks=(range(30, 36, 1)))
handles, labels = axs[3].get_legend_handles_labels()



plt.legend(handles, labels, bbox_to_anchor=(0, 6.500), loc='upper left')
# plt.savefig("ap1_p_vs_bleu_per_model_auto.png")
# plt.show()
plt.clf()


# Plotting % replaced vs BLEU score for all
vb, va = df[cols[0]], df[cols[1]]
ab, aa = df[cols[2]], df[cols[3]]
y = df[cols[4]]
plt.scatter(vb, y, s = 20, label="Victim BLEU Original")
plt.scatter(va, y, s  = 20, label="Victim BLEU Stylized")
plt.scatter(ab, y, s = 20, label="Attacker BLEU Original training")
plt.scatter(aa, y, s = 20, label = "Attacker BLEU Mixed (Stylized / Original) Training")
plt.title("Victim / Attacker BLEU Scores")
plt.legend(bbox_to_anchor=(.0, 1.5), loc='upper left')
plt.xlabel("BLEU4 Score")
plt.ylabel("% Stylized")
plt.xticks(range(29, 36, 1))
plt.yticks(range(0, 25, 5))



plt.show()