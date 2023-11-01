from flask import Flask, request, jsonify
from src.email_manager import fetch_unread_threads, extract_emails_from_thread, fetch_free_time
from flask import session, redirect
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import logging, os
from firebase_admin import firestore, credentials
from src.response_generator import generate_response, generate_history
# from src.meeting_scheduler import send_email
from src.list_emails import get_agents, get_associated_emails_for_agent
from src.account_manager import get_gmail_service, send_email


app = Flask(__name__)
cred = credentials.Certificate("firebaseCredentials.json")
firebase_admin.initialize_app(cred)

@app.route('/process_unread_emails', methods=['POST'])
def process_unread_emails_route():
    # Extract gmail token for the agent in AGENTS collection's first document
    all_agents = get_agents()
    gmail_token = all_agents[0]['gmailToken']
    agent_email = all_agents[0]['agentEmail']
    # Use gmail service to fetch unread threads
    gmail_service = get_gmail_service(gmail_token)
    # List all emails
    # Get associated emails for the agents
    associated_emails = get_associated_emails_for_agent(all_agents[0]['id'])
    associated_email_ids = list(associated_emails.keys())
    unread_threads = fetch_unread_threads(gmail_service)

    for thread in unread_threads:
        # Extract all email ids in the thread
        all_emails_in_thread = extract_emails_from_thread(thread)
        
        # Determine owner email
        owner_email = next((email for email in all_emails_in_thread if email in associated_emails), None)

        # If owner_email is missing or there's no other email, mark the thread as read and continue
        if not owner_email or len(all_emails_in_thread) <= 1:
            gmail_service.users().threads().modify(userId='me', id=thread['id'] , body={'removeLabelIds': ['UNREAD']}).execute()
            continue

        # Determine client email
        client_email = next((email for email in all_emails_in_thread if email != owner_email), None)
        free_time = fetch_free_time(associated_emails[owner_email])

        # Generate a response for the client, and BCC the owner
        history = generate_history(thread)
        responses = generate_response(history, client_email, owner_email, agent_email, free_time)
        # Send the response and mark thread as read
        send_email(gmail_service, agent_email, client_email, owner_email, responses['subject'], responses['body'], thread['id'])
        gmail_service.users().threads().modify(userId='me', id=thread['id'] , body={'removeLabelIds': ['UNREAD']}).execute()
    return jsonify({
        'message': 'Processed unread emails successfully'
    })

@app.route('/authenticate_calendar', methods=['POST', 'GET'])
def authenticate():
    user_id = request.args.get('userId')
    print("USER ID: ", user_id)
    logging.info("USER ID: ", user_id)
    flow = InstalledAppFlow.from_client_secrets_file(
        'servicesCredentials.json',
        ['https://www.googleapis.com/auth/calendar']
    )
    # flow.redirect_uri = url_for('callback', _external=True)
    flow.redirect_uri = "https://zenbackend-mw5cw3u7ga-uc.a.run.app/callback"
    print(flow.redirect_uri)
    logging.info("Redirect URI: ", flow.redirect_uri)
    authorization_url, _ = flow.authorization_url(prompt='consent')
    session['userId'] = user_id
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    print("SESSION: ", session)
    logging.info("SESSION: ", session)
    userId = session.get("userId")
    print("USER ID IN CALLBACK: ", userId)
    logging.info("USER ID IN CALLBACK: ", userId)
    flow = InstalledAppFlow.from_client_secrets_file(
        'servicesCredentials.json',
        ['https://www.googleapis.com/auth/calendar']
    )
    # flow.redirect_uri = url_for('callback', _external=True)
    flow.redirect_uri = "https://zenbackend-mw5cw3u7ga-uc.a.run.app/callback"
    print(flow.redirect_uri)
    authorization_response = request.url.replace("http://", "https://")
    flow.fetch_token(authorization_response=authorization_response)

    # Get the user's email
    service = build('calendar', 'v3', credentials=flow.credentials)
    profile = service.calendarList().get(calendarId='primary').execute()
    email = profile['id']

    # Serialize credentials
    serialized_credentials = {
        'token': flow.credentials.token,
        'refresh_token': flow.credentials.refresh_token,
        'token_uri': flow.credentials.token_uri,
        'client_id': flow.credentials.client_id,
        'client_secret': flow.credentials.client_secret,
        'scopes': flow.credentials.scopes
    }
    print("SERIALIZED CREDENTIALS: ", serialized_credentials)
    logging.info("SERIALIZED CREDENTIALS: ", serialized_credentials)

    # Prepare data for Firestore
    user_data = {
        'calendarCredentials': serialized_credentials,
        'calendarEmail': email,
        'status': 'CalConnected-Active'
    }

    db = firestore.client()
    users_ref = db.collection(u'USERS')
    user_doc = users_ref.document(userId)

    user_doc.update(user_data)
    print("USER DATA UPDATED FOR USER: ", userId)
    logging.info("USER DATA UPDATED FOR USER: ", userId)

    return redirect("https://zen-scheduler-web.vercel.app/dashboard")

port = int(os.environ.get("PORT", 8080))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
