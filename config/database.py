from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

# Async MongoDB connection
client = AsyncIOMotorClient(MONGO_URI)
db = client["chat_ai"]

# Collections
chat_collection = db["chat_history"]
user_collection = db["users"]

print("✅ Connected to MongoDB asynchronously using Motor!")
