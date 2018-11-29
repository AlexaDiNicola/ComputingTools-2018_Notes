#!/usr/bin/env python

class Edge:
    """Edge class, to contain a directed edge of a tree or directed graph.
    attributes parent and child: index of parent and child node in the graph.
    """
	
	# Here's the function to create a new object & reserve memory for it.
	# __init__ is always that function: it's effectively the one called when
	# you create a new object of this class. Note also that self is a
	# reserved variable name.
    def __init__ (self, parent, child, length=None):
        """create a new Edge object, linking nodes
        with indices parent and child."""
        print("starting __init__ for new Edge object/instance")
        self.parent = parent   # So edges have an attribute called "parent",
        self.child = child     # one called "child",
        self.length = length   # and one called "length". Note that its default value is None, for a tree without branch lengths.

	# This one defines what happens when you print an object of this class --
	# i.e. convert it into a string -- for human readability.
    def __str__(self):
        res = "edge from " + str(self.parent) + " to " + str(self.child)
        return res

class Tree:
    """A Tree is described by its list of edges."""
    def __init__(self, edgelist):
        """create a new Tree object from a list of existing Edges"""
        self.edge = edgelist

    def __str__(self):
        res = "parent -> child:"
        for e in self.edge:
            res += "\n" + str(e.parent) + " " + str(e.child)
        return res

	# We'll want methods to expand the tree, etc.; these are defined below,
	# using much the same syntax as variables.
	
	# This one adds a previously-defined edge to an existing tree:
    def add_edge(self, ed):
        """add an edge to the tree"""
        self.edge.append(ed)

	# This one creates a new edge and adds it to the tree.
    def new_edge(self, parent, child):
        """add to the tree a new edge from parent to child (node indices)"""
        self.add_edge( Edge(parent,child) )
        
    def update_node2edge(self): # NB: all methods have `self` as the first argument.
      """(Makes a dictionary of nodes and their numbers/names.)     
      dictionary child node index -> edge for fast access to edges.
      also add/update root attribute."""
      self.node2edge = {e.child : e for e in self.edge}
      childrenset = set(self.node2edge.keys())
      rootset = set(e.parent for e in self.edge).difference(childrenset) # `difference` subtracts the elements of a given set that overlap with the other given set.
      if len(rootset) > 1:
          warn("there should be a single root: " + str(rootset)) 
      if len(rootset) == 0:
          raise Exception("there should be at least one root!") # If it has no root, it's a cycle (cyclic graph), not a tree
      self.root = rootset.pop()
      
    def get_dist2root(i):
    	'''find the distance between an edge and the root node. Edges without a defined
    	length are assumed to have length 1.'''
    	pass
    
    def get_path2root():
    	pass
    	
    def root():
    	pass
    	
a = 5
class Foo:
    def __init__(self):
        self.x = a
class Bar:
    a = 6 # will be object attribute: .a , an attribute of *the entire class*, not of 
    	  # specific objects in the class
    b = ["u","v"] # also .b, shared across all Bar objects
    def __init__(self):
        self.x = a
