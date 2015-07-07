__author__ = 'ferzerkerx'


def print_contribution_percentage_by_committer_using_categories(stats_by_category):
    for category_stats in stats_by_category:
        print '*******', category_stats.name
        print get_dir_stats(category_stats)
        for dir_stats in category_stats.dir_stats:
            print '\n' + '########' + dir_stats.dir_name + '\n' + get_dir_stats(dir_stats)

def print_contribution_percentage_by_committer(sorted_dir_list, dir_stat_list):
    for dir_name in sorted_dir_list:
        print '########', dir_name
        dir_stats = dir_stat_list[dir_name]
        print get_dir_stats(dir_stats)
        # print_stats_for_files_in_dir(dir_stats)


def get_dir_stats(dir_stat):
    result_str = ''
    for name, contribution in dir_stat.sorted_contributions:
        result_str += '%(contributor_name)s has %(percent)g %% \n' % {"contributor_name": name, "percent": contribution.average(dir_stat.total_dir_lines)}
    return result_str

def print_stats_for_files_in_dir(dir_stat):
    for file_name in dir_stat.contribution_list_per_file:
        contributions = dir_stat.contribution_list_per_file[file_name]
        print file_name
        total_lines_to_consider = 0 #TODO Fer find a better way to do this
        for contribution in contributions:
            total_lines_to_consider += contribution.contributed_lines

        for contribution in contributions:
            print '%(contributor_name)s has %(percent)g %%' % {"contributor_name": contribution.contributor_name,
                                                               "percent": contribution.average(total_lines_to_consider)}
