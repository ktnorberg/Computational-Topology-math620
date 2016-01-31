# Union-Find

The description of the algorithm:

> Using the integers from 1 to n as the names of the vertices, we store each component of the graph as a subset of [n]={1, 2, 3, ..., n}. 

> Adding the edges one at a time and maintaining the system of sets representing the components, we find that the graph is connected iff in the end there is only one set left, namely [n]. 

> Formulated as an abstract data type, we have two operations manipulating the system:

> Find(i): return the name of the set that contains i.

> Union(i, j): assuming i and j belong to different sets in the system, replace the two sets by their union. 

So I read this next part, and I got to thinking, oh!, our problem is that we weren't noticing how the data structure was defined for their solution:


> ...A standard data structure implementing a disjoint set system stores each set as a tree embedded in a linear array, V[1,...,n]. Each node in the tree is equipped with a pointer to its /parent/, except for the /root/ which has no parent... 

Now that I see what kind of data structure the authors have fixed as what their code operates over, the description of the implementation makes more sense to me:

> We implement the find operation by traversing the tree upward until we reach the root, reporting the root as the name of the tree. 

Based on our discussion on Saturday <2016-01-30 Sat>, I'd like to write a way to make the simple way to declare a graph that we discussed -- a list of edges -- into this data structure that the authors describe. That way the implementations they give ought to be more readable. 

Note: The "list of edges" approach leaves out isolated vertices. Since isolated vertices are completely uninteresting for information about components -- they're their own component, whoop-ti-doo -- I will declare that we are concentrating only on the "no isolated vertices" case. 


## Possibly unhelpful helper functions
We will define a graph by a list of its edges. For example, 

```python
example_graph = [[1, 2], [2, 3], [4, 5]]
```

The vertices of a graph, then, are the union of the vertices found in the graph's edges. 

```python
def vertices(graph):
  """Returns a list of the graph's vertices."""
  v = []
  for e in graph:
    v += e
  return list(set(v))
```

The algorithm seems to indicate that we start by assuming that there is one component for every vertex. 

```python
def initial_components(graph):
  """Returns a list of singleton sets of the vertices in the graph, so that union will have something nice to work with."""
  v = vertices(graph)
  return [set([vertex]) for vertex in v]
```

It might be nice to have an =edges= function. The data structure we're writing down graphs in is a list of 2-element lists, but it would be nice to be able to think of the edges as sets. 

```python
def edges(graph):
  """Returns a list of sets, representing the edges in the graph."""
  return [set e for e in graph]
```

In fact, it gives me an idea for a possible algorithm. The two endpoints of one edge are vertices in the same component, right? So, take the list of edges, and see if the first edge has any nonempty intersections with the other edges. When it does, union the two sets together. 

I /think/ that you could go through the whole list of edges, increasing the size of the component the first edge is in. The problem is, you'd have missed some edges when the first edge wasn't incident to an early edge. For example, consider

```python
g = [[1, 2], [3, 4], [4, 5], [5, 2]]
```

Here's what bothers me as I close down on this problem for the night: In the text, it shows trees. Are those trees just representatives of the components, and so are acceptable structures to use (somehow) on graphs that have cycles? How is union-find implemented so as to avoid infinite loops when, say, the parent of a parent of a parent of a vertex is the vertex itself?

