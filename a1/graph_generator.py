from networkx.generators import directed
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

df = pd.read_csv(input("CSV File: "))
print(df)
G = nx.from_pandas_edgelist(df, source='Source', target='Target', edge_attr='weight', create_using=nx.DiGraph)

nx.draw_networkx(G, arrows=True)
plt.savefig("filename.png")