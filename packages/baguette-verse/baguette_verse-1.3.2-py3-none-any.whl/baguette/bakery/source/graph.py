"""
This module defines all graph-related base classes.
Look at the classes Vertex, Edge, Arrow and Graph.
Vertex, Edge and Arrow classes are heavily subclasses in BAGUETTE. Look at package 'baguette.bakery.source.types' to know more.
"""

from threading import RLock, Thread
from typing import Any, Callable, Iterable, Iterator, Never, Optional, TypeVar, TypedDict, Union
from weakref import WeakKeyDictionary, WeakValueDictionary
from .colors import Color
from .config import ColorSetting, SizeSetting, SwitchSetting, WeightSetting
from Viper.meta.iterable import InstanceReferencingClass
from Viper.collections import IsoSet

__all__ = ["Vertex", "Edge", "Arrow", "Graph", "FrozenGraph", "find_or_create"]





class Vertex(metaclass = InstanceReferencingClass):

    """
    A vertex for a graph. Can be linked to other vertices and added to a graph.
    """

    __slots__ = {
        "edges" : "The set of edges linking this vertex to others.",
        "parent" : "A vertex that 'contains' this one.",
        "children" : "The tuple of vertices (directly) contained by this one.",
        "graph" : "The graph object containing this vertex",
        "__size" : "The customized size of the vertex",
        "__color" : "The customized color of the vertex"
        }
    
    __pickle_slots__ = {
        "color",
        "parent",
        "size"
    }

    default_color = ColorSetting(Color.white)
    default_size = SizeSetting(2.0)

    def __init__(self, *, parent : Optional["Vertex"] = None) -> None:
        from .colors import Color
        if parent != None and not isinstance(parent, Vertex):
            raise TypeError("Expected vertex for parent, got " + repr(parent.__class__.__name__))
        self.edges : set[Edge] = set()
        self.__color : Color | None = None
        self.__size : float | None = None
        self.parent : Vertex | None = parent
        self.graph : Graph | None = None
        if parent:
            parent.children += (self, )
        self.children : tuple[Vertex, ...] = ()
        for g in Graph.active_graphs():
            g.vertices.add(self)

    __vertexing = False
    __comparing : set[tuple["Vertex", ...]] = set()

    @property
    def color(self) -> Color:
        """
        The Color of this Vertex.
        """
        if self.__color is not None:
            return self.__color
        return self.default_color
    
    @color.setter
    def color(self, value : Color):
        from .colors import Color
        if not isinstance(value, Color):
            raise TypeError(f"Expected Color, got '{type(value).__name__}'")
        self.__color = value

    @color.deleter
    def color(self):
        self.__color = None

    @property
    def size(self) -> float:
        """
        The size of this Vertex.
        """
        if self.__size is not None:
            return self.__size
        return self.default_size
    
    @size.setter
    def size(self, value : float):
        if not isinstance(value, float):
            try:
                value = float(value)
            except:
                pass
        if not isinstance(value, float):
            raise TypeError("Expected float, got " + repr(type(value).__name__))
        if value < 0 or value in (float("inf"), float("nan")):
            raise ValueError("Expected positive finite number for size, got " + repr(value))
        self.__size = value
    
    @size.deleter
    def size(self):
        self.__size = None

    @property
    def label(self) -> str:
        """
        The label used when plotting this vertex.
        """
        return type(self).__name__

    def __repr__(self) -> str:
        """
        Implements repr(self)
        """
        if Vertex.__vertexing:
            return str(type(self)) + "()"
        Vertex.__vertexing = True
        r = type(self).__name__ + "(" + ", ".join(str(name) + " = " + str(getattr(self, name)) for name in self.__slots__ if not name.startswith("_")) + ")"
        Vertex.__vertexing = False
        return r
    
    def __str__(self) -> str:
        """
        Implements str(self)
        """
        if Vertex.__vertexing:
            return str(type(self))
        Vertex.__vertexing = True
        r = "(" + ", ".join(str(name) + " = " + str(getattr(self, name)) for name in self.__slots__ if not name.startswith("_")) + ")"
        Vertex.__vertexing = False
        return r
    
    # def __hash__(self) -> int:
    #     """
    #     Implements hash(self)
    #     """
    #     n = 0
    #     for name in dir(self):
    #         if not name.startswith("__") and not name.endswith("__") and name not in Vertex.__slots__:
    #             try:
    #                 n += hash(name) * hash(getattr(self, name))
    #             except:
    #                 pass
    #     return n
    
    # def __eq__(self, o: object) -> bool:
    #     """
    #     Implements self == o
    #     """
    #     if self is o:
    #         return True
    #     if (self, o) in self.__comparing or (o, self) in self.__comparing:
    #         return True
    #     if type(self) != type(o):
    #         return False
    #     self.__comparing.add((self, o))
    #     res = all(getattr(self, name) == getattr(o, name) for name in type(self).__slots__)
    #     self.__comparing.remove((self, o))
    #     return res
    
    def __reduce__(self) -> str | tuple[Any, ...]:
        """
        Implements dumping of self
        """
        # Note : When serializing a vertex, the edges/arrows should not be serialized. These will be handled independently when serializing a graph.
        pickle_data = super().__reduce__()
        if isinstance(pickle_data, str):
            raise TypeError("Expected tuple from parent's __reduce__, got str")
        func, args, state = pickle_data
        state : dict
        if "edges" in state or "graph" in state:
            raise RuntimeError("Cannot pickle edges or graph of a vertex")
        return type(self), (), state
    
    def __setstate__(self, state : dict[str, Any]):
        """
        Implements loading of self
        """
        for k, v in state.items():
            setattr(self, k, v)
    
    def __getstate__(self) -> dict[str, Any]:
        """
        Implements dumping of self
        """
        from .utils import extract_pickle_slots
        return {name : getattr(self, name) for name in extract_pickle_slots(type(self))}
    
    def __copy__(self) -> "Vertex":
        """
        Implements copy of self
        """
        from inspect import ismethod
        cp = type(self)()
        cp.color = self.color
        for name in dir(self):
            if not name.startswith("_") and not name.endswith("_") and name not in Vertex.__slots__ and not ismethod(getattr(self, name)):
                setattr(cp, name, getattr(self, name))
        return cp
    
    def __deepcopy__(self, memo : dict[int, Any]) -> "Vertex":
        """
        Implements deepcopy of self
        """
        from copy import deepcopy
        from inspect import ismethod
        cp = type(self)()
        cp.color = self.color
        memo[id(self)] = cp
        for name in dir(self):
            if not name.startswith("_") and not name.endswith("_") and name not in Vertex.__slots__ and not ismethod(getattr(self, name)):
                setattr(cp, name, deepcopy(getattr(self, name), memo))
        return cp
                    
    def neighbors(self) -> Iterator["Vertex"]:
        """
        Iterates over all the neighbor vertices.
        """
        for e in self.edges:
            if e.source is self:
                yield e.destination
            else:
                yield e.source
    
    def outwards(self) -> Iterator["Vertex"]:
        """
        Iterates over the outwards neighbors of this vertex (neighbors linked by an outgoing arrow).
        """
        for e in self.edges:
            if isinstance(e, Arrow) and e.source is self:
                yield e.destination
    
    def inwards(self) -> Iterator["Vertex"]:
        """
        Iterates over the inwards neighbors of this vertex (neighbors linked by an incomming arrow).
        """
        for e in self.edges:
            if isinstance(e, Arrow) and e.destination is self:
                yield e.source
    
    def linked(self) -> Iterator["Vertex"]:
        """
        Iterates over the undirected neighbors if this vertex (neighbors linked by a strict edge).
        """
        for e in self.edges:
            if not isinstance(e, Arrow):
                yield (e.source if e is not e.source else e.destination)

    def connect(self, o : "Vertex", *, directional : bool = False) -> None:
        """
        Links this vertex to another. Directional indicates if the link should be an arrow instead of an edge.
        """
        if not isinstance(o, Vertex):
            raise TypeError("Expected vertex, got " + repr(o.__class__.__name__))
        if not isinstance(directional, bool):
            raise TypeError("Expected bool for directional, got" + repr(directional.__class__.__name__))
        if directional:
            e = Arrow(self, o)
        else:
            e = Edge(self, o)
        e.write()

    @classmethod
    def add_vertices_to_graph(cls : type["Vertex"], G : "Graph", fil : Optional[Callable[["Vertex"], bool]] = None):
        """
        Adds all vertices of this class to a graph.
        If given a filter function fil, only filtered vertices will be added.
        """
        if not isinstance(G, Graph):
            raise TypeError("Expected graph, got " + repr(G.__class__.__name__))
        if fil != None and not callable(fil):
            raise TypeError("Expected callable for filter, got " + repr(fil.__class__.__name__))
        if fil == None:
            G.vertices.update(cls)
        else:
            G.vertices.update(filter(fil, cls))
            




