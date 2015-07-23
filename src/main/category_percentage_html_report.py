__author__ = 'ferzerkerx'

import os
import collections

from contributor_stats import ContributorStatsByCategory
from jinja2 import Template


def render_contribution_percentage_by_committer_using_categories(stats_by_category):
    layout_template = get_template('layout.html')
    category_percentage_template = get_template('category_percentage.html')
    directory_percentages_template = get_template('directory_percentages.html')

    category_html = ''
    navigation_links = collections.OrderedDict()
    for category_stats in stats_by_category:
        navigation_links[category_stats.name] = '#' + category_stats.name
        context_data = {'category_stats': category_stats,
                        'directory_percentages_template': directory_percentages_template}
        category_html += category_percentage_template.render(context_data)
    return layout_template.render({'content': category_html, 'navigation_links': navigation_links})

def render_categroy_contribution_percentage_by_committer(stats_by_category):
    contributor_stats_by_category = {}

    contributor_percentages_template = get_template('contributor_percentages.html')
    for category_stats in stats_by_category:
        for name,contribution in category_stats.sorted_contributions:
            if



def get_template(template_name=None):
    template_path = get_templates_path()
    f = open(template_path + '/' + template_name, 'r')
    return Template(f.read())


def get_templates_path():
    path_project = os.path.realpath(os.path.dirname(__file__))
    template_path = os.path.join(path_project, '..', 'templates')
    return template_path
