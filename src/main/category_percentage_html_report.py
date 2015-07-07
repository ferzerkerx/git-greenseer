__author__ = 'ferzerkerx'

import os

from jinja2 import Template


def render_contribution_percentage_by_committer_using_categories(stats_by_category):
    html = ''
    t = get_template('category_percentage.html')
    for category_stats in stats_by_category:
        directory_percentages_template = get_template('directory_percentages.html')
        context_data = {'category_stats': category_stats,
                        'directory_percentages_template': directory_percentages_template}
        html += t.render(context_data)
    return html


def get_template(template_name=None):
    template_path = get_templates_path()
    f = open(template_path + '/' + template_name, 'r')
    return Template(f.read())


def get_templates_path():
    path_project = os.path.realpath(os.path.dirname(__file__))
    template_path = os.path.join(path_project, '..', 'templates')
    return template_path
