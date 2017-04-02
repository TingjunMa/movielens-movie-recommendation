import json
import logging
from flask import Flask, request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = Flask(__name__)

@app.route('/rate')
def index():
    return "test"

if __name__ == '__main__':
	app.debug = True
	app.run()