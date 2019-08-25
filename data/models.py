"""
https://docs.sqlalchemy.org/en/13/orm/tutorial.html
"""

import csv
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, String, Float, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('sqlite:///crimes.sqlite', echo=True)
Base = declarative_base()

class Crime(Base):
    """
    Crime db table
    """
    __tablename__ = 'crimes'

    id = Column(Integer, primary_key=True)
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

    def __repr__(self):
        return f"Crime occured at {self.timestamp}"

def get_session():
    Session = sessionmaker(bind=db)
    return Session()

def demo():
    """
    """
    # Create tables
    Base.metadata.create_all(db)

    session = get_session()

    c = Crime(
        id=1,
        number="12345",
        timestamp=datetime.utcnow(),
        address="1",
        latitude=10.1,
        longitude=-11
    )
    print(c)

    session.add(c)
    session.commit()

def populate_from_csv(filename: str):
    """
    """
    # Create tables
    Base.metadata.create_all(db)

    session = get_session()

    with open(filename) as fin:
        crimedata = csv.reader(fin)
        cols = next(crimedata)
        cols[0] = 'id'
        for crime in crimedata:
            crime[0] = int(crime[0])
            crime[-1] = float(crime[-1])
            crime[-2] = float(crime[-2])
            crime[2] = datetime.strptime(crime[2], "%Y-%m-%d %H:%M:%S")
            crime = dict(zip(cols, crime))
            c = Crime(**crime)
            session.add(c)
    session.commit()


if __name__ == "__main__":
    populate_from_csv("clean_opd.csv")
