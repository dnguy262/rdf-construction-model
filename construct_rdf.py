import csv
from re import sub
from rdflib import Graph, Namespace, URIRef, BNode, Literal
from rdflib.namespace import RDF, SPR
from rdflib.namespace import Namespace


class Entity:
    def __init__(self, row, entity_type, text):
        self.row = row
        self.entity_type = entity_type
        self.text = text

class Predicate:
    def __init__(self, row, text):
        self.row = row
        self.text = text

def snake_case(s):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
        sub('([A-Z]+)', r' \1',
        s.replace('-', ' '))).split()).lower()

def create_SVO_dictionaries(f):
    with open(f, 'r') as file:
        reader = csv.reader(file)
        #skips header
        next(reader) 

        #(Key: Row Number, Value: Entity/Predicate)

        subjects_dict = {}
        verbs_dict = {}
        objects_dict = {}

        for i,row in enumerate(reader):
            #todo: account for Dates

            #Create objects for Entity 1 and insert into dictionary
            subject = Entity(i,row[0],snake_case(row[1]))
            subjects_dict[subject.row] = subject

            #Create objects for predicates and insert into dictionary
            verb = Predicate(i,snake_case(row[2]))
            verbs_dict[verb.row] = verb

            #Create objects for Entity 2 and insert into dictionary
            obj = Entity(i,row[3],snake_case(row[4]))
            objects_dict[obj.row] = obj

        return [subjects_dict,verbs_dict,objects_dict]

def create_URI(node, namespace):

# def construct_RDF(SVO):

#     g = Graph()

#     subjects = SVO[0]
#     verbs = SVO[1]
#     objects= SVO[2]
    
#     row_len = len(subjects)

#     ns = 'http://example.org/'

#     for i in range(row_len):
#         URI_subject = create_URI(subjects[i],ns)
#         URI_verb = create_URI(verbs[i],ns)
#         URI_obj = create_URI(objects[i],ns)
#         g.add(URI_subject,URI_verb,URI_obj)
      
def main():
    SVO = create_SVO_dictionaries('condensed history.csv')
    # construct_RDF(SVO)


if __name__ == '__main__':
    main()