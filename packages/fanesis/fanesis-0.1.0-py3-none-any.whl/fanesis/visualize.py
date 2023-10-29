import os
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

class Visualize:
    def __init__(
        self,
        output_path: str,
    ) -> None:
        self.output_path = output_path
        
    def visualize(
            self, 
            df: pd.DataFrame,
        ) -> None:
            G = nx.from_pandas_edgelist(df, 'person1',
                                'person2', edge_attr="value", create_using=nx.Graph())
            plt.figure(figsize=(10, 10))
            pos = nx.kamada_kawai_layout(G)
            node_degree = dict(G.degree())

            nx.draw(G, with_labels=True, node_color='skyblue',
                    edge_cmap=plt.cm.Blues, pos=pos,
                    node_size=[v * 100 for v in node_degree.values()]
                    )
            viz_path = os.path.join(self.output_path, "graph.png")
            plt.savefig(viz_path)