class Edge(metaclass = InstanceReferencingClass):

    """
    An (undirected) edge for a graph. Links two vertices together.
    """

    __slots__ = {
        "source" : "The source vertex.",
        "destination" : "The destination vertex.",
        "__weight" : "The customized weight of the edge",
        "__color" : "The customized color of the edge"
    }

    __pickle_slots__ = {
        "color",
        "source",
        "destination",
        "weight"
    }

    default_color = ColorSetting(Color.white)
    default_weight = WeightSetting(1.0)

    blend_vertices_colors = SwitchSetting(True)

    def __init__(self, source : Vertex, destination : Vertex, *, auto_write : bool = True) -> None:
        from .colors import Color
        if not isinstance(source, Vertex) or not isinstance(destination, Vertex):
            raise TypeError("Expected vertex, vertex, got " + repr(source.__class__.__name__) + " and " + repr(destination.__class__.__name__))
        if not isinstance(auto_write, bool):
            raise TypeError("Expected bool for write, got " + repr(auto_write.__class__.__name__))
        self.source : Vertex = source
        self.destination : Vertex = destination
        self.__color : Color | None = None
        self.__weight : float | None = None
        if auto_write:
            self.write()
        for g in Graph.active_graphs():
            g.edges.add(self)

    @property
    def color(self) -> Color:
        """
        The Color of this Vertex.
        """
        if self.__color is not None:
            return self.__color
        if self.blend_vertices_colors:
            from .colors import Color
            return Color.average(self.source.color, self.destination.color)
        else:
            return self.default_color
    
    @color.setter
    def color(self, value : Color):
        from .colors import Color
        if not isinstance(value, Color):
            raise TypeError(f"Expected Color, got '{type(value).__name__}'")
        self.__color = value

    @color.deleter
    def color(self):
        self.__color = None
        
    @property
    def weight(self) -> float:
        """
        The weight of this Edge.
        """
        if self.__weight is not None:
            return self.__weight
        return self.default_weight
    
    @weight.setter
    def weight(self, value : float):
        if not isinstance(value, float):
            try:
                value = float(value)
            except:
                pass
        if not isinstance(value, float):
            raise TypeError("Expected float for weight, got " + repr(type(value).__name__))
        if value < 0 or value in (float("inf"), float("nan")):
            raise ValueError("Expected positive finite number for weight, got " + repr(value))
        self.__weight = value

    @weight.deleter
    def weight(self):
        self.__weight = None

    @property
    def label(self) -> str:
        """
        The label used when plotting this edge.
        """
        return type(self).__name__
    
    def __repr__(self) -> str:
        """
        Implements repr(self)
        """
        return "edge(" + repr(self.source) + ", " + repr(self.destination) + ")"
    
    def __str__(self) -> str:
        """
        Implements str(self)
        """
        return str(self.source) + " -- " + str(self.destination)
    
    def __hash__(self) -> int:
        """
        Implements hash(self)
        """
        return hash(hash(self.source) + hash(type(self)) + hash(self.destination))
    
    def __eq__(self, o: object) -> bool:
        """
        Implements self == o
        """
        if not isinstance(o, type(self)):
            return False
        return (self.source == o.source and self.destination == o.destination) or (self.source == o.destination and self.destination == o.source)
        
    def __setstate__(self, state : dict[str, Any]):
        """
        Implements loading of self
        """
        for k, v in state.items():
            setattr(self, k, v)
    
    def __getstate__(self) -> dict[str, Any]:
        """
        Implements dumping of self
        """
        from .utils import extract_pickle_slots
        return {name : getattr(self, name) for name in extract_pickle_slots(type(self))}
    
    def __copy__(self) -> "Edge":
        """
        Implements copy(self)
        """
        raise NotImplementedError
        
    def write(self):
        """
        Writes this edge in the edges sets of both vertices.
        """
        self.source.edges.add(self)
        self.destination.edges.add(self)
        if self.source.graph:
            self.source.graph.edges.add(self)
        elif self.destination.graph:
            self.destination.graph.edges.add(self)
    
    def delete(self) -> tuple[Vertex, Vertex]:
        """
        Deletes the link. (Deletes it from the vertices egde sets)
        """
        self.source.edges.discard(self)
        self.destination.edges.discard(self)
        if self.source.graph:
            self.source.graph.edges.discard(self)
        elif self.destination.graph:
            self.destination.graph.edges.discard(self)
        return self.source, self.destination
    
    @classmethod
    def add_edges_to_graph(cls : type["Edge"], G : "Graph", fil : Optional[Callable[["Edge"], bool]] = None):
        """
        Adds all edges of this class to a graph.
        If given a filter function fil, only filtered edges will be added.
        """
        if not isinstance(G, Graph):
            raise TypeError("Expected graph, got " + repr(G.__class__.__name__))
        if fil != None and not callable(fil):
            raise TypeError("Expected callable for filter, got " + repr(fil.__class__.__name__))
        if fil == None:
            G.edges.update(cls)
        else:
            G.edges.update(filter(fil, cls))

    
        


