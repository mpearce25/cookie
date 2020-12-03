import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

fn = "approach1.csv"
cols = []
# cols = ["Model", "p value", "learning rate", "dropout" ,"attention dropout","epcohs", "% Classified as Stylized"]
df = pd.read_csv(fn)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
print(df)
# df = df.drop("Unnamed: 7")
# Filter if desired
if len(cols) > 1:
    df = df[cols]

print(df.to_latex(index=False))
