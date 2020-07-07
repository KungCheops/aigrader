import os
import glob
import unittest
import shutil


from aigrader import aigrader
from aigrader import assignment_helper
from aigrader import human_in_the_loop
from aigrader import visualizer


dirname, _ = os.path.split(os.path.abspath(__file__))
test_data_dir = os.path.join(dirname, 'data')
test_submissions = glob.glob(os.path.join(test_data_dir, 'source-*.py'))
test_scaffold = os.path.join(test_data_dir, 'scaffold.py')
test_output = os.path.join(test_data_dir, 'output')
shutil.rmtree(test_output, ignore_errors=True)


class TestBasic(unittest.TestCase):

    def testBasic(self):
        assert 1+1 == 2


class TestEditDistance(unittest.TestCase):

    def testEditDistance(self):
        assignment = assignment_helper.calculate_edit_distance(test_submissions,test_scaffold, test_output)
        assert len(assignment.submissions) == 3
        assert assignment.comparison_table is not None
