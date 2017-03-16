from flask import Flask
from redis import Redis
from datetime import datetime

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    s = 'Hello world! I have been seen {} times.\n'.format(count)

    f = open('log', 'a')
    f.write(str(datetime.now()) + '\n')
    f.close()
    return s

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
