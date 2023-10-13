
README for Flask Gmail Assistant

Description:
This application is a Flask server that integrates with the Gmail API to read and respond to emails. It automatically checks for new email threads and emails, generates responses using a predefined method (`generate_resp`), and sends back the response. Additionally, it can schedule meetings using Google Calendar.

Setup & Installation:

1. Dependencies:
   - Flask: Web framework.
   - gmail_api: Custom module to interact with Gmail API.
   - Other modules: Various utility functions and API integrations.

2. Setting up Environment Variable:
   - Before running the application, you must set the OPENAI_API_KEY environment variable. This key is required for OpenAI integration.
     export OPENAI_API_KEY=YOUR_OPENAI_KEY

3. Service Account:
   - Ensure you have a gmail_service.pkl (pickle file) containing the Gmail service object. This allows the application to interact with Gmail API on behalf of the user.

4. Assistant Email:
   - Store the assistant's email in assistant_email.txt. This email ID is used to filter out emails that the assistant sends or receives.

Running the Application:

- Local Setup:
   python your_flask_filename.py
   By default, the application runs on port 5000.

- Deployment (e.g., on Heroku):
   - Deploy as per the platform's guidelines.
   - Ensure the PORT environment variable is set for the platform to bind to the correct port.

Usage:

1. Home Endpoint (/):
   - This endpoint starts the processing of unread email threads and emails. It marks emails as read once processed.

2. Email & Calendar Integration:
   - The application reads new unread emails and threads.
   - It generates a response for each email or thread using the generate_resp function.
   - If a meeting is to be scheduled, it fetches the free time of the owner and schedules a meeting using Google Calendar.

3. Utilities:
   - Various utility functions are included, such as mark_email_as_read, create_raw_email, extract_email, etc., to facilitate email processing.

Notes:

- Ensure you have the necessary Google Cloud permissions and have shared the calendar with the service account email for Google Calendar integration.
- Always keep your OPENAI_API_KEY secret. Do not expose it in public repositories or public spaces.
