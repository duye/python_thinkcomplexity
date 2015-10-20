__author__ = 'duye'
  # -*- coding: utf-8 -*-

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

    def get_edge(self, v, w):
        """返回连接v， w， 的边"""
        try:
            return self[v][w]
        except KeyError:
            return None
            #print("no edge between %s and %s" %(v,w))

    def remove_edge(self, e):
        """删除连接v, w, 的边"""
        v,w = e
        try:
            del self[v][w]
            del self[w][v]
        except KeyError:
            """边不存在，不做任何操作"""
            pass

    def vertices(self):
        """返回图中顶点列表"""
        vs = []
        for v in self:
            vs.append(v)
        return vs

    def edges(self):
        """返回所有边的列表"""
        es = []
        for v,ve in self.items():
            for w in ve:
                if self[v][w] not in es:
                    es.append(self[v][w])
        return es

    def out_vertices(self, v):
        """返回v 的临近顶点的列表"""
        vs = []
        for w in self[v]:
            vs.append(w)
        return vs

    def out_edges(self, v):
        """返回v 的相邻边的列表"""
        es = []
        for w in self[v]:
            es.append(self[v][w])
        return es

    def add_all_edges(self):
        """从一个无边的图，添加所有边，成为完全图"""
        for v in self:
            for w in self:
                e = Edge(v,w)
                self[v][w] = e
        for v in self:
            for w in self:
                self[w][v] = self[v][w]
        for v in self:
            del self[v][v]

def main(script, *args):
    a = Vertex('a')
    b = Vertex('b')
    n = Vertex('n')
    p = Vertex('p')
    g = Graph([a,b,n,p], [])
    print(g)
    g.add_all_edges()
    print(g)
    e = Edge(p,a)
    g.remove_edge(e)
    e = Edge(b,p)
    g.remove_edge(e)
    print(g)
    print(g.get_edge(a,b),g.get_edge(a,p))
    print(g.vertices())
    print(g.edges())
    print(g.out_vertices(n))
    print(g.out_edges(n))

if __name__ == "__main__":
    import  sys
    main(*sys.argv)


