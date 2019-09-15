"""
OPD Crime database models

Adapted from /data/models.py
"""

from crimes import db

# pylint: disable=no-member


class Crime(db.Model):
    """
    Crime database model/table
    """

    __tablename__ = "crimes"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String, unique=True)
    timestamp = db.Column(db.DateTime)
    address = db.Column(db.String)
    offense_location_type = db.Column(db.String)
    offense_category = db.Column(db.String)
    offense_type = db.Column(db.String)
    offense_charge_type = db.Column(db.String)
    disposition = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __repr__(self) -> str:
        return f"Crime occured at {self.timestamp}"

    @property
    def serialized(self) -> dict:
        """
        Returns a JSON-serializable representation of the Crime object
        """
        return {
            "id": self.id,
            "number": self.number,
            "timestamp": self.timestamp.iso_format(),
            "address": self.address,
            "offense_location_type": self.offense_location_type,
            "offense_category": self.offense_category,
            "offense_type": self.offense_type,
            "offense_charge_type": self.offense_charge_type,
            "disposition": self.disposition,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }
