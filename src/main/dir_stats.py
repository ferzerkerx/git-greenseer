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

from contributor_stats import ContributorStats

__author__ = 'fmontes'


class DirStats:
    contribution_list_per_file = {}
    contributors_stats = {}
    dir_name = ''
    total_dir_lines = 0

    def __init__(self, dir_name):
        self.dir_name = dir_name

    def add_file_contributions(self, file_name, contributions):
        self.contribution_list_per_file[file_name] = contributions
        for contribution in contributions:
            existing_stat = self.contributors_stats.get(contribution.contributor_name)
            if existing_stat == None:
                existing_stat = ContributorStats(contribution.contributor_name, 0)
                self.contributors_stats[contribution.contributor_name] = existing_stat

            existing_stat.lines_contributed = existing_stat.lines_contributed + contribution.lines_contributed
            self.total_dir_lines = self.total_dir_lines + contribution.lines_contributed

    def print_dir_stats(self):
        for name in self.contributors_stats:
            contribution = self.contributors_stats[name]
            contribution.total_lines_to_consider = self.total_dir_lines
            print '%(contributor_name)s has %(percent)g %%' % {"contributor_name": name, "percent": contribution.average()}

    def print_stats_for_files_in_dir(self):
        for file_name in self.contribution_list_per_file:
            contributions = self.contribution_list_per_file[file_name]
            print file_name
            for contribution in contributions:
                print '%(contributor_name)s has %(percent)g %%' % {"contributor_name": contribution.contributor_name,
                                                                   "percent": contribution.average()}
