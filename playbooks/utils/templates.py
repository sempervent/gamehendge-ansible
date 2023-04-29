"""Manage templates."""
import os
from jinja2 import Environment, FileSystemLoader


def render_template(template_file, context):
    templates_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template(template_file)
    return template.render(context)
