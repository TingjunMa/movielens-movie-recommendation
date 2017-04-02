import logging
from flask import Flask, request
import rate_limit

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

application = Flask(__name__)

@application.after_request
def inject_x_rate_headers(response):
    limit = rate_limit.get_view_rate_limit()
    if limit and limit.send_x_headers:
        h = response.headers
        h.add('X-RateLimit-Remaining', str(limit.remaining))
        h.add('X-RateLimit-Limit', str(limit.limit))
        h.add('X-RateLimit-Reset', str(limit.reset))
    return response

@application.route('/rate-limited')
@rate_limit.ratelimit(limit=10, per=60 * 1)
def test():
    return "this is rate limit test"


@application.route('/')
def index():
    return "hello world!"

@application.route('/rate')
def rate():
    return "test"

if __name__ == '__main__':
	application.debug = True
	application.run()