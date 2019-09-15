"""
OPD Crimes high-level config objects
"""

from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

# Create the Flask app
app = Flask(__name__)

# Create the database manager
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../../data/crimes.sqlite"
db = SQLAlchemy(app)

# Create the admin portal manager
admin = Admin(app)

# Import the admin config and views
# These would not be applied if they were not imported somewhere
# But they need to be imported after the config objects have been created
from crimes import admin_config, views