class Arrow(Edge):

    """
    An arrow (directed) for a graph. Links two vertices together.
    """
    
    def __repr__(self) -> str:
        """
        Implements repr(self).
        """
        return "arrow(" + repr(self.source) + ", " + repr(self.destination) + ")"
    
    def __str__(self) -> str:
        """
        Implements str(self).
        """
        return str(self.source) + " --> " + str(self.destination)
    
    def __hash__(self) -> int:
        """
        Implements hash(self).
        """
        return hash(-hash(self.source) + hash(type(self)) + hash(self.destination))
    
    def __eq__(self, o: object) -> bool:
        """
        Implements self == o.
        """
        if not isinstance(o, type(self)):
            return False
        return self.source == o.source and self.destination == o.destination
    





CLS = TypeVar("CLS", bound=Vertex)

def find_or_create(cls : type[CLS], **kwargs) -> tuple[CLS, bool]:
    """
    Finds in the given class cls for a vertex which attributes have values matching the given keyword arguments.
    If there is one, returns it. Otherwise, creates it.
    Returns the object and a boolean indicating if the object existed before.
    """
    for ist in cls:
        if all(hasattr(ist, name) and getattr(ist, name) == value for name, value in kwargs.items()):
            return ist, True
    ist = cls()
    for name, value in kwargs.items():
        setattr(ist, name, value)
    return ist, False





