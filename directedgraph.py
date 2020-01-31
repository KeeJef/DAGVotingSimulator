import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

#style.use('fivethirtyeight')

G = nx.MultiDiGraph()
fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)


def animate(i):

    fig.clf()
    relationshiplist = open('data.txt','r').read() #import json here
    relationshiplist = eval(relationshiplist)

    G.clear()
    G.add_edges_from(relationshiplist)

    
    pos = nx.spectral_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size = 500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color='b', arrows=True, connectionstyle='arc3, rad = 0.1')

    
    

ani = animation.FuncAnimation(fig, animate, interval=5000)
plt.show()