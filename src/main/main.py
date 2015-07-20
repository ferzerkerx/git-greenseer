#!/usr/bin/env python

import sys
import os

print sys.path

from percentage import PercentageContributorCalculator
from category_percentage_html_report import render_contribution_percentage_by_committer_using_categories
from category_percentage_text_report import print_contribution_percentage_by_committer_using_categories
from category_percentage_text_report import print_contribution_percentage_by_committer


def main():
    current_path = os.getcwd()
    target_dir = '.'
    if (len(sys.argv) > 1):
        target_dir = sys.argv[1]

    # TODO Fer read this from sdin
    max = None

    aliases = {
        'adt': 'encore',
        'adtcore': 'encore',
        'adtcommon': 'encore',
        'adm': 'admin',
        'amadeus': 'gds',
        'sabre': 'gds',
        'compress': 'asset packaging',
        'asset_packaging': 'asset packaging',
        'webcf': 'ots',
        'implementationresolver': 'stub framework'

    }

    # TODO Fer read this from sdin
    categories = [
        # 'search',
        # 'room',
        # 'activity',
        # 'air',
        # 'discount',
        # 'insurance',
        # 'car',
        # 'merchandise',
        # 'loyalty',
        # 'api',
        # 'connector',
        # 'multi',
        # 'internal',
        # 'feedprocessor',
        # 'enrichment',
        # 'payment',
        # 'points',
        # 'model',
        # 'remoteservice',
        # 'repository',
        # 'tasks',
        # 'report',
        # 'encore',
        # 'ezmodify',
        # 'automation',
        # 'stub',
        # 'service',
        # 'shopping',
        # 'mobile',
        # 'handlebars',
        # 'interceptors',
        # 'freemarker',
        # 'adm',
        # 'marketing',
        # 'gds',
        # 'validation',
        # 'tracking',
        # 'asset packaging',
        # 'ots'
        # 'stub framework',
        'ferzerkerx',
        'web'
    ]
    percentage_contributor_calculator = PercentageContributorCalculator(target_dir)
    #TODO Add reporting type

    should_print_by_category = len(categories) > 0
    if should_print_by_category:
        stats_by_category = percentage_contributor_calculator.calculate_contribution_percentage_by_committer_using_categories(
            aliases, categories, max)
        html = render_contribution_percentage_by_committer_using_categories(stats_by_category)

        file_dir = os.path.join(current_path, 'out')
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        f = open(file_dir + '/index.html', "w")
        f.write(html)
        f.close()
    else:
        dir_stat_list, sorted_dir_list = percentage_contributor_calculator.calculate_contribution_percentage_by_committer(max)
        print_contribution_percentage_by_committer(sorted_dir_list, dir_stat_list)



if __name__ == "__main__":
    main()
