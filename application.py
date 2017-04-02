import json
import logging
from flask import Flask, request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


application = Flask(__name__)

@application.route('/rate')
def index():
    return "test"

if __name__ == '__main__':
	application.debug = True
	application.run()