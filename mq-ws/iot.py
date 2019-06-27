from app import app as application 
from app import socketio

if __name__ == '__main__':
    socketio.run(application, host='0.0.0.0', port=5000, use_reloader=True, debug=True)
