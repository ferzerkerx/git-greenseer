#!/usr/bin/env python

import sys
import os

print(sys.path)

from setup import *
from percentage import PercentageContributorCalculator
from category_percentage_html_report import render_contribution_percentage_by_committer_using_categories
from category_percentage_html_report import render_categroy_contribution_percentage_by_committer


def main():
    current_path = os.getcwd()
    target_dir = '.'
    if (len(sys.argv) > 1):
        target_dir = sys.argv[1]

    sorted_categories = sorted(group_report_using_categories)
    percentage_contributor_calculator = PercentageContributorCalculator(target_dir)

    group_using_specific_categories = len(group_report_using_categories) > 0

    if group_using_specific_categories:
        stats_by_category = \
            percentage_contributor_calculator.calculate_contribution_percentage_by_committer_using_categories(
                category_aliases, sorted_categories, max_number_of_files, allowed_extensions)
    else:
        dir_stat_list, sorted_dir_list = \
            percentage_contributor_calculator.calculate_contribution_percentage_by_committer(
                category_aliases, max_number_of_files, allowed_extensions)

        all_categories = set()
        for dir_name in sorted_dir_list:
            dir_stats = dir_stat_list[dir_name]
            for category in dir_stats.categories:
                all_categories.add(category)

        stats_by_category = percentage_contributor_calculator.calculate_stats_by_category(list(all_categories),
                                                                                          sorted_dir_list,
                                                                                          dir_stat_list)

    print('Generating Contribution Percentage By Category Report')
    html = render_contribution_percentage_by_committer_using_categories(stats_by_category)
    write_file(current_path, html, 'index.html')

    print('Generating Contributor Percentage By Category Report')
    html = render_categroy_contribution_percentage_by_committer(stats_by_category)
    write_file(current_path, html, 'contributors_stats.html')


def write_file(current_path, html, file_name='output'):
    file_dir = os.path.join(current_path, 'out')
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    html_filename = file_dir + '/' + file_name
    print('Writing html report to file:' + html_filename)
    f = open(html_filename, "w")
    f.write(html)
    f.close()


if __name__ == "__main__":
    main()
