# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs, locale
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

import os
import re
from datetime import timedelta, datetime
from flask import Flask,  jsonify
from flask_sslify import SSLify
import logging

# add environment variables using 'heroku config:add VARIABLE_NAME=variable_name'
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
TESTING = DEBUG


app = Flask(__name__)
app.config.from_object(__name__) 

# logging
stream_handler = logging.StreamHandler()
app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.INFO)

if app.debug:
	app.logger.setLevel(logging.DEBUG)
	app.logger.info('Running in debug mode')
else:
	app.logger.info('Running in prod mode')
if not app.config['RESOURCE_FILEPATH']:
	app.logger.error('RESOURCE_FILEPATH config var is missing')


# services
sslify = SSLify(app)
@app.route('/')
def root():
	return jsonify(result=success)


if __name__=='__main__':
	port = int(os.environ.get('PORT', 5000))
	host = '0.0.0.0' if os.environ.get('HEROKU') else '127.0.0.1'
	app.logger.info("Starting server at %s:%d" % (host, port))
	app.run(host=host, port=port, debug=app.debug)
	app.logger.info("Server shuting down")
