import subprocess
import os

from contributor_stats import ContributorStats
from dir_stats import DirStats

__author__ = 'fmontes'


class PercentageContributorCalculator:
    current_dir = '.'
    def __init__(self, target_dir):
        self.current_dir = os.getcwd()
        os.chdir(target_dir)
        print 'Changed to:', target_dir

    def __del__(self):
        os.chdir(self.current_dir)
        print 'Changed back to:', self.current_dir

    def get_contributors_for_file(self, file_name):
        git_lines_per_committer_for_file = subprocess.Popen(
            "git blame --line-porcelain " + file_name + " | sed -n 's/^author //p' | sort | uniq -c | sort -rn",
            shell=True, bufsize=1, stdout=subprocess.PIPE).stdout
        lines = git_lines_per_committer_for_file.readlines()

        lines_in_file = 0
        file_contributors = []
        for i in lines:
            j = i.strip().decode("unicode_escape", "ignore")
            j = j.encode("latin-1", "replace")
            j = j.decode("utf-8", "replace")

            line_components = j.split()
            line_count = int(line_components[0])
            contributor_name = line_components[1]

            file_contributors.append(ContributorStats(contributor_name, line_count))

            lines_in_file = lines_in_file + line_count

        for contributor in file_contributors:
            contributor.total_lines_to_consider = lines_in_file
            # print '%(contributor_name)s has %(percent)g %%' %  {"contributor_name": contributor.contributor_name, "percent": (float(contributor.lines_contributed) /  float(lines_in_file)  * 100)}
        # print "Total lines in file:", lines_in_file
        return file_contributors

    def print_contribution_percentage_by_commiter(self):
        git_lines_per_committer_for_file = subprocess.Popen("git ls-files master .",
                                                            shell=True, bufsize=1, stdout=subprocess.PIPE).stdout
        lines = git_lines_per_committer_for_file.readlines()
        dir_stat_list = {}

        # max = 5
        total_file_count = 0

        for line in lines:
            full_file_name = line.strip().decode("unicode_escape", "ignore")
            full_file_name = full_file_name.encode("latin-1", "replace")
            full_file_name = full_file_name.decode("utf-8", "replace")

            file_components = full_file_name.split(".", 1)
            if (len(file_components) != 2):
                # print "Skipping file:" + full_file_name
                continue
            extension = file_components[1]
            if (extension != "java"):
                # print "Skipping file:" + full_file_name
                continue

            total_file_count = total_file_count + 1
            dir = full_file_name[:full_file_name.rfind("/")]
            # print "file:", full_file_name
            contributors = self.get_contributors_for_file(full_file_name)
            # contributors = []

            dir_stats = dir_stat_list.get(dir)
            if (dir_stats == None):
                dir_stats = DirStats(dir)
                dir_stat_list[dir] = dir_stats

            dir_stats.add_file_contributions(full_file_name, contributors)
            # max = max - 1
            # if (max <= 0):
            #     break

        print 'Total Files: ', total_file_count
        for dir_name in sorted(dir_stat_list):
            print '########',dir_name
            dir_stats = dir_stat_list[dir_name]
            dir_stats.print_dir_stats()
            # dir_stats.print_stats_for_files_in_dir()
