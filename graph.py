
import networkx as nx
import matplotlib.pyplot as plt


def parse_graph(file_path):
    vertices = set()
    edges = []

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            if parts[0] == 'vertex':
                vertices.add(parts[1])
            elif parts[0] == 'edge':
                edges.append((parts[1], parts[2]))

    return vertices, edges


def draw_graph(vertices, edges):
    G = nx.DiGraph()
    G.add_nodes_from(vertices)
    G.add_edges_from(edges)

    plt.figure(figsize=(12, 8))
    # Increase k to spread out the nodes (thus making edges longer)
    pos = nx.spring_layout(G, seed=42, k=1.5)

    nx.draw_networkx_nodes(G, pos, node_size=1500, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

    plt.title("Graph Visualization")
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    # Replace 'graph.txt' with your input file path
    file_path = 'graph.txt'
    vertices, edges = parse_graph(file_path)
    draw_graph(vertices, edges)