class _GraphStateDict(TypedDict):

    vertices : IsoSet[Vertex]
    edges : IsoSet[Edge]
    data : dict[str, Any]

class Graph:

    """
    A graph class. Add starting vertices and use explore() to complete the graph.
    Graph can be used in context managers to append all Vertices and Edges created in the current thread to the context Graph:
    >>> G = Graph()
    >>> with G:
    ...     u = Vertex()
    ...     e = Edge(u, u)
    ... 
    >>> u in G.vertices:
    True
    >>> e in G.edges:
    True
    """

    from Viper.collections.isomorph import IsoSet as __IsoSet, IsoDict as __IsoDict
    from typing import Iterable as __Iterable
    from threading import current_thread as __current_thread

    __slots__ = {
        "vertices" : "The set of vertices in this graph",
        "edges" : "The set of edges in this graph",
        "data" : "A dictionary holding additional data for this graph",
        "__weakref__" : "A slot for weak references to Graph objects"
    }

    __active_graphs : WeakKeyDictionary[Thread, dict[int, bool]] = WeakKeyDictionary()
    __graphs : WeakValueDictionary[int, "Graph"] = WeakValueDictionary()

    def __init__(self, vertices_or_edges : Iterable[Vertex | Edge] = ()) -> None:
        Graph.__graphs[id(self)] = self
        self.vertices : Graph.__IsoSet[Vertex] = Graph.__IsoSet()
        self.edges : Graph.__IsoSet[Edge] = Graph.__IsoSet()
        self.data : "dict[str, Any]" = {}
        if not isinstance(vertices_or_edges, Graph.__Iterable):
            raise TypeError(f"Expected iterable, got '{type(vertices_or_edges).__name__}'")
        if not isinstance(vertices_or_edges, Graph.__Iterable):
            raise TypeError("Expected iterable, got " + repr(vertices_or_edges.__class__.__name__))
        for value in vertices_or_edges:
            if isinstance(value, Vertex):
                self.vertices.add(value)
                value.graph = self
            elif isinstance(value, Edge):
                value.write()
                self.edges.add(value)
            else:
                raise TypeError("Expected edge or vertex, got " + repr(value.__class__.__name__))

    def __eq__(self, other : object) -> bool:
        """
        Implements self == other.
        """
        if not isinstance(other, Graph):
            return NotImplemented
        return self.vertices.iso_view == other.vertices.iso_view and self.edges.iso_view == other.edges.iso_view

    def __ge__(self, other : "Graph") -> bool:
        """
        Implements self >= other.
        """
        if not isinstance(other, Graph):
            return NotImplemented
        return self.vertices.iso_view >= other.vertices.iso_view and self.edges.iso_view >= other.edges.iso_view
    
    def __gt__(self, other : "Graph") -> bool:
        """
        Implements self > other.
        """
        if not isinstance(other, Graph):
            return NotImplemented
        return self.vertices.iso_view > other.vertices.iso_view and self.edges.iso_view > other.edges.iso_view
    
    def __le__(self, other : "Graph") -> bool:
        """
        Implements self <= other.
        """
        if not isinstance(other, Graph):
            return NotImplemented
        return self.vertices.iso_view <= other.vertices.iso_view and self.edges.iso_view <= other.edges.iso_view
    
    def __lt__(self, other : "Graph") -> bool:
        """
        Implements self < other.
        """
        if not isinstance(other, Graph):
            return NotImplemented
        return self.vertices.iso_view < other.vertices.iso_view and self.edges.iso_view < other.edges.iso_view
    
    def __enter__(self):
        """
        Implements with self.
        """
        Graph.__active_graphs.setdefault(Graph.__current_thread(), {})[id(self)] = True
    
    def __exit__(self, exc_type, exc_value, traceback):
        """
        Implements with self.
        """
        Graph.__active_graphs[Graph.__current_thread()].pop(id(self))
    
    @staticmethod
    def active_graphs() -> list["Graph"]:
        """
        Returns the list of all the active Graphs in the current thread.
        """
        if Graph.__current_thread() not in Graph.__active_graphs:
            return []
        return [Graph.__graphs[i] for i, inserting in Graph.__active_graphs[Graph.__current_thread()].items() if inserting]
    
    @staticmethod
    def graphs_status() -> list[tuple["Graph", bool]]:
        """
        More advanced version of active_graphs. Returns a dictionary of Graphs that indicates if they are in auto_write mode.
        """
        if Graph.__current_thread() not in Graph.__active_graphs:
            return []
        return [(Graph.__graphs[i], inserting) for i, inserting in Graph.__active_graphs[Graph.__current_thread()].items()]

    def explore(self, source : Optional[Vertex] = None) -> None:
        """
        Explores the graph for more linked vertices. If a vertex of the graph is given, only searches starting from that vertex. Otherwise, searches from all vertices.
        """
        if source == None:
            to_explore = self.vertices.copy()
        else:
            if not isinstance(source, Vertex):
                raise TypeError("Expected vertex, got " + repr(source.__class__.__name__))
            if source not in self.vertices:
                raise KeyError("Vertex not in graph.")
            to_explore = {source}
        from itertools import chain
        seen_vertices = set()
        seen_edges = set()
        while to_explore:
            u = to_explore.pop()
            seen_vertices.add(u)
            seen_edges.update(u.edges)
            u.graph = self
            next_vertices = chain(u.neighbors(), iter(u.children))
            if u.parent:
                next_vertices = chain(next_vertices, (u.parent, ))
            new = set()
            for v in next_vertices:
                if v not in seen_vertices:
                    new.add(v)
            to_explore.update(new)
        self.vertices.update(seen_vertices)
        self.edges.update(seen_edges)

    def pairs(self) -> Iterator[tuple[Vertex, Edge, Vertex]]:
        """
        Yields all (vertex u, edge e, vertex v) tuples where (u, v) is a pair of linked vertices. e may be an edge or an arrow directed from u to v.
        """
        for e in self.edges:
            yield e.source, e, e.destination

    def __len__(self) -> int:
        """
        Implements len(self). Returns the number of vertices.
        """
        return len(self.vertices)
    
    def __contains__(self, vertex_or_edge : Vertex | Edge) -> bool:
        """
        Implements vertex_or_edge in self. Returns True if the given Vertex or Edge is in the Graph.
        """
        if isinstance(vertex_or_edge, Vertex):
            return vertex_or_edge in self.vertices
        elif isinstance(vertex_or_edge, Edge):
            return vertex_or_edge in self.edges
        else:
            raise TypeError(f"Expected Vertex or Edge, got '{type(vertex_or_edge).__name__}'")
    
    @property
    def n(self) -> int:
        """
        The number of vertices.
        """
        return len(self)
    
    @property
    def m(self) -> int:
        """
        The number of edges and arrows.
        """
        return len(self.edges)
        
    def append(self, value : Vertex | Edge, explore : bool = False):
        """
        Adds a vertex or an edge to the graph.
        If explore is True, explores the graph from the added vertex or the source vertex of the added edge.
        """
        if not isinstance(explore, bool):
            raise TypeError("Expected bool for explore, got " + repr(explore.__class__.__name__))
        if isinstance(value, Vertex):
            self.vertices.add(value)
            value.graph = self
            if explore:
                self.explore(value)
        elif isinstance(value, Edge):
            value.write()
            self.edges.add(value)
            if explore:
                self.explore(value.source)
        else:
            raise TypeError("Expected edge or vertex, got " + repr(value.__class__.__name__))
    
    def remove(self, value : Vertex | Edge):
        """
        Removes a vertex or an edge from the graph.
        When removing a vertex, it will also remove all edges/arrows connected to it.
        """
        if isinstance(value, Vertex):
            self.edges.difference_update(value.edges)
            for e in value.edges.copy(): 
                e.source.edges.discard(e)
                e.destination.edges.discard(e)
            self.vertices.discard(value)
        elif isinstance(value, Edge):
            self.edges.discard(value)
            value.source.edges.discard(value)
            value.destination.edges.discard(value)
        else:
            raise TypeError("Expected edge or vertex, got " + repr(type(value).__name__))

    def extend(self, values : Iterable[Vertex | Edge], explore : bool = False):
        """
        Extends the graph with an iterable of vertices and/or edges.
        """
        from typing import Iterable
        if not isinstance(explore, bool):
            raise TypeError("Expected bool for explore, got " + repr(explore.__class__.__name__))
        if not isinstance(values, Iterable):
            raise TypeError("Expected iterable, got " + repr(values.__class__.__name__))
        for value in values:
            if isinstance(value, Vertex):
                self.vertices.add(value)
                value.graph = self
                if explore:
                    self.explore(value)
            elif isinstance(value, Edge):
                value.write()
                self.edges.add(value)
                if explore:
                    self.explore(value.source)
            else:
                raise TypeError("Expected edge or vertex, got " + repr(value.__class__.__name__))
        
    def paint(self, c : Color):
        """
        Changes the colors of all vertices and edges/arrows of this graph to the given Color.
        """
        from .colors import Color
        if not isinstance(c, Color):
            raise TypeError("Expected Color, got " + repr(type(c).__name__))
        for u in self.vertices:
            u.color = c
        for e in self.edges:
            e.color = c

    def __getstate__(self) -> _GraphStateDict:
        """
        Implements dumping of self.
        """
        return {
            "vertices" : self.vertices,
            "edges" : self.edges, 
            "data" : self.data
        }

    def __setstate__(self, state : _GraphStateDict):
        """
        Implements loading of self. Note that subclass attributes must be handled by the user.
        """
        thread_dict = Graph.__active_graphs.get(Graph.__current_thread(), default={})
        thread_dict[id(self)] = False       # This is a weak graph activation. It does not trigger auto_insertion.
        Graph.__graphs[id(self)] = self
        try:
            for name in ("vertices", "edges", "data"):
                setattr(self, name, state[name])
            if isinstance(self.vertices, set):       # For compatibility issues (before IsoSets)
                self.vertices = Graph.__IsoSet(self.vertices)
            if isinstance(self.edges, set):
                self.edges = Graph.__IsoSet(self.edges)
            for v in self.vertices:
                v.graph = self
            for e in self.edges:
                e.write()
        finally:
            thread_dict.pop(id(self))
   
    # def __copy__(self) -> "graph":
    #     """
    #     Implements copy of self
    #     """
    #     from copy import copy
    #     translation = {u : copy(u) for u in self.vertices}
    #     cp = graph()
    #     cp.vertices.update(translation.values())
    #     for u, e, v in self.pairs():
    #         e = copy(e)
    #         e.source = translation[u]
    #         e.destination = translation[v]
    #         e.write()
    #     return cp
    
    # def __deepcopy__(self, memo : Dict[int, Any]) -> "graph":
    #     """
    #     Implements deepcopy of self
    #     """
    #     from copy import deepcopy
    #     translation = {u : deepcopy(u, memo) for u in self.vertices}
    #     cp = graph()
    #     cp.vertices.update(translation.values())
    #     for u, e, v in self.pairs():
    #         e = deepcopy(e, memo)
    #         e.source = translation[u]
    #         e.destination = translation[v]
    #         e.write()
    #     return cp

    def export(self, file : str, *, subgraph_supported : bool = False) -> None:
        """
        Writes this graph under the GEXF format into given file.
        """
        # List of possible attributes to include in visuals :
        # Node Size : proportional to radius! not surface area!
        # Color : R, G, B
        # Node Shape : Any of "disc", "square", "triangle" or "diamond"
        # Edge Thickness : same as weight?
        # Edge Shape : Any of "solid", "dotted", "dashed" or "double"
        from datetime import date
        import json

        forbidden_characters : dict[int, str] = {i : "�" for i in range(32) if chr(i) not in {"\n", "\t", "\r"}}

        if not isinstance(subgraph_supported, bool):
            raise TypeError("Expected bool for subgraph_supported, got " + repr(subgraph_supported.__class__.__name__))
        try:
            with open(file, "wb") as f:
                import xml.etree.ElementTree as ET
                head = b'<?xml version="1.0" encoding="UTF-8"?>'
                root = ET.Element("gexf", attrib={"xmlns":"http://www.gexf.net/1.3", "version":"1.3", "xmlns:viz":"http://www.gexf.net/1.3/viz", "xmlns:xsi":"http://www.w3.org/2001/XMLSchema-instance", "xsi:schemaLocation":"http://www.gexf.net/1.3 http://www.gexf.net/1.3/gexf.xsd"})
                meta = ET.SubElement(root, "meta", lastmodifieddate=date.today().isoformat())
                creator = ET.SubElement(meta, "creator")
                creator.text = "Graph Builder"
                description = ET.SubElement(meta, "description")
                description.text = ""
                graph = ET.SubElement(root, "graph", mode="static")
                node_attr = ET.SubElement(graph, "attributes", **{"class" : "node", "mode" : "static"})
                node_attributes = {}
                edge_attr = ET.SubElement(graph, "attributes", **{"class" : "edge", "mode" : "static"})
                edge_attributes = {}
                nodes = ET.SubElement(graph, "nodes")
                edges = ET.SubElement(graph, "edges")
                n_ids = Graph.__IsoDict((u, i) for i, u in enumerate(self.vertices))
                additional_links : set[tuple[Vertex, Vertex]] = set()
                for u, i in n_ids.items():
                    d = {name : str(getattr(u, name)).translate(forbidden_characters) for name in u.__pickle_slots__ if not name.startswith("_")}
                    d["Type"] = type(u).__name__
                    if "__weakref__" in d:
                        d = {}
                    if u.parent:
                        if subgraph_supported:
                            node_i = ET.SubElement(nodes, "node", id=str(i), label=u.label.translate(forbidden_characters), pid=str(n_ids[u.parent]))
                        else:
                            node_i = ET.SubElement(nodes, "node", id=str(i), label=u.label.translate(forbidden_characters))
                            additional_links.add((u.parent, u))
                    else:
                        node_i = ET.SubElement(nodes, "node", id=str(i), label=u.label.translate(forbidden_characters))
                    attr_i = ET.SubElement(node_i, "attvalues")
                    for name, value in d.items():
                        if name not in node_attributes:
                            node_attributes[name] = ET.SubElement(node_attr, "attribute", id=name, title=name, type="string")
                        if isinstance(value, (dict, list)):
                            try:
                                svalue = json.dumps(value, indent = "\t")
                            except:
                                svalue = str(value)
                        else:
                            svalue = str(value)
                        ET.SubElement(attr_i, "attvalue", **{"for" : name, "value" : svalue.translate(forbidden_characters)})
                    size = ET.SubElement(node_i, "viz:size", value=str(u.size))
                    color = ET.SubElement(node_i, "viz:color", r=str(int(u.color.R * 255)), g=str(int(u.color.G * 255)), b=str(int(u.color.B * 255)))
                for u, e, v in self.pairs():
                    if u not in n_ids:
                        continue
                    if v not in n_ids:
                        continue
                    d = {name : str(getattr(e, name)).translate(forbidden_characters) for name in e.__pickle_slots__ if not name.startswith("_")}
                    d["Type"] = type(e).__name__
                    if "__weakref__" in d:
                        d = {}
                    try:
                        edge_i = ET.SubElement(edges, "edge", source=str(n_ids[u]), target=str(n_ids[v]), type=("directed" if isinstance(e, Arrow) else "undirected"), label=e.label.translate(forbidden_characters), attrib=d, weight=str(e.weight))
                    except KeyError:
                        raise
                    color = ET.SubElement(edge_i, "viz:color", r=str(int(e.color.R * 255)), g=str(int(e.color.G * 255)), b=str(int(e.color.B * 255)))
                    attr_i = ET.SubElement(edge_i, "attvalues")
                    for name, value in d.items():
                        if name not in edge_attributes:
                            edge_attributes[name] = ET.SubElement(edge_attr, "attribute", id=name, title=name, type="string")
                        if isinstance(value, (dict, list)):
                            try:
                                svalue = json.dumps(value, indent = "\t")
                            except:
                                svalue = str(value)
                        else:
                            svalue = str(value)
                        ET.SubElement(attr_i, "attvalue", **{"for" : name, "value" : svalue.translate(forbidden_characters)})
                for u, v in additional_links:
                    edge_i = ET.SubElement(edges, "edge", source=str(n_ids[u]), target=str(n_ids[v]), type="directed", label="contains", weight="1.0")
                f.write(head + b"\n")
                ET.indent(root, "\t")
                for line in ET.tostringlist(root):
                    f.write(line + b"\n")
        except Exception as E:
            raise





