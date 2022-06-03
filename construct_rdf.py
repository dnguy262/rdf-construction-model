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

def construct_RDF(SVO):
    
    g = Graph()

    subjects = SVO[0]
    verbs = SVO[1]
    objects= SVO[2]
    
    row_len = len(subjects)

    ns = 'http://example.org/'

    for i in range(row_len):
        
        subject = subjects[i]
        URI_subject = URIRef(ns + subject.text)
        if subject.entity_type == 'PERSON':
            g.add((URI_subject,RDF.type,SPR.Person))
        elif subject.entity_type == 'NORP':
            g.add((URI_subject,RDF.type,SPR.Group))
        elif subject.entity_type == 'FAC':
            g.add((URI_subject,RDF.type,SPR.Facility))
        elif subject.entity_type == 'ORG':
            g.add((URI_subject,RDF.type,SPR.Organization))
        elif subject.entity_type == 'GPE':
            g.add((URI_subject,RDF.type,SPR.GPE_Location))
        elif subject.entity_type == 'LOC':
            g.add((URI_subject,RDF.type,SPR.Location))
        elif subject.entity_type == 'PRODUCT':
            g.add((URI_subject,RDF.type,SPR.Product))
        elif subject.entity_type == 'EVENT':
            g.add((URI_subject,RDF.type,SPR.Event))
        elif subject.entity_type == 'WORK_OF_ART':
            g.add((URI_subject,RDF.type,SPR.Work_Of_Art))
        elif subject.entity_type == 'LAW':
            g.add((URI_subject,RDF.type,SPR.Law))
        elif subject.entity_type == 'LANGUAGE':
            g.add((URI_subject,RDF.type,SPR.Language))
        elif subject.entity_type == 'DATE':
            g.add((URI_subject,RDF.type,SPR.Date))
        elif subject.entity_type == 'TIME':
            g.add((URI_subject,RDF.type,SPR.Time))
        elif subject.entity_type == 'PERCENT':
            g.add((URI_subject,RDF.type,SPR.Percent))
        elif subject.entity_type == 'MONEY':
            g.add((URI_subject,RDF.type,SPR.Money))
        elif subject.entity_type == 'QUANTITY':
            g.add((URI_subject,RDF.type,SPR.Quantity))
        elif subject.entity_type == 'ORDINAL':
            g.add((URI_subject,RDF.type,SPR.Ordinal))
        elif subject.entity_type == 'CARDINAL':
            g.add((URI_subject,RDF.type,SPR.Cardinal))
        else:
            g.add((URI_subject,RDF.type,SPR.Other))
        
        verb = verbs[i]
        URI_verb = URIRef(ns + verb.text)

        obj = objects[i]
        URI_object = URIRef(ns + obj.text)
        if obj.entity_type == 'PERSON':
            g.add((URI_object,RDF.type,SPR.Person))
        elif obj.entity_type == 'NORP':
            g.add((URI_object,RDF.type,SPR.Group))
        elif obj.entity_type == 'FAC':
            g.add((URI_object,RDF.type,SPR.Facility))
        elif obj.entity_type == 'ORG':
            g.add((URI_object,RDF.type,SPR.Organization))
        elif obj.entity_type == 'GPE':
            g.add((URI_object,RDF.type,SPR.GPE_Location))
        elif obj.entity_type == 'LOC':
            g.add((URI_object,RDF.type,SPR.Location))
        elif obj.entity_type == 'PRODUCT':
            g.add((URI_object,RDF.type,SPR.Product))
        elif obj.entity_type == 'EVENT':
            g.add((URI_object,RDF.type,SPR.Event))
        elif obj.entity_type == 'WORK_OF_ART':
            g.add((URI_object,RDF.type,SPR.Work_Of_Art))
        elif obj.entity_type == 'LAW':
            g.add((URI_object,RDF.type,SPR.Law))
        elif obj.entity_type == 'LANGUAGE':
            g.add((URI_object,RDF.type,SPR.Language))
        elif obj.entity_type == 'DATE':
            g.add((URI_object,RDF.type,SPR.Date))
        elif obj.entity_type == 'TIME':
            g.add((URI_object,RDF.type,SPR.Time))
        elif obj.entity_type == 'PERCENT':
            g.add((URI_object,RDF.type,SPR.Percent))
        elif obj.entity_type == 'MONEY':
            g.add((URI_object,RDF.type,SPR.Money))
        elif obj.entity_type == 'QUANTITY':
            g.add((URI_object,RDF.type,SPR.Quantity))
        elif obj.entity_type == 'ORDINAL':
            g.add((URI_object,RDF.type,SPR.Ordinal))
        elif obj.entity_type == 'CARDINAL':
            g.add((URI_object,RDF.type,SPR.Cardinal))
        else:
            g.add((URI_object,RDF.type,SPR.Other))
        
        g.add((URI_subject,URI_verb,URI_object))
    return g
      
def main():
    path = './data/condensed history.csv'
    SVO = create_SVO_dictionaries(path)
    g = construct_RDF(SVO)
    print(g.serialize(format="turtle"))
    g.serialize(destination="tbl.ttl")


if __name__ == '__main__':
    main()