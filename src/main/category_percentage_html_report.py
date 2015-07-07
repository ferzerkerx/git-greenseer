__author__ = 'ferzerkerx'

import os

import django
from django.conf import settings
from django.template import loader, Context

settings.configure()
django.setup()
DEBUG = True

def render_contribution_percentage_by_committer_using_categories(stats_by_category):
    html = ''
    t = get_template('category_percentage.html')
    for category_stats in stats_by_category:
        context_data = {}
        context_data['category_name'] = category_stats.name
        context_data['category_dir_stats'] = category_stats.dir_stats
        context_data['directory_percentages_template'] = get_template('directory_percentages.html')

        c = Context(context_data)
        html += t.render(c)

    return html


def get_dir_stats(dir_stat):
    result_str = ''
    for name, contribution in dir_stat.sorted_contributions:
        result_str += '%(contributor_name)s has %(percent)g %% \n' % {"contributor_name": name, "percent": contribution.average(dir_stat.total_dir_lines)}
    return result_str


def get_template(template_name=None):
    template_path = get_templates_path()
    t = loader.get_template(template_name, [template_path])
    return t


def get_templates_path():
    path_project = os.path.realpath(os.path.dirname(__file__))
    template_path = os.path.join(path_project, '..', 'templates')
    return template_path

