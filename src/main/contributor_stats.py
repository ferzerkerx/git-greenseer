__author__ = 'fmontes'


class ContributorStatsByCategory:

    def __init__(self, contributor_name):
        self.contributor_name = contributor_name
        self.contribution_by_category = {}

    def add_contribution(self, category, contribution_percentage):
        self.contribution_by_category[category] = contribution_percentage