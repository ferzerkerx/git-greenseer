__author__ = 'fmontes'

import unittest

from main.dir_stats import DirStats
from main.contribution_stats import ContributionStats

class DirStatsTest(unittest.TestCase):

    def test_add_file_contributions(self):
        dir_name = '/someDir'
        dir_stats = DirStats(dir_name)
        dir_stats.add_file_contributions('some_file1', self.create_file_contributions())
        dir_stats.add_file_contributions('some_file2', self.create_file_contributions())
        dir_stats.add_file_contributions('some_file3', self.create_file_contributions())
        dir_stats.add_file_contributions('some_file4', self.create_file_contributions())
        
        self.assertEqual(len(dir_stats.sorted_contributions), 3)
        firstContribution = dir_stats.sorted_contributions[0]
        name = firstContribution[0]
        contributions = firstContribution[1]
        self.assertEqual(name, 'foo_name3')
        self.assertAlmostEqual(contributions.average(1000), 40, 3)


    def create_file_contributions(self):
        contributor_name1 = 'foo_name1'
        contributor_name2 = 'foo_name2'
        contributor_name3 = 'foo_name3'
        file_contributions = [self.create_contribution(contributor_name1),
                               self.create_contribution(contributor_name2),
                               self.create_contribution(contributor_name3)]
        return file_contributions

    def create_contribution(self, contributor_name, line_count=100, total_lines_to_consider=1050.0):
        contributor_stats = ContributionStats(contributor_name, line_count)
        contributor_stats.total_lines_to_consider = total_lines_to_consider
        return contributor_stats


if __name__ == '__main__':
    unittest.main()
