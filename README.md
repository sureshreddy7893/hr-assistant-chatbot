# HR Assistant Chatbot using Dialogflow & Python Webhook

## 📌 Project Overview
The HR Assistant Chatbot is an AI-powered conversational application built using **Dialogflow ES** and a **Python Flask webhook**.  
It automates common HR-related employee queries such as leave balance, leave policy, attendance status, holidays, and HR contact details.

Dialogflow handles **Natural Language Processing (NLP)**, while the webhook acts as the **backend** to process business logic and return **dynamic responses**.

---

## 🎯 Problem Statement
In many organizations, HR teams spend a significant amount of time answering repetitive employee queries.  
This manual process increases workload and delays responses.

**Goal:**  
To build a chatbot that can automatically respond to common HR queries and reduce dependency on manual HR support.

---

## 🧠 Solution
- Dialogflow is used for intent detection and entity extraction.
- A Python Flask webhook processes backend logic.
- Communication between Dialogflow and the webhook happens using **HTTP POST requests with JSON data**.
- ngrok is used to expose the local webhook during development.

---

## 🛠️ Technologies Used
- **Dialogflow ES** – Conversational AI platform
- **Python** – Backend programming language
- **Flask** – Web framework for webhook
- **ngrok** – Exposes local server to the internet
- **HTTP POST & JSON** – Backend communication
- **GitHub** – Version control and project hosting

---

## 🧩 Architecture
User
↓
Dialogflow (Intent Detection & Entity Extraction)
↓
Webhook (Python Flask Backend)
↓
Dialogflow (Fulfillment Response)
↓
User

---

## 📂 Project Structure
hr-assistant-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── documentation/
│ └── HR_Assistant_Chatbot_Documentation.pdf
└── screenshots/

---

## 📌 Intents Implemented
- **Default Welcome Intent** – Greets the user and explains bot capabilities
- **Default Fallback Intent** – Handles unknown queries
- **Leave_Policy** – Explains company leave rules
- **Leave_Balance** – Provides dynamic leave balance
- **Attendance_Status** – Shows attendance details
- **Holiday_List** – Displays company holidays
- **HR_Contact** – Shares HR contact details

---

## 📌 Entities Used
- **@leave_type** (custom entity)
  - casual leaves
  - sick leaves
  - earned leaves
- **@sys.date-period** (system entity)
  - this month
  - last month
  - next week

---

## 🔗 Webhook & Backend Logic
- Dialogflow sends intent and entity data to the webhook using **HTTP POST**.
- Data is sent in **JSON format**.
- Flask webhook processes the request and returns a JSON response using `fulfillmentText`.

### Example:
**User Query:**  
`How many casual leaves do I have?`

**Webhook Logic:**  
- Extracts intent: `Leave_Balance`
- Extracts entity: `leave_type = casual`
- Returns dynamic response accordingly.

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
- pip install flask

2️⃣ Run the Flask application
- python app.py

3️⃣ Start ngrok
- ngrok http 5000

4️⃣ Configure Dialogflow
Enable Fulfillment
- Set webhook URL:https://nameless-unnumbed-lavette.ngrok-free.dev/webhook
Enable webhook for:
- Leave_Balance
- Attendance_Status

---

💬 Sample Conversations
User: How many casual leaves do I have?
Bot: You have 6 casual leaves remaining.

---

📄 Documentation
Detailed project documentation is available in the documentation/ folder in PDF format.

---

🚀 Future Enhancements
Database integration (MySQL / Firebase)
Employee authentication
WhatsApp / Telegram integration
Voice-based chatbot
Cloud deployment without ngrok

---

👤 Author
Suresh Reddy Munagala

⭐ If you find this project useful, feel free to fork or star the repository!
