"""
    Reference: https://python.plainenglish.io/create-a-network-graph-in-python-8829e0ec6741
"""

import random
import networkx as nx
import plotly.graph_objects as go

node_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
             "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

G = nx.Graph()


def draw_graph(length):
    from_index = random.randint(0, length)
    to_index = random.randint(0, length)

    return from_index, to_index


def create_numbers():
    from_list, to_list, counter = [], [], 30
    i = 0
    while i < counter:
        from_index, to_index = draw_graph(len(node_list) - 1)
        if from_index == to_index:
            continue
        from_list.append(node_list[from_index])
        to_list.append(node_list[to_index])
        i += 1
    print(from_list, '\n', to_list)

    return from_list, to_list


def draw():
    from_list, to_list = create_numbers()

    for i in range(len(node_list)):
        G.add_node(node_list[i])
        G.add_edges_from([(from_list[i], to_list[i])])

    pos = nx.spring_layout(G, k=0.5, iterations=100)
    for n, p in pos.items():
        G.nodes[n]['pos'] = p

    edge_trace = go.Scatter(
        x=[],
        y=[],
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        edge_trace['x'] += tuple([x0, x1, None])
        edge_trace['y'] += tuple([y0, y1, None])

    node_trace = go.Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers+text',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='pinkyl',
            reversescale=True,
            color=[],
            size=37,
            colorbar=dict(
                thickness=1,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line=dict(width=0)))
    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        node_trace['x'] += tuple([x])
        node_trace['y'] += tuple([y])
    for node, adjacencies in enumerate(G.adjacency()):
        node_trace['marker']['color'] += tuple([len(adjacencies[1])])
        node_info = adjacencies[0]
        node_trace['text'] += tuple([node_info])

    title = "Network Graph Demonstration"
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title=title,
                        titlefont=dict(size=16),
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=21, l=5, r=5, t=40),
                        annotations=[dict(
                            text="Text Here",
                            showarrow=False,
                            xref="paper", yref="paper")],
                        xaxis=dict(showgrid=False, zeroline=False,
                                   showticklabels=False, mirror=True),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, mirror=True)))
    fig.show()


if __name__ == '__main__':

    # create_numbers()
    draw()