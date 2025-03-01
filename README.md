# 🚀 AI Chat Assistant with OpenAI Assistant + Google Calendar Integration  

An advanced, **AI-powered chat assistant** that leverages **OpenAI Assistants API** with a **built-in vector store** to handle intelligent conversations about **Timothy Riffe’s skills and expertise**. It also integrates **Google Calendar API** to **automatically schedule meetings** from within the chat.

---

## 🛠️ **Key Features**
✅ **AI Chat Powered by OpenAI Assistants API** – Uses a **fine-tuned assistant with a vector store** for highly relevant responses.  
✅ **Automated Scheduling with Google Calendar** – Users can **book meetings directly from chat** using OpenAI **Function Calling**.  
✅ **Scalable & Asynchronous** – Built with **FastAPI** and **Motor (MongoDB Async)** for high-performance and scalability.  
✅ **Secure & Production-Ready** – Uses **.env for API keys**, **secret scanning protection**, and **OAuth2 authentication for Google API**.  
✅ **Optimized for Real-World Use** – Structured to handle real conversations, **resume queries, scheduling, and skills-based Q&A**.  

---

## 📂 **Project Structure**
```plaintext
ai-chat-assistant/ 
│── app/ 
│ ├── main.py # FastAPI App Entry Point 
│ ├── chat_logic.py # AI Chat using OpenAI Assistant + Function Calling 
│ ├── calendar_logic.py # Google Calendar API Integration 
│ ├── database.py # MongoDB Connection (Motor) 
│ ├── models.py # Pydantic Models for API Requests 
│ ├── routes.py # API Routes 
│── config/ 
│ ├── settings.py # API Keys & Environment Variables 
│ ├── database.py # DB Configuration 
│── .gitignore 
│── requirements.txt # Python Dependencies 
│── README.md
```
```yaml

---

## 🚀 **Quick Start Guide**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Riffe007/ai-chat-assistant.git
cd ai-chat-assistant
```
### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
### 4️⃣ Set Up Environment Variables
Create a .env file in the config/ directory with:
```ini
OPENAI_API_KEY=your-openai-api-key
CHAT_ASSISTANT_ID=your-assistant-id
MONGO_URI=your-mongodb-uri
GOOGLE_APPLICATION_CREDENTIALS=path-to-your-google-service-account.json
```
### 🔒 Security Note: Your .env file is already ignored by .gitignore to prevent accidental API key leaks.
## 5️⃣ Run the Application
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
The API will now be running at http://127.0.0.1:8000/

# 🛠️ API Endpoints
### 💬 AI Chat API


| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/chat` | Chat with AI Assistant about skills, experience, and general inquiries. |

#### **Example Request**
```sh
curl -X 'POST' 'http://127.0.0.1:8000/chat' \
  -H 'Content-Type: application/json' \
  -d '{"user_id": "12345", "message": "Tell me about Timothy Riffe’s expertise in AI"}'
```
Example Response
```json
{
  "message": "Timothy Riffe is an AI Engineer with deep expertise in machine learning, cybersecurity, and investment banking..."
}
```
### 📅 Google Calendar Scheduling API

| Method | Endpoint            | Description                                        |
|--------|---------------------|----------------------------------------------------|
| `POST` | `/schedule_meeting` | Schedules a meeting with Timothy via Google Calendar API. |

#### **Example Request**
```sh
curl -X 'POST' 'http://127.0.0.1:8000/schedule_meeting' \
  -H 'Content-Type: application/json' \
  -d '{"user_email": "user@example.com", "meeting_time": "2025-03-01T15:00:00Z"}'
```
Example Response
```json
{
  "message": "Meeting scheduled!",
  "meeting_details": {
    "meeting_link": "https://meet.google.com/xyz-123",
    "event_id": "abcd1234"
  }
}
```
## 🔧 Technology Stack

| Component       | Technology Used                      |
|----------------|-------------------------------------|
| **AI Chat**    | OpenAI Assistants API (Vector Store) |
| **Scheduling** | Google Calendar API (OAuth2)        |
| **Backend**    | FastAPI (Asynchronous)              |
| **Database**   | MongoDB with Motor (Async)          |
| **Infrastructure** | Uvicorn, Docker (Optional) |

---

## 🏗️ Future Enhancements

🚀 **Real-time WebSocket Chat** for live AI interactions  
🚀 **CRM Integration** for lead tracking and automation  
🚀 **Multi-Assistant Setup** (Resume Assistant + Chat Assistant)  

---

## 🛠️ Troubleshooting & Debugging

### 🔍 OpenAI API Issues
- Ensure **`OPENAI_API_KEY`** is **valid**.
- If experiencing **delays**, check **OpenAI status**: [OpenAI Status](https://status.openai.com)

### 🔍 Google Calendar API Issues
- Make sure **OAuth credentials** are set up correctly.
- Check **Google Calendar permissions** in your Google Cloud Console.

### 🔍 MongoDB Issues
- If running locally, ensure **MongoDB is running**:
```sh
sudo systemctl start mongod
```
- If using Atlas, verify MONGO_URI is correct.
# 📜 License
This project is licensed under the MIT License – feel free to use and modify!
# 💡 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss.

# 🌟 Acknowledgments
🔹 OpenAI for Assistants API
🔹 Google for Calendar API
🔹 FastAPI for Modern Python Backend

# 🔥 Built by Timothy Riffe – LinkedIn



