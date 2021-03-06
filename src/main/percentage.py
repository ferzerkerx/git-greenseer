import subprocess
import os

from contribution_stats import ContributionStats
from category_stats import CategoryStats
from dir_stats import DirStats

__author__ = 'fmontes'


class PercentageContributorCalculator:
    current_dir = '.'

    def __init__(self, target_dir):
        self.current_dir = os.getcwd()
        os.chdir(target_dir)
        print('Changed to:', target_dir)

    def __del__(self):
        os.chdir(self.current_dir)
        print('Changed back to:', self.current_dir)

    @staticmethod
    def parse_file_name(line):
        full_file_name = line.strip().decode("unicode_escape", "ignore")
        full_file_name = full_file_name.encode("latin-1", "replace")
        full_file_name = full_file_name.decode("utf-8", "replace")
        return full_file_name

    @staticmethod
    def get_contributors_for_file(file_name):
        print('Getting contributors for file:' + file_name)
        command = "git blame HEAD --line-porcelain " + file_name + " | sed -n 's/^author //p' | sort | uniq -c | sort -rn"
        print(command)
        git_lines_per_committer_for_file = subprocess.Popen(command, shell=True, bufsize=1, stdout=subprocess.PIPE).stdout
        lines = git_lines_per_committer_for_file.readlines()

        lines_in_file = 0
        file_contributors = []
        for i in lines:
            j = PercentageContributorCalculator.parse_file_name(i)

            line_components = j.split()
            line_count = int(line_components[0])
            contributor_name = line_components[1].replace('(', '')

            file_contributors.append(ContributionStats(contributor_name, line_count))

            lines_in_file += line_count

        for contributor in file_contributors:
            contributor.total_lines_to_consider = lines_in_file
        return file_contributors

    @staticmethod
    def calculate_stats_by_category(categories, sorted_dir_list, dir_stat_list):
        dir_category_stats = []
        for category in categories:
            dir_category_stat = CategoryStats(category)
            dir_category_stats.append(dir_category_stat)
            for dir_name in sorted_dir_list:
                dir_stats = dir_stat_list[dir_name]
                if dir_stats.contains_category(category):
                    dir_category_stat.merge_dir_stats(dir_stats)
        return dir_category_stats

    def calculate_contribution_percentage_by_committer_using_categories(self, aliases=None, categories=None, max_files=None, allowed_extensions=None):
        if not aliases:
            aliases = {}
        if not categories:
            categories = []

        print('Calculating percentages...')
        dir_stat_list, sorted_dir_list = self.calculate_percentages_for_git_repository(aliases, max_files, allowed_extensions)

        print('Grouping by category...')
        stats_by_category = self.calculate_stats_by_category(categories, sorted_dir_list, dir_stat_list)
        return stats_by_category

    def calculate_contribution_percentage_by_committer(self, aliases, max_files=None, allowed_extensions=None):
        return self.calculate_percentages_for_git_repository(aliases , max_files, allowed_extensions)

    def should_process_file(self, allowed_extensions, full_file_name):
        file_components = full_file_name.split(".", 1)
        if len(file_components) != 2:
            return False
        extension = file_components[1]
        if extension not in allowed_extensions:
            return False
        return True

    def calculate_percentages_for_git_repository(self, aliases, max_files, allowed_extensions):
        print('Listing files...')
        git_lines_per_committer_for_file = subprocess.Popen("git ls-files master .",
                                                            shell=True, bufsize=1, stdout=subprocess.PIPE).stdout
        lines = git_lines_per_committer_for_file.readlines()
        dir_stat_list = {}
        total_file_count = 0

        for line in lines:
            full_file_name = PercentageContributorCalculator.parse_file_name(line)

            if not self.should_process_file(allowed_extensions, full_file_name):
                continue

            total_file_count += 1
            directory = full_file_name[:full_file_name.rfind("/")]
            contributors = self.get_contributors_for_file(full_file_name)

            dir_stats = dir_stat_list.get(directory)
            if dir_stats is None:
                dir_stats = self.create_dir_stats(aliases, directory)
                dir_stat_list[directory] = dir_stats

            dir_stats.add_file_contributions(full_file_name, contributors)

            if max_files is not None and total_file_count > max_files:
                break
        print('Total Files: ', total_file_count)
        print('Sorting by dir...')
        sorted_dir_list = sorted(dir_stat_list)
        return dir_stat_list, sorted_dir_list

    @staticmethod
    def create_dir_stats(aliases, directory):
        dir_stats = DirStats(directory)
        for category in dir_stats.categories:
            aliased_category = aliases.get(category, None)
            if aliased_category:
                dir_stats.add_category(aliased_category)
        return dir_stats
