"""
Builds the OPD crimes SQLite database

Documentation + Tutorials

CSV: https://docs.python.org/3.7/library/csv.html
Datetime Format: https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior
SQLAlchemy: https://docs.sqlalchemy.org/en/13/orm/tutorial.html
"""

import csv
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Float, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connect to the database
# SQLite will create a new one for us
db = create_engine('sqlite:///crimes.sqlite', echo=True)

# This is the table base that will manage table creation for us
Base = declarative_base()

class Crime(Base):
    """
    Crime database model/table
    """
    __tablename__ = 'crimes'

    # Tables must have a primary key
    id = Column(Integer, primary_key=True)

    # Column names and types match the data from our clean dataset
    number = Column(String)
    timestamp = Column(DateTime)
    address = Column(String)
    offense_location_type = Column(String)
    offense_category = Column(String)
    offense_type = Column(String)
    offense_charge_type = Column(String)
    disposition = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    def __repr__(self) -> str:
        return f"Crime occured at {self.timestamp}"

def create_tables():
    """
    Uses the declarative base object to create database tables
    """
    Base.metadata.create_all(db)

def get_session() -> "sqlalchemy.orm.session.Session":
    """
    Returns a session connected to our database
    """
    Session = sessionmaker(bind=db)
    return Session()

def demo():
    """
    This demo creates a new database and loads a single crime row into it
    """
    
    create_tables()
    session = get_session()

    # Create a new Crime using keyword arguements
    c = Crime(
        id=1,
        number="12345",
        timestamp=datetime.utcnow(),
        address="1",
        latitude=10.1,
        longitude=-11
    )

    # print will call Crime.__repr__
    print(c)

    # Registers the new Crime object
    session.add(c)

    # Commits all changes to the database
    session.commit()

def populate_from_csv(filename: str):
    """
    Load the database with crime data from a CSV
    """

    create_tables()
    session = get_session()

    # Open the file contents
    with open(filename) as fin:
        # Read in the CSV data
        crimedata = csv.reader(fin)
        # Remove the columns names
        cols = next(crimedata)
        # Set the first column name as id because pandas didn't do that for us
        cols[0] = 'id'

        for crime in crimedata:
            # Cast the id to an int
            crime[0] = int(crime[0])
            # Cast the coordinates to floats
            crime[-1] = float(crime[-1])
            crime[-2] = float(crime[-2])
            # Cast to timestamp to a datetime object
            crime[2] = datetime.strptime(crime[2], "%Y-%m-%d %H:%M:%S")

            # Create a dict where the key is col name and value is the row data
            # zip turns [1,2,3],[3,2,1] into [(1,3),(2,2),(3,1)]
            # Casting to a dict makes these key-value pairs
            crime = dict(zip(cols, crime))

            # Create a new crime where the dict is expanded into keyword args
            c = Crime(**crime)

            # Add the new row to the table
            session.add(c)

    # Commit the changes when done
    # This prevents changes being made if an error arises beforehand
    session.commit()


# Will only run if called directly ie "python models.py"
if __name__ == "__main__":
    populate_from_csv("clean_opd.csv")
