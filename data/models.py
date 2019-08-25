"""
https://docs.sqlalchemy.org/en/13/orm/tutorial.html
"""

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

def demo():
    """
    """
    # Create tables
    Base.metadata.create_all(db)

    Session = sessionmaker(bind=db)
    session = Session()

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
    pass

if __name__ == "__main__":
    demo()
