__author__ = 'duye'


class Vertex(object):
    """定义点，继承自object"""
    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        return 'Vertex (%s)' % repr(self.label)
    __str__ = __repr__


class Edge(tuple):
    """定义边，继承自tuple"""
    def __new__(cls, *vs):
        """继承自tuple，不用__init__,用__new__"""
        if len(vs) != 2:
            raise(ValueError, 'Edges must connect exactly two vertices.')
        return tuple.__new__(cls, vs)

    def __repr__(self):
        return 'Edge (%s, %s) ' % (repr(self[0]), repr(self[1]))
    __str__ = __repr__


class Graph(dict):
    def __init__(self, vs=[], es=[]):
        """创建新的graph，vs 是顶点集，es 是边集"""
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """把v 添加到graph中"""
        self[v] = {}

    def add_edge(self, e):
        """把e 添加到graph中,如果已经存在，更新"""
        v, w = e
        self[v][w] = e
        self[w][v] = e



