#!/usr/bin/env python
from words import word
from pprint import pprint
import codecs

f = codecs.open('pg2591.txt', 'r', "utf-8")
db = word.worddb()
lastword = None
for line in f.readlines():
    for word in line.split():
        db.add(word)
        if lastword is not None:
            db[lastword].add_edge(word)
        lastword = word

for word in db._db:
    print db[word]
    for edge in db[word]._edges:
        print "   " + repr(db[word]._edges[edge])
