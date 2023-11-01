import openai
from datetime import datetime
import base64

def generate_history(thread_data):
    """
    Generates a history string for a given Gmail thread.

    Parameters:
        thread_data (dict): The thread data as returned by the Gmail API.

    Returns:
        str: A history string in the format "sender: content".
    """
    history = []

    for message in thread_data['messages']:
        headers = message['payload']['headers']
        sender = next((header['value'] for header in headers if header['name'] == 'From'), None)
        body_data = message['payload']['body'].get('data', '')
        
        # Decode the email body content from base64
        body_content = base64.urlsafe_b64decode(body_data).decode('utf-8').strip()

        history.append(f"{sender}: {body_content}")

    return "\n".join(history)

def query(role, content):
    return {"role": role, "content": content}

def generate_response(history, client_email, owner_email, assistant_email, free_time):
    # Initialize the date
    today = datetime.now()
    formatted_date = today.strftime("%Y-%m-%d")

    # Set the context and prompt for the assistant
    body_context = '''You are a meeting scheduling agent working for {}'''.format(owner_email)
    body_prompt = '''You are Zen. Your email: {}, Your owner's email: {}, Owner has free time at: {}
                    , client's email: {}, conversation so far: {}'''.format(assistant_email, owner_email, free_time, client_email, history)
    
    messages_list = [
        query("system", body_context),
        query("user", body_prompt)
    ]

    # Generate the body using GPT-3.5-turbo
    body_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages_list
    )
    body_reply = body_response['choices'][0]['message']['content']

    # Context for generating the subject
    subject_context = '''I will give you an email, generate appropriate subject'''  # As previously defined
    subject_prompt = '''Content of the email: "{}"'''.format(body_reply)
    
    messages_list = [
        query("system", subject_context),
        query("user", subject_prompt)
    ]

    # Generate the subject using GPT-3.5-turbo
    subject_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages_list
    )
    subject_reply = subject_response['choices'][0]['message']['content']

    return body_reply, subject_reply
