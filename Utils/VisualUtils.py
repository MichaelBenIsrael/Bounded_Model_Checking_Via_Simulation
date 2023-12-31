# import the modules
import os
import networkx as nx
import matplotlib.pyplot as plt
from KripkeStructureFramework.KripkeStructure import KripkeStructure
from KripkeStructureFramework.Node import Node
import Utils.SystemUtils as Utils
import graphviz


def create_test_structures():
    # m1 :
    s0 = Node(0, isInitial=True)
    s1 = Node(1)
    s2 = Node(2)
    s3 = Node(3, assignment='p')
    s4 = Node(4)
    s0.add_relation(1)
    s0.add_relation(2)
    s1.add_relation(3)
    s2.add_relation(4)
    s3.add_relation(3)
    s4.add_relation(4)
    m1 = KripkeStructure([s0, s1, s2, s3, s4])
    # m2:
    t0 = Node(0, isInitial=True)
    t1 = Node(1)
    t2 = Node(2, assignment='p')
    t3 = Node(3)
    t0.add_relation(1)
    t1.add_relation(2)
    t1.add_relation(3)
    t2.add_relation(2)
    t3.add_relation(3)
    m2 = KripkeStructure([t0, t1, t2, t3])
    return m1, m2


@staticmethod
def preview_system_new_window(system):
    colors_lst = Utils.SystemUtils.get_node_color_list(system)
    sys1_relations = Utils.SystemUtils.get_relations_list(system)
    node_names = Utils.SystemUtils.get_node_names_dictionary(system)
    # Create the graph
    G = nx.MultiDiGraph()
    # Makes sure nodes are on the appropriate indexes
    for i in range(len(system.get_nodes())):
        G.add_node(i)
    G.add_edges_from(sys1_relations)
    # Visualize
    nx.draw(G, with_labels=True, labels=node_names, node_size=800, node_color=colors_lst, pos=nx.kamada_kawai_layout(G))
    plt.show()

@staticmethod
def preview_system(system):
    colors_lst = Utils.SystemUtils.get_node_color_list(system)
    sys1_relations = Utils.SystemUtils.get_relations_list(system)
    node_names = Utils.SystemUtils.get_node_names_dictionary(system)
    # Create the graph
    G = nx.MultiDiGraph()
    nodes_size = len(system.get_nodes())
    # Makes sure nodes are on the appropriate indexes
    for i in range(nodes_size):
        G.add_node(i)
    # add relations to the nodes
    G.add_edges_from(sys1_relations)
    # Visualize
    nx.draw(G, with_labels=True, labels=node_names, node_size=800, node_color=colors_lst, pos=nx.kamada_kawai_layout(G))
    return G, node_names, colors_lst, plt

@staticmethod
def store_test_systems():
    s1, s2 = create_test_structures()
    Utils.SystemUtils.save_system(s1, 'c:\BMC_Systems\s1.json')
    Utils.SystemUtils.save_system(s2, 'c:\BMC_Systems\s2.json')
