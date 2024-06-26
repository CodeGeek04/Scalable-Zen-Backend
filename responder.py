from datetime import datetime
import openai
import os
openai.api_key = os.environ["OPENAI_API_KEY"]

def query(role, content):
    return {"role": role, "content": content}

def generate_resp(history, sender_email, owner_email, free_time, assistant_email):
    # Initialize the conversation with the assistant's role and a prompt
    today = datetime.now()
    formatted_date = today.strftime("%Y-%m-%d")

    # Set the context for the assistant
    body_context = f'''You are a meeting scheduling agent acting as a bridge . Your name is Zen ({assistant_email}), virtual assistant, working under {owner_email} (the owner). You will have access to the owner's availability. You can either suggest 3-4 slots for the meeting to the client, or generate a confirmation message for the client, based on the conversation provided.'''

    body_prompt = '''You are Zen ({}). Today is {}. You are working under, {} (the owner), who has free time slots: {}. 
                    They are trying to schedule a meeting with the client, {} (extract the name properly to write in email). 
                    Look at this conversation conversation: "{}". Now, look thoroughly through this conversation, and based on this, you have to do one of the following:
                    1) Suggest free times for the meeting (atleast 2) from available time slots, (and client's preferences, if any) that the client can choose from. Limit the duration to 30-45 minutes, and provide start + end time both and the time-zone. Be biased towards suggesting times in the next 2-3 days.
                    2) Generate a confirmation message for the client containing necessary details regarding time of meeting, like starting and ending time. Do not include location of meeting.
                    3) If the user has some query for time slots, or they are just sending regards, then generate the email accordingly for the user.
                    Decide just one of these and then frame the body of the email, and check the time zone properly as provided. Carefully include the client's preferences if present in the conversation, and provide suitable 30minute-1hour window(s).
                    Do not write subject of the email.
                    I will be sending your response directly to the client as it is, so you need to reply JUST THE BODY of email which will be automatically sent to the client. 
                    Do not even share any notes/instructions/your thought process.
                    Be very brief and to the point. Do not write anything unnecessary.
                    If you have already provided suggestions, and client is agreeing to one of them, just generate a confirmation message.
                    While giving regards/salutation, use- Zen, Virtual Assistant to "owner's name".
                    You have all the required names for the email content, so do not leave out any placeholders anywhere. 
                    The email (your response) will be sent directly to the client as it is.
                    If meeting is already scheduled, do not schedule it again, and decide properly how to reply'''.format(assistant_email, str(formatted_date), owner_email, free_time, sender_email, history) 
    messages_list = [
        query("system", body_context),
        query("user", body_prompt)
    ]
    print("SYSTEM MESSAGE: {}".format(body_context))
    print("USER PROMPT: {}".format(body_prompt))
    # Generate a response using GPT-3.5-turbo
    print("GENERATING BODY")
    try:
        body_response = openai.chat.completions.create(
            model="gpt-4",
            messages=messages_list
        )
    except Exception as e:
        print("ERROR: {}".format(e))
        raise e
    print("GOT IT")

    # Extract the assistant's reply from the response
    body_reply = body_response.choices[0].message.content
    if body_reply == "ERROR":
        raise Exception("Empty response from GPT-3.5-turbo")

    subject_context = '''I will give you an email, and generate just a single proper subject for the email. Return the subject and nothing else'''

    # Create the prompt
    subject_prompt = '''Content of the email: "{}"'''.format(body_reply)

    messages_list = [
        query("system", subject_context),
        query("user", subject_prompt)
    ]

    # Generate a response using GPT-3.5-turbo
    print("GENERATING SUBJECT")
    subject_response = openai.chat.completions.create(
        model="gpt-4",
        messages=messages_list
    )
    print("GOT IT")

    # Extract the assistant's reply from the response
    subject_reply = subject_response.choices[0].message.content

    return body_reply, subject_reply
