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

            existing_stat.contributed_lines = existing_stat.contributed_lines + contribution.lines_contributed
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
