#!/usr/bin/env python

import sys

print sys.path

from percentage import PercentageContributorCalculator

def main():
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
        'search',
        'room',
        'activity',
        'air',
        'discount',
        'insurance',
        'car',
        'merchandise',
        'loyalty',
        'api',
        'connector',
        'multi',
        'internal',
        'feedprocessor',
        'enrichment',
        'payment',
        'points',
        'model',
        'remoteservice',
        'repository',
        'tasks',
        'report',
        'encore',
        'ezmodify',
        'automation',
        'stub',
        'service',
        'shopping',
        'mobile',
        'handlebars',
        'interceptors',
        'freemarker',
        'adm',
        'marketing',
        'gds',
        'validation',
        'tracking',
        'asset packaging',
        'ots'
        'stub framework'
    ]
    percentage_contributor_calculator = PercentageContributorCalculator(target_dir)
    percentage_contributor_calculator.print_contribution_percentage_by_commiter(aliases, categories, max)


if __name__ == "__main__":
    main()