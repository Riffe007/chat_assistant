import openai
import asyncio
from config.settings import OPENAI_API_KEY, CHAT_ASSISTANT_ID
from config.database import chat_collection
from fastapi import HTTPException

# OpenAI Async Client
client = openai.AsyncOpenAI(api_key=OPENAI_API_KEY)

async def chat_with_assistant(user_id: str, user_message: str):
    """Handles chat using OpenAI Assistant with built-in Vector Store and Function Calling."""

    try:
        # **Step 1: Create a Thread (if needed)**
        thread = await client.beta.threads.create()

        # **Step 2: Add User Message to Thread**
        await client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_message
        )

        # **Step 3: Run Assistant**
        run = await client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=CHAT_ASSISTANT_ID
        )

        # **Step 4: Poll for Completion**
        while run.status in ["queued", "in_progress"]:
            await asyncio.sleep(2)
            run = await client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

        # **Step 5: Retrieve AI Response**
        messages = await client.beta.threads.messages.list(thread_id=thread.id)

        if messages.data and messages.data[0].content:
            response_text = messages.data[0].content[0].text.value
        else:
            raise HTTPException(status_code=500, detail="No response generated.")

        # **Step 6: Store Chat History in MongoDB**
        chat_entry = {
            "user_id": user_id,
            "user_message": user_message,
            "ai_response": response_text
        }
        await chat_collection.insert_one(chat_entry)

        return {"response": response_text}

    except openai.APIError as e:
        raise HTTPException(status_code=502, detail=f"OpenAI API Error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
