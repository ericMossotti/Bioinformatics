# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 15:51:16 2023

@author: ecmos
"""

from Py.de_bruijn_ize import de_bruijn_ize


def visualize_de_bruijn ( st, k ) :
    
    """ Visualize a directed multigraph using graphviz """
    
    nodes, edges = de_bruijn_ize ( st, k )
    
    dot_str = 'digraph "DeBruijn graph" {\n'
    
    for node in nodes :
        
        dot_str += '  %s [label="%s"] ;\n' % ( node, node )
        
    for src, dst in edges :
        
        dot_str += '  %s -> %s ;\n' % ( src, dst )
        
    return dot_str + '}\n'


"""

# might have to do this first:
# %install_ext https://raw.github.com/cjdrake/ipython-magic/master/gvmagic.py
%load_ext gvmagic

"""

"""
%dotstr visualize_de_bruijn("ACGCGTCG", 3)


"""