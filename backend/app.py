from re import U
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

STATE = dict()

@app.route("/api/users/<userId>/tasks", methods=['GET'])
def get_tasks(userId):
    return jsonify(STATE[userId] if userId in STATE else [])
    
@app.route("/api/users/<userId>/tasks", methods=['POST'])
def save_task(userId):
    task = request.json
    task['id'] = str(uuid.uuid4())
    def get_or_create_user_tasks():
        if userId in STATE:
            return STATE[userId]
        else:
            user_tasks = []
            STATE[userId] = user_tasks
            return user_tasks
    tasks = get_or_create_user_tasks()
    tasks.append(task)
    return get_tasks(userId)

@app.route("/api/users/<userId>/tasks/<taskId>", methods=['DELETE'])
def delete_task(userId, taskId):
    if userId in STATE:
        tasks = STATE[userId]
        for t in tasks:
            if 'id' in t and t['id'] == taskId:
                tasks.remove(t)
                break
    
    return ('', 204)
