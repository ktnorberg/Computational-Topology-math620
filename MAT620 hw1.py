
def union(lis):
  lis = [set(e) for e in lis]
  res = []
  while True:
    for i in range(len(lis)):
      a = lis[i]
      if res == []:
        res.append(a)
      else:
        pointer = 0 
        while pointer < len(res):
          if a & res[pointer] != set([]) :
            res[pointer] = res[pointer].union(a)
            break
          pointer +=1
        if pointer == len(res):
          res.append(a)
          if res == lis:
              break
    lis,res = res,[]
  return res

'''
def set(x):
    x.parent = x
    x.rank = 0
    

def union(x, y):
    xroot = find(x)
    yroot = find(y)
    if xroot.rank > yroot.rank:
        yroot.parent = xroot
    elif xroot.rank < yroot.rank:
        xroot.parent = yroot
    elif xroot != yroot:
        yroot.parent = xroot
        xroot.rank = xroot.rank +1

        
def find(x):
    if x.parent == x:
        return x
    else:
        x.parent = find(x.parent)
        return x.parent
'''




'''
class node:
    def _init_(self, parent, rank = 0):
        self.parent = parent
        self.rank = rank

def find(n):
        if n != n.parent:
            n.parent = find(n.parent)
        return n.parent

def merge(n, n1, n2):
    set_val_1 = find(n, n1)
    set_val_1 = find(n, n2)
    if set_val_1.rank > set_val_2.rank:
        set_val_2.parent = set_val_1
    else:
        set_val_1.parent = set_val_2
        if set_val_1.rank == set_val_2.rank:
            set_val_2.rank += 1

def MakeSet(n):
     x.parent = n
     x.rank   = 0

def SameSet(n1, n2):
    return find(n1) == find(n2)
'''            


'''
from collections import defaultdict


class UF:
    def _init_(self, N):
        self._id = list(range(N))
        self._count = N
        self._rank = [0] * N
        self._N = N
        self._symbol_to_index = {}
        self._index_to_symbol = {}

        
        
    def find(self, p):
        if isinstance(p, int) and p < self._N and \
           p not in self._index_to_symbol:
            self._symbol_to_index[p] = p
            self._index_to_symbol[p] = p
        else:
            self._symbol_to_index.setdefault(p, len(self._symbol_to_index))
            self._index_to_symbol.setdefault(self._symbol_to_index[p], p)
        i = self._symbol_to_index[p]
        if i >=self._N:
            raise IndexError('You have been exceeding the UF capacity')

            id = self._id
            while i != id[i]:
                id[i] = id[id[i]]
                i = id[i]
            return i
        
        def count(self):
            return self._count

        def connected(self, p, q):
            return self.find(p) == self.find(q)

        def union(self, p, q):
            id = self._id
            rank = self._rank

            i = self.find(p)
            j = self.find(q)
            if i ==j:
                return

            self._count -= 1
            if rank[i] <rank[j]:
                id[i] = j
            elif rank[i] > rank[j]:
                id[j] = i
            else:
                id[j] = i
                rank[i] += 1

        def get_components(self):
            d = defaultdict(set)
            for i, j in enumerate(self._id):
                d[self.find(self._index_to_symbol.get(j, j))].add(
                    self._index_to_symbol.get(i,i)
                    )
                return list(d.values())

            def _str_(self):
                return ' '.join([str(x) for x in self._id])

            def _repr_(self):
                return "UF(" + str(self) + ")"

        if _name_ == "_main_":
            print("Union find data structure.")
            N = int(raw_input("Enter number of items: "))
            uf = UF(N)
            print("Enter a sequence of space separated pairs of integers: ")
            while True:
                try:
                    p, q = [int(x) for x in raw_input().split()]
                    uf.union(p,q)
                except:
                    break

            print(str(uf.count()) + " components: " + str(uf))
            '''



