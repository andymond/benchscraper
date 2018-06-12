import unittest
import os

def create_suite():
    suite = unittest.TestSuite()
    for file in os.listdir("./test"):
        if file.endswith("_test.py"):
            print("running " + file)
            name = file[0:-3]
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(name))
    return suite

suite = create_suite()
unittest.TextTestRunner().run(suite)
