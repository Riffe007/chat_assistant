from fastapi import APIRouter, HTTPException
from app.chat_logic import chat_with_assistant
from app.calendar_logic import schedule_meeting

router = APIRouter()

@router.post("/chat")
async def chat(user_id: str, message: str):
    """Handles AI chat using OpenAI Assistant with built-in Vector Store"""
    response = await chat_with_assistant(user_id, message)
    return {"message": response}

@router.post("/schedule_meeting")
async def book_meeting(user_email: str, meeting_time: str):
    """Schedules a meeting via Google Calendar"""
    try:
        result = schedule_meeting(user_email, meeting_time)
        return {"message": "Meeting scheduled!", "meeting_details": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
