__author__ = 'fmontes'


class ContributorStats:

    def __init__(self, contributor_name, line_count):
        self.contributor_name = contributor_name
        self.contributed_lines = line_count
        self.total_lines_to_consider = 0

    def average(self):
        return (float(self.contributed_lines) / float(self.total_lines_to_consider) * 100)