'''            
class UnionFind:
    """Union-find data structure.

    Each unionFind instance X maintains a family of disjoint sets of
    hashable objects, supporting the following two methods:

    - X[item] returns a name for the set containing the given item.
      Each set is named by an arbitrarily-chosen one of its members; as
      long as the set remains unchanged it will keep the same name. If
      the item is not yet part of a set in X, a new singleton set is
      created for it.

    - X.union(item1, item2, ...) merges the sets containing each item
      into a single larger set.  If any item is not yet part of a set
      in X, it is added to X as one of the members of the merged set.
    """

    def __init__(self):
        """Create a new empty union-find structure."""
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        """Find and return the name of the set containing the object."""

        # check for previously unknown object
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root
        
    def __iter__(self):
        """Iterate through all items ever found or unioned by this structure."""
        return iter(self.parents)

    def union(self, *objects):
        """Find the sets containing the objects and merge them all."""
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest
print (X)
'''


'''
class DisjointSet(object):

    def __init__(self):
        self.leader = {} # maps a member to the group's leader
        self.group = {} # maps a group leader to the group (which is a set)

    def add(self, a, b):
        leadera = self.leader.get(a)
        leaderb = self.leader.get(b)
        if leadera is not None:
            if leaderb is not None:
                if leadera == leaderb: return # nothing to do
                groupa = self.group[leadera]
                groupb = self.group[leaderb]
                if len(groupa) < len(groupb):
                    a, leadera, groupa, b, leaderb, groupb = b, leaderb, groupb, a, leadera, groupa
                groupa |= groupb
                del self.group[leaderb]
                for k in groupb:
                    self.leader[k] = leadera
            else:
                self.group[leadera].add(b)
                self.leader[b] = leadera
        else:
            if leaderb is not None:
                self.group[leaderb].add(a)
                self.leader[a] = leaderb
            else:
                self.leader[a] = self.leader[b] = a
                self.group[a] = set([a, b])

data = """T1 T2
T3 T4
"""
# data is chosen to demonstrate each of 5 paths in the code
from pprint import pprint as pp
ds = DisjointSet()
for line in data.splitlines():
    x, y = line.split()
    ds.add(x, y)
    print
    print (x, y)
    pp(ds.leader)
    pp(ds.group)


"""
MakeSet(x) initializes disjoint set for object x
Find(x) returns representative object of the set containing x
Union(x,y) makes two sets containing x and y respectively into one set

Some Applications:
- Kruskal's algorithm for finding minimal spanning trees
- Finding connected components in graphs
- Finding connected components in images (binary)
"""
'''

'''
def MakeSet(x):
     x.parent = x
     x.rank   = 0

def Union(x, y):
     xRoot = Find(x)
     yRoot = Find(y)
     if xRoot.rank > yRoot.rank:
         yRoot.parent = xRoot
     elif xRoot.rank < yRoot.rank:
         xRoot.parent = yRoot
     elif xRoot != yRoot: # Unless x and y are already in same set, merge them
         yRoot.parent = xRoot
         xRoot.rank = xRoot.rank + 1

def Find(x):
     if x.parent == x:
        return x
     else:
        x.parent = Find(x.parent)
        return x.parent

""""""""""""""""""""""""""""""""""""""""""
# sample code using Union-Find (not needed)

import itertools

class Node:
    def __init__ (self, label):
        self.label = label
    def __str__(self):
        return self.label
    
l = [Node(ch) for ch in "abcdefg"]      #list of seven objects with distinct labels
print ("")
print ("objects labels:\t\t\t"), [str(i) for i in l]

[MakeSet(node) for node in l]       #starting with every object in its own set

sets =  [str(Find(x)) for x in l]
print ("set representatives:\t\t"), sets
print ("number of disjoint sets:\t"), len([i for i in itertools.groupby(sets)])

assert( Find(l[0]) != Find(l[2]) )
Union(l[0],l[2])        #joining first and third
assert( Find(l[0]) == Find(l[2]) )

assert( Find(l[0]) != Find(l[1]) )
assert( Find(l[2]) != Find(l[1]) )
Union(l[0],l[1])        #joining first and second
assert( Find(l[0]) == Find(l[1]) )
assert( Find(l[2]) == Find(l[1]) )

Union(l[-2],l[-1])        #joining last two sets
Union(l[-3],l[-1])        #joining last two sets

sets = [str(Find(x)) for x in l]
print ("set representatives:\t\t"), sets
print ("number of disjoint sets:\t"), len([i for i in itertools.groupby(sets)])

for o in l:
    del o.parent
'''
