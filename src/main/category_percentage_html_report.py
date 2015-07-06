__author__ = 'ferzerkerx'

import os

import django
from django.conf import settings
from django.template import loader, Context

settings.configure()
django.setup()

def render_contribution_percentage_by_committer_using_categories(stats_by_category):
    html = ''
    t = get_template('category_percentage.html')
    for category_stats in stats_by_category:
        context_data = {}
        context_data['category_name'] = category_stats.name
        #TODO Fer implement
        # print get_dir_stats(category_stats)
        # for dir_stats in category_stats.dir_stats:
        #     print '\n' + '########' + dir_stats.dir_name + '\n' + get_dir_stats(dir_stats)
        c = Context(context_data)
        html += t.render(c)

    return html

def get_template(template_name=None):
    path_project = os.path.realpath(os.path.dirname(__file__))
    template_path = os.path.join(path_project, '..', 'templates')
    t = loader.get_template(template_name, [template_path])
    return t

