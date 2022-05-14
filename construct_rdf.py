import csv
from re import sub

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

        for i,row in enumerate(reader,1):
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
        
      
def main():
    SVO = create_SVO_dictionaries('condensed history.csv')
    print(len(SVO[1]))

if __name__ == '__main__':
    main()