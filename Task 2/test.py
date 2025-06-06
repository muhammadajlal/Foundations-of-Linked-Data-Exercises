from rdflib import Graph

# Load the graph
g = Graph()
g.parse("fld.ttl", format="ttl")

# Optional: print all triples
# for s, p, o in g:
#     print(s, p, o)

# Run a SPARQL query to count all triples
q = """

BASE <https://paul.ti.rw.fau.de/~uq25ywiq/fld.ttl>

ASK {
  ?team <#name> "Borussia Dortmund"@de .
}


"""


results = g.query(q)

# This part prints the result:
for row in results:
    print(row)
