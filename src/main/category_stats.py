from dir_stats import DirStats

__author__ = 'fmontes'


class CategoryStats(DirStats):
    def __init__(self, name):
        DirStats.__init__(self)
        self.name = name
        self.dir_stats = []

    def merge_dir_stats(self, other_dir_stats):
        self.dir_stats.append(other_dir_stats)
        for file_name in other_dir_stats.contribution_list_per_file:
            self.add_file_contributions(file_name, other_dir_stats.contribution_list_per_file[file_name])
