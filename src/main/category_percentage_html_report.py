__author__ = 'ferzerkerx'

import os

import django
from django.conf import settings
from django.template import loader, Context

settings.configure()
django.setup()

def render_category_html_string(categories_stats):
    path_project = os.path.realpath(os.path.dirname(__file__))
    template_path = os.path.join(path_project,  '..', 'templates')
    t = loader.get_template('category_percentage.html', [template_path])
    c = Context({ 'category_name': 'test' })
    html = t.render(c)
    return html

