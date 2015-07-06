__author__ = 'ferzerkerx'


def print_contribution_percentage_by_committer_using_categories(stats_by_category):
    for category_stats in stats_by_category:
        print '*******', category_stats.name
        category_stats.print_dir_stats()
        for dir_stats in category_stats.dir_stats:
            print '\n' + '########' + dir_stats.dir_name + '\n' + dir_stats.get_dir_stats()

def print_contribution_percentage_by_committer(sorted_dir_list, dir_stat_list):
    for dir_name in sorted_dir_list:
        print '########', dir_name
        dir_stats = dir_stat_list[dir_name]
        dir_stats.print_dir_stats()
        # dir_stats.print_stats_for_files_in_dir()
