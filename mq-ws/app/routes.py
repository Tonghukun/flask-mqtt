from flask import render_template, jsonify
from app import app, mqtt, socketio, bootstrap, db
from datetime import datetime
from app.channel import Channel
from app.models import Dht_22, MQ7
import json, time

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/index_test')
def index_test():
    return render_template('index_test.html')

@app.route('/history/<node_name>/<sensor_name>')
def history(node_name, sensor_name):
    if sensor_name == 'DHT22':
        json_list = [i.serialize for i in Dht_22.query.filter_by(node=node_name).order_by(db.desc(Dht_22.timestamp))]
    elif sensor_name == 'MQ7':
        json_list = [i.serialize for i in MQ7.query.filter_by(node=node_name).order_by(db.desc(MQ7.timestamp))]
    return render_template('history.html', json_list = json_list, sensor_name=sensor_name)

@socketio.on('publish')
def handle_publish(json_str):
    data = json.loads(json_str)
    mqtt.publish(data['topic'], data['message'], data['qos'])


@socketio.on('subscribe')
def handle_subscribe(json_str):
    data = json.loads(json_str)
    mqtt.subscribe(data['topic'], data['qos'])


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    c = Channel()
    c.serialize(message.topic, message.payload.decode(), message.qos, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    data = c.dict
    if data['sensor_name'] == 'dht22':
        sign = Dht_22(node=data['node_name'], temp=data['temp'], hum=data['hum'])
    elif data['sensor_name'] == 'mq7':
        sign = MQ7(node=data['node_name'], air=data['payload'])
    db.session.add(sign)
    db.session.commit()
    socketio.emit('mqtt_message', data=data)

@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    # print(level, buf)
    pass
