import networkx as nx
import matplotlib.pyplot as plt
import graphviz
import matplotlib.animation as animation
import json
from matplotlib import style

style.use('fivethirtyeight')

G = nx.MultiDiGraph()
fig = plt.figure()

def animate(i):

    fig.clf()
    with open('listfile.txt') as json_file:
        relationshiplist = json.load(json_file)
        
    
    counter = 0 
    while len(relationshiplist) != counter:

        relationshiplist[counter].reverse()
        relationshiplist[counter] = tuple(relationshiplist[counter])
        
        counter+=1 
        pass

    

    G.clear()
    G.add_edges_from(relationshiplist)
 
    #pos = nx.spring_layout(G)
    pos = nx.nx_agraph.graphviz_layout(G, prog='dot' ,args="-Grankdir=RL")
    
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size = 500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color='b', arrows=True,) #connectionstyle='arc3, rad = 0.1')

    
ani = animation.FuncAnimation(fig, animate, interval=2000)
plt.show()