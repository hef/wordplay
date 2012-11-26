
class worddb(object):
    """ A directed graph of words """
    def __init__(self):
        self._db = {}
    def add(self, text):
        if text not in self._db:
            self._db[text] = word(self, text)
    def __getitem__(self, key):
        return self._db[key]

class word(object):
    """ A word object contains the string and a frequency of neigboring words """
    def __init__(self, worddb, text):
        self._worddb = worddb
        self._text = text
        self._edges = {}
    def add_edge(self, text):
        """ indicate that the text follows this one """
        if text in self._edges:
            self._edges[text].count += 1
        else:
            self._edges[text] = edge(self, self._worddb[text])
    def __hash__(self):
        return self._text.__hash__()
    def __eq__(self, other):
        return self._text == other._text
    def __unicode__(self):
        return self._text
    def __repr__(self):     # must be unambiguous
        return (repr(unicode(self)))

class edge(object):
    """ Conects a word to a word in a directed manner. """
    def __init__(self, source, target):
        self.source = source 
        self.target = target
        self.count = 1
    def __hash__(self):
        return hash(target)
    def __eq__(self, other):
        return target == target
    def __repr__(self):
        return "%(source)s -> %(target)s [count = %(count)d]"%vars(self)
