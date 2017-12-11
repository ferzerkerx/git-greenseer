__author__ = 'fmontes'

import unittest

from main.contribution_stats import ContributionStats

class ContributorStatsTest(unittest.TestCase):

    def test_average(self):
        contributor_name = 'foo_name'
        line_count = 100.0
        contributor_stats = ContributionStats(contributor_name, line_count)
        
        total_lines_to_consider = 1050.0
        average = contributor_stats.average(total_lines_to_consider)
        self.assertAlmostEqual(average, 9.523809523809524, 3)

if __name__ == '__main__':
    unittest.main()
