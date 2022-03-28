
from crypt import methods
from uuid import uuid4
from flask import Flask, request, render_template, make_response, redirect
import requests
from datetime import datetime
import os
import logging
import json

app = Flask(__name__)

BACKEND_LOCATION = os.environ['BACKEND_LOCATION'] if 'BACKEND_LOCATION' in os.environ else 'http://localhost:5000'

@app.route('/')
@app.route('/index')
def index():
    user_id = request.cookies.get('user_id') if 'user_id' in request.cookies else uuid4()

    try:
        back_end_resp = requests.get('{}/api/users/{}/tasks'.format(BACKEND_LOCATION, user_id), )
        view_args = { 'tasks': back_end_resp.json(), 'error': False } if back_end_resp.ok else { 'tasks': [], 'error': True}
    except:
        logging.error('Unable to reach back end services')
        view_args = { 'tasks': [], 'error': True}
    
    resp = make_response(render_template('index.html', **view_args, hostname=os.uname()[1], timestamp=str(datetime.now())))
    resp.set_cookie('user_id', str(user_id), max_age=3600*7)

    return resp

@app.route('/create-task', methods=['POST'])
def create_task():
    user_id = request.cookies.get('user_id')
    description = request.form['description']

    back_end_resp = requests.post('{}/api/users/{}/tasks'.format(BACKEND_LOCATION, user_id), json={'description': description})
    if not back_end_resp.ok:
        logging.error('Unable to communicate with back end service')

    return redirect('/')

@app.route('/complete-task', methods=['POST'])
def complete_task():
    user_id = request.cookies.get('user_id')
    for task_id in request.form:
        requests.delete('{}/api/users/{}/tasks/{}'.format(BACKEND_LOCATION, user_id, task_id))

    return redirect('/')