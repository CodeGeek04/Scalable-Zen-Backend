
# Complete Features List of the Harmonized Project

This document provides an exhaustive list of every single feature and functionality in the harmonized project. The aim is to give a comprehensive understanding of what the project can do.

## Email Management (`src/email_manager.py`)

- Fetch unread emails from a Gmail account.
- Archive emails.
- Mark emails as read or unread.
- Handle threaded conversations.
- Integrate calendar functionalities for scheduling.
- Fetch and save email attachments.

## Draft Management (`src/draft_manager.py`)

- Save generated email responses as drafts in Gmail.
- Retrieve saved drafts for review.
- Delete drafts.

## Account Management (`src/account_manager.py`)

- Add new email accounts for management.
- Remove existing email accounts.
- List all managed email accounts.

## Meeting Scheduling (`src/meeting_scheduler.py`)

- Schedule 1-1 meetings using the Zoom API.
- Schedule meetings with multiple participants.
- Handle time zones for international meetings.
- Send calendar invites to participants.
- Cancel scheduled meetings.

## Response Generation (`src/response_generator.py`)

- Generate automatic email responses using ChatGPT API.
- Context-aware response generation.
- Template-based responses for common queries.
- Error handling for unsupported queries.

## Configuration and Settings (`config/settings.py`)

- Configure Gmail API settings.
- Configure ChatGPT API settings.
- Configure Zoom API settings.
- Store and retrieve API keys securely.

## Utility Features

- Logging functionalities for debugging and auditing.
- Error handling and exception management.
- Unit tests for validating each module's functionalities.

This comprehensive list aims to capture every feature and functionality within the harmonized project, offering a complete overview of what the project is capable of doing.

- For deployment instructions, refer to `DEPLOYMENT_GUIDE.md`.

- For Docker and GCP deployment instructions, refer to `DOCKER_GCP_DEPLOYMENT_GUIDE.md`.
