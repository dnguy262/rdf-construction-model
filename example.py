from rdflib import Graph, Namespace, URIRef, BNode, Literal
from rdflib.namespace import RDF, FOAF, XSD, SDO, SPR
from rdflib.namespace import Namespace

g = Graph()

swanton_persons = Namespace("http://example.org/")

al_smith = URIRef("http://example.org/Al_Smith") #use namespace + String concatenation

was_born = URIRef("http://example.org/was_born")

g.add((al_smith, RDF.type, SPR.Person))
g.add((al_smith, was_born, Literal("1921", datatype=XSD.integer)))
print(g.serialize(format="turtle"))

