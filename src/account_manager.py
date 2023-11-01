from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText

def send_email(gmail_service, agent_email, client_email, owner_email, subject, body, thread_id):
    # Create a MIMEText object to represent the email
    mime_email = MIMEText(body)
    mime_email['to'] = client_email
    mime_email['bcc'] = owner_email
    mime_email['subject'] = subject
    mime_email['from'] = agent_email

    # Convert the MIMEText email into a base64 encoded string
    encoded_email = base64.urlsafe_b64encode(mime_email.as_bytes()).decode('utf-8')
    
    # Send the email and append it to the given thread
    gmail_service.users().messages().send(userId='me', body={'raw': encoded_email, 'threadId': thread_id}).execute()

def get_gmail_service(token):
    # Create a Credentials object from the provided token
    credentials = Credentials(token=token['token'],
                              refresh_token=token['refresh_token'],
                              token_uri='https://oauth2.googleapis.com/token',
                              client_id=token['client_id'],
                              client_secret=token['client_secret'],
                              scopes=token['scopes'])
    
    # Build the Gmail service client
    service = build('gmail', 'v1', credentials=credentials)

def extract_emails_from_thread(thread_data):
    all_emails = []

    for message in thread_data['messages']:
        headers = message['payload']['headers']
        for header in headers:
            if header['name'] in ['From', 'To', 'Cc', 'Bcc']:
                # Extract and append all emails from header values
                all_emails.extend([email.strip() for email in header['value'].split(',')])

    return list(set(all_emails))  # Return unique email addresses

    
    return service
