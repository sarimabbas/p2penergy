# extension to help create blueprints
from flask import Blueprint

# create a blueprint for the many routes
bp = Blueprint("admin", __name__, url_prefix="/admin", static_folder="static",
               static_url_path="/admin/static", template_folder="templates")

# import modules containing routes into __init__.py
# the . tells __init__.py to look in the current directory for these modules
from . import routes
