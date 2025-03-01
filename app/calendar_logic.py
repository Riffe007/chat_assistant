from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime
import os

# Load Google Calendar Credentials
GOOGLE_CREDENTIALS_FILE = "config/service_account.json"

credentials = service_account.Credentials.from_service_account_file(
    GOOGLE_CREDENTIALS_FILE,
    scopes=["https://www.googleapis.com/auth/calendar"]
)

calendar_service = build("calendar", "v3", credentials=credentials)

def schedule_meeting(user_email: str, meeting_time: str, duration: int = 30):
    """Schedules a Google Calendar meeting via Function Calling"""
    event = {
        "summary": "Meeting with Timothy Riffe",
        "location": "Google Meet",
        "description": "AI-powered scheduled meeting with Timothy.",
        "start": {"dateTime": meeting_time, "timeZone": "America/Los_Angeles"},
        "end": {
            "dateTime": (datetime.datetime.fromisoformat(meeting_time) + datetime.timedelta(minutes=duration)).isoformat(),
            "timeZone": "America/Los_Angeles",
        },
        "attendees": [{"email": user_email}],
        "reminders": {"useDefault": True},
    }

    created_event = calendar_service.events().insert(calendarId="primary", body=event).execute()
    return {"meeting_link": created_event["hangoutLink"], "event_id": created_event["id"]}
