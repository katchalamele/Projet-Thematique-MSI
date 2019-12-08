import networkx as nx
import matplotlib.pyplot as plt
import os

options = {
    'node_size': 200,
    'width': 1,
    'with_labels': True
    }

directory = [ 'circular', 'kamada_kawai', 'planer', 'random',
              'spectral', 'spring', 'shell' ]

def save_graph(name, node_range, couples):
    G = nx.Graph()
    l = []
    for i in range(1, node_range+1):
        l.append(i)
        
    G.add_nodes_from(l)
    G.add_edges_from(couples)
    
    if not os.path.exists("graphs"):
        os.makedirs("graphs")
    for e in directory:
        if not os.path.exists("./graphs/" + e):
            os.makedirs("./graphs/" + e)

    nx.draw_circular(G, **options)
    plt.savefig("./graphs/circular/" + name + ".png")
    plt.clf()
    
    nx.draw_kamada_kawai(G, **options)
    plt.savefig("./graphs/kamada_kawai/" + name + ".png")
    plt.clf()

    try:    
        nx.draw_planar(G, **options)
        plt.savefig("./graphs/planer/" + name + ".png")
        plt.clf()
    except:
        nx.draw_spring(G, **options, k=0.15,iterations=20)
        plt.savefig("./graphs/planer/" + name + ".png")
        plt.clf()
        print(name + " is not planar, spring draw")
    
    nx.draw_random(G, **options)
    plt.savefig("./graphs/random/" + name + ".png")
    plt.clf()

    nx.draw_spectral(G, **options)
    plt.savefig("./graphs/spectral/" + name + ".png")
    plt.clf()
    
    nx.draw_spring(G, **options, k=0.15,iterations=20)
    plt.savefig("./graphs/spring/" + name + ".png")
    plt.clf()

    nx.draw_shell(G, **options,
                  nlist=[
                      range(node_range//2+1, node_range+1),
                      range(1, node_range//2+1)
                      ])
    plt.savefig("./graphs/shell/" + name + ".png")
    plt.clf()
    