class FrozenGraph(Graph):
    
    """
    Frozen (immutable) version of Graphs.
    """

    from Viper.collections import FrozenIsoSet as __FrozenIsoSet, IsoSet as __IsoSet

    def __init__(self, vertices_or_edges: Iterable[Vertex | Edge] = ()) -> None:
        super().__init__(vertices_or_edges)
        self.vertices : "FrozenGraph.__FrozenIsoSet[Vertex]" = FrozenGraph.__FrozenIsoSet(self.vertices)
        self.edges : "FrozenGraph.__FrozenIsoSet[Edge]" = FrozenGraph.__FrozenIsoSet(self.edges)
        
    def append(self, value: Vertex | Edge, explore: bool = False) -> Never:
        raise AttributeError(f"Cannot append to a '{type(self).__name__}'")
    
    def remove(self, value: Vertex | Edge) -> Never:
        raise AttributeError(f"Cannot remove from a '{type(self).__name__}'")
    
    def extend(self, values: Iterable[Vertex | Edge], explore: bool = False) -> Never:
        raise AttributeError(f"Cannot extend a '{type(self).__name__}'")
    
    def paint(self, c: Color) -> Never:
        raise AttributeError(f"Cannot paint to a '{type(self).__name__}'")
    
    def __hash__(self) -> int:
        return hash(hash(self.vertices) -  hash(self.edges))
    
    def __getstate__(self) -> _GraphStateDict:
        res = super().__getstate__()
        res["edges"] = FrozenGraph.__IsoSet(res["edges"])
        res["vertices"] = FrozenGraph.__IsoSet(res["vertices"])
        return res
    
    def __setstate__(self, state: _GraphStateDict):
        super().__setstate__(state)
        self.edges = FrozenGraph.__FrozenIsoSet(self.edges)
        self.vertices = FrozenGraph.__FrozenIsoSet(self.vertices)


    

del RLock, Thread, Any, Callable, Iterable, Iterator, Never, Optional, TypeVar, TypedDict, Union, WeakKeyDictionary, WeakValueDictionary, Color, ColorSetting, SizeSetting, SwitchSetting, WeightSetting, InstanceReferencingClass, IsoSet