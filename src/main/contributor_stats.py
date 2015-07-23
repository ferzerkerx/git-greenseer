__author__ = 'fmontes'


class ContributorStatsByCategory:

    def __init__(self, contributor_name):
        self.contributor_name = contributor_name
        self.contribution_by_category = {}
        self.percentage_by_category = {}

    def add_contribution(self, category, line_count_contribution, contribution_percentage):
        self.contribution_by_category[category] = line_count_contribution
        self.percentage_by_category[category] = contribution_percentage