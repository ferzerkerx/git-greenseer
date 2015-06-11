#!/usr/bin/env python

import sys

print sys.path

from percentage import PercentageContributorCalculator

def main():
    target_dir = '.'
    if (len(sys.argv) > 1):
        target_dir = sys.argv[1]
    percentage_contributor_calculator = PercentageContributorCalculator(target_dir)
    percentage_contributor_calculator.print_contribution_percentage_by_commiter()


if __name__ == "__main__":
    main()