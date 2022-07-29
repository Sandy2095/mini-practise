from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint("simple_page",__name__,
                        template_folder='templates')
simple_page  = Blueprint("simple_page", __name__,
                         url_prefix="/pages")

@simple_page.route('/',defaults={'page':'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template(f'pages/{page}.html')
    except TemplateNotFound:
        abort(404)

@simple_page.route('/')
def index():
    return "hello"