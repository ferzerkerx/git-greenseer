from contributor_stats import ContributorStats

__author__ = 'fmontes'


class DirStats:
    def __init__(self, dir_name=''):
        self.dir_name = dir_name
        self.categories = dir_name.split("/")
        self.contribution_list_per_file = {}
        self.contributors_stats = {}
        self.total_dir_lines = 0

    def contains_category(self, category):
        return category in self.categories

    def add_file_contributions(self, file_name, contributions):
        self.contribution_list_per_file[file_name] = contributions
        for contribution in contributions:
            existing_stat = self.contributors_stats.get(contribution.contributor_name)
            if existing_stat is None:
                existing_stat = ContributorStats(contribution.contributor_name, 0)
                self.contributors_stats[contribution.contributor_name] = existing_stat

            # print 'To dir', self.dir_name, ' adding contributions for file: ', file_name, ' lines:',contribution.contributed_lines, ' from:', contribution.contributor_name, ' existing_stat.contributed_lines: ', existing_stat.contributed_lines
            existing_stat.contributed_lines = existing_stat.contributed_lines + contribution.contributed_lines

            # print self.total_dir_lines

            self.total_dir_lines = self.total_dir_lines + contribution.contributed_lines
            # print 'To dir', self.dir_name, ' adding contributions for file: ', file_name, ' lines:',contribution.contributed_lines, ' from:', contribution.contributor_name
            # print self.total_dir_lines

    def merge_dir_stats(self, other_dir_stats):
        for file_name in other_dir_stats.contribution_list_per_file:
            self.add_file_contributions(file_name, other_dir_stats.contribution_list_per_file[file_name])

    def add_category(self, aliased_category):
        self.categories.append(aliased_category)
