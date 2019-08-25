from sqlalchemy import create_engine, Column, String, Float, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('sqlite:///:crimes:', echo=True)
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
