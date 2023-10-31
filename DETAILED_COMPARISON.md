
# Detailed Comparison between Zenpal and Harmonized Project

This document provides an exhaustive comparison between the original Zenpal project and the new harmonized project. The aim is to explain how each feature and file in Zenpal has been adapted, enhanced, or replaced in the harmonized project.

## Project Structure

### Zenpal

- `calendar_api.py`: Provides functionalities related to calendar management.
- `event_planner.py`: Handles event planning logic.
- `firebaseCredentials.json`: Credentials for Firebase.
- `gmail_api.py`: Gmail API functionalities.
- `initialize_agent.py`: Initializes the AI agent.
- `list_emails.py`: Lists emails from Gmail.
- `push_notifs_setup.py`: Handles push notification setup.
- `read_threads.py`: Reads email threads from Gmail.
- `responder.py`: Responds to emails.
- `services.py`: Miscellaneous services.
- `servicesCredentials.json`: Credentials for various services.

### Harmonized Project

- `firebaseCredentials.json`: Credentials for Firebase, copied from Zenpal.
- `src/`: Source code directory.
  - `__init__.py`: Initializer for Python package.
  - `account_manager.py`: Manages new email accounts.
  - `draft_manager.py`: Saves generated responses as drafts in Gmail.
  - `email_manager.py`: Fetches unread emails from Gmail.
  - `meeting_scheduler.py`: Schedules meetings using the Zoom API.
  - `response_generator.py`: Uses ChatGPT to generate email responses.

## Comparisons

1. **Firebase Integration**: Both Zenpal and the harmonized project use Firebase. The credentials (`firebaseCredentials.json`) have been directly copied from Zenpal.

2. **Calendar Management**: The functionalities from Zenpal's `calendar_api.py` have been integrated into the harmonized project's `src/email_manager.py`.

3. **Email Management**: Zenpal used multiple files (`gmail_api.py`, `list_emails.py`, `read_threads.py`, `responder.py`) for email-related functionalities. The harmonized project consolidates these into a single, modular `src/email_manager.py` file.

4. **Event Planning**: Zenpal's `event_planner.py` has been replaced with `src/meeting_scheduler.py` in the harmonized project, which uses the Zoom API for meeting scheduling.

5. **Services and Credentials**: Zenpal had separate files (`services.py` and `servicesCredentials.json`). In the harmonized project, all configurations are managed through the `config/` directory.

6. **AI Agent**: Zenpal's `initialize_agent.py` initializes an AI agent. This is inherently part of the ChatGPT functionalities in `src/response_generator.py` of the harmonized project.

## Conclusion

The harmonized project aims to keep the best of both worlds. It adopts a more modular approach, making it easier to manage and extend. Key functionalities from Zenpal have been carefully integrated to ensure a seamless and enhanced user experience.
