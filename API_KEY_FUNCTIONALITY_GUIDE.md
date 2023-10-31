
# User-specific API Key Functionality Guide

## Objective

Allow each user to use their own API key for interacting with various services like Gmail, Google Calendar, and Zoom.

## Frontend Changes

### Steps:

1. **API Key Input Form**: Add a form field in the user settings page where users can input their API key.
2. **Store API Key**: Use secure client-side storage to save the API key locally. Do not store it in plain text.
3. **Send API Key**: Attach the API key in the header or as a parameter while making API calls to the backend.

## Backend Changes

### Steps:

1. **Read API Key**: Add middleware to read the API key from incoming requests.
2. **Validate API Key**: Verify the API key and proceed only if it is valid.
3. **Use API Key**: Use the provided API key for making subsequent API calls to Gmail, Google Calendar, and Zoom services.

### Environment Variable (Alternative)

If you prefer to use environment variables for API keys:

1. **Read from Env**: Modify the backend code to read the API key from an environment variable.
2. **User Mapping**: Create a mapping between the user and the corresponding API key environment variable.

By implementing these steps, you can allow each user to use their own API key.
