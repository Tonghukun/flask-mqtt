from app import db
from datetime import datetime

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%d %H:%M:%S")

#class RFID(db.Model):
#	id = db.Column(db.Integer, primary_key=True)
#	node = db.Column(db.String(10))
#	card = db.Column(db.String(24))
#	timestamp = db.Column(db.DateTime, default=datetime.now)
#	
#	@property
#	def serialize(self):
#		"""Return object data in easily serializable format"""
#		return {
#			'node' : self.node,
#			'card' : self.card,
#			'timestamp': dump_datetime(self.timestamp)
#        }
		
class Dht_22(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	node = db.Column(db.String(10))
	temp = db.Column(db.String(7))
	hum = db.Column(db.String(7))
	timestamp = db.Column(db.DateTime, default=datetime.now)
	
	@property
	def serialize(self):
		return {
			'node': self.node,
			'temp': self.temp,
			'hum': self.hum,
			'timestamp': dump_datetime(self.timestamp)
		}

class MQ7(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	node = db.Column(db.String(10))
	air = db.Column(db.String(6))
	timestamp = db.Column(db.DateTime, default=datetime.now)

	@property
	def serialize(self):
		return {
			'node': self.node,
			'air': self.air,
			'timestamp': dump_datetime(self.timestamp)
		}