__author__ = 'fmontes'


class ContributionStats:

    def __init__(self, contributor_name, line_count):
        self.contributor_name = contributor_name
        self.contributed_lines = line_count

    def average(self, total_lines_to_consider=0):
        return float(self.contributed_lines) / float(total_lines_to_consider) * 100
