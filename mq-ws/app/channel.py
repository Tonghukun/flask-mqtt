class Channel:
	def __init__(self):
		self.dict = {}
		
	def serialize(self, topic, payload, qos, time):
		split_topic = topic.split('/')
		self.dict['topic'] = topic
		self.dict['node_name'] = split_topic[1]
		self.dict['sensor_name'] = split_topic[2]
		if self.dict['sensor_name'] == 'dht22':
			split_th = payload.split('+')
			self.dict['temp'] = split_th[0]
			self.dict['hum'] = split_th[1]
			self.dict['payload'] = self.dict['temp'] + '℃ '+ '/ ' + self.dict['hum'] + '%'
		else:
			self.dict['payload'] = payload
		self.dict['qos'] = qos
		self.dict['time'] = time