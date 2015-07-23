__author__ = 'ferzerkerx'

import os
import collections

from jinja2 import FileSystemLoader
from jinja2.environment import Environment

from contributor_stats import ContributorStatsByCategory



path_project = os.path.realpath(os.path.dirname(__file__))
template_path = os.path.join(path_project, '..', 'templates')
env = Environment()
env.loader = FileSystemLoader(template_path)

def render_contribution_percentage_by_committer_using_categories(stats_by_category):
    layout_template = get_template('category_percentages_layout.html')
    category_percentage_template = get_template('category_percentage.html')
    directory_percentages_template = get_template('directory_percentages.html')

    categories_html = ''
    navigation_links = collections.OrderedDict()
    for category_stats in stats_by_category:
        navigation_links[category_stats.name] = '#' + category_stats.name
        context_data = {'category_stats': category_stats,
                        'directory_percentages_template': directory_percentages_template}
        categories_html += category_percentage_template.render(context_data)
    return layout_template.render({'title': 'Category',
                                   'categories_content': categories_html,
                                   'navigation_links': navigation_links})


def render_categroy_contribution_percentage_by_committer(stats_by_category):

    layout_template = get_template('contributor_percentages_layout.html')
    contributor_stats_by_category = collections.OrderedDict()
    navigation_links = collections.OrderedDict()

    for category_stats in stats_by_category:
        for name, contribution in category_stats.sorted_contributions_by_name:
            contributor_stat = contributor_stats_by_category.get(name)
            if contributor_stat is None:
                navigation_links[name] = '#' + name
                contributor_stat = ContributorStatsByCategory(name)
                contributor_stats_by_category[name] = contributor_stat
            contributor_stat.add_contribution(category_stats.name, contribution.average(category_stats.total_dir_lines))

    return layout_template.render({'contributor_stats_by_category': contributor_stats_by_category,
                                   'navigation_links': navigation_links})


def get_template(template_name=None):
    return env.get_template(template_name)
    # template_path = get_templates_path()
    # f = open(template_path + '/' + template_name, 'r')
    # return Template(f.read())

