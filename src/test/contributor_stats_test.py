# The MIT License (MIT)
#
# Copyright (c) 2015 Fernando Montes
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
__author__ = 'fmontes'

import unittest

from main.contributor_stats import ContributorStats

class ContributorStatsTest(unittest.TestCase):

    def test_average(self):
        contributor_name = 'foo_name'
        line_count = 100.0
        contributor_stats = ContributorStats(contributor_name, line_count)
        contributor_stats.total_lines_to_consider = 1050.0
        average = contributor_stats.average()
        self.assertAlmostEqual(average, 9.523809523809524, 3)

if __name__ == '__main__':
    unittest.main()
