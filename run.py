from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/time')

def get_current_time():
    local_tz = pytz.timezone('America/New_York')
    current_time = datetime.now(local_tz).strftime("%Y-%m-%d %H:%M:%S")
    return {'time':current_time}

# def hello_world():
#     return 'Hello world!'


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
