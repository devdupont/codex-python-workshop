"""
Registers db models with the admin portal
"""

from flask_admin.contrib.sqla import ModelView
from crimes import admin, db
from crimes.models import Crime

# Registers a model view for our Crime model/table
# DB session is required to commit changes
admin.add_view(ModelView(Crime, db.session))
