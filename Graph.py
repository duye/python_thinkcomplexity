__author__ = 'duye'


class Vertex(object):
    """����㣬�̳���object"""
    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        return 'Vertex (%s)' % repr(self.label)
    __str__ = __repr__


class Edge(tuple):
    """����ߣ��̳���tuple"""
    def __new__(cls, *vs):
        """�̳���tuple������__init__,��__new__"""
        if len(vs) != 2:
            raise(ValueError, 'Edges must connect exactly two vertices.')
        return tuple.__new__(cls, vs)

    def __repr__(self):
        return 'Edge (%s, %s) ' % (repr(self[0]), repr(self[1]))
    __str__ = __repr__


class Graph(dict):
    def __init__(self, vs=[], es=[]):
        """�����µ�graph��vs �Ƕ��㼯��es �Ǳ߼�"""
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """��v ��ӵ�graph��"""
        self[v] = {}

    def add_edge(self, e):
        """��e ��ӵ�graph��,����Ѿ����ڣ�����"""
        v, w = e
        self[v][w] = e
        self[w][v] = e



