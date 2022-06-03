import unittest
from construct_rdf import *

class Test_Create_SVO_Dictionaries(unittest.TestCase):
    def test_01_file1(self):
        SVO = create_SVO_dictionaries('test_files/condensed history.csv')
        self.assertEqual(80,len(SVO[0]))
        self.assertEqual(80,len(SVO[1]))
        self.assertEqual(80,len(SVO[2]))

    def test_02_file1(self):
        SVO = create_SVO_dictionaries('test_files/condensed history.csv')
        subjects = SVO[0]
        verbs = SVO[1]
        objects = SVO[2]
        subject = subjects[0]
        verb = verbs[0]
        obj = objects[0]
        self.assertEqual('fred_swanton', subject.text)
        self.assertEqual('businessman_of', verb.text)
        self.assertEqual('santa_cruz', obj.text)
  
    def test_01_mainfile(self):
        SVO = create_SVO_dictionaries('condensed history.csv')
        self.assertTrue(len(SVO[0]) == len(SVO[1]) == len(SVO[2]))

if __name__ == "__main__":
    unittest.main()