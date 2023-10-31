from flask import Flask, request, jsonify
from src.email_manager import fetch_unread_emails
from src.draft_manager import save_drafts
from src.account_manager import manage_accounts
from src.meeting_scheduler import schedule_meeting
from src.response_generator import generate_responses

app = Flask(__name__)

@app.route('/emails/unread', methods=['GET'])
def fetch_unread_emails_route():
    return jsonify(fetch_unread_emails())

@app.route('/drafts', methods=['POST'])
def save_drafts_route():
    data = request.get_json(force=True)
    return jsonify(save_drafts(data))

@app.route('/accounts', methods=['POST'])
def manage_accounts_route():
    data = request.get_json(force=True)
    return jsonify(manage_accounts(data))

@app.route('/meetings/schedule', methods=['POST'])
def schedule_meeting_route():
    data = request.get_json(force=True)
    return jsonify(schedule_meeting(data))

@app.route('/responses/generate', methods=['POST'])
def generate_responses_route():
    data = request.get_json(force=True)
    return jsonify(generate_responses(data))

@app.route('/api_keys', methods=['POST'])
def set_api_keys_route():
    data = request.get_json(force=True)
    return jsonify(set_api_keys(data))

if __name__ == '__main__':
    app.run(debug=True)
