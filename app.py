from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Server is running"

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()

    intent = req["queryResult"]["intent"]["displayName"]
    parameters = req["queryResult"].get("parameters", {})

    response_text = "Sorry, I couldn't process your request."

    if intent == "Leave_Balance":
        leave_type = parameters.get("leave_type")

        if leave_type == "casual":
            response_text = "You have 6 casual leaves remaining."
        elif leave_type == "sick":
            response_text = "You have 4 sick leaves remaining."
        elif leave_type == "earned":
            response_text = "You have 2 earned leaves remaining."
        else:
            response_text = (
                "Here is your current leave balance:\n"
                "• Casual Leave: 6 days\n"
                "• Sick Leave: 4 days\n"
                "• Earned Leave: 2 days"
            )

    elif intent == "Attendance_Status":
        date_period = parameters.get("date-period")

        if date_period:
            response_text = f"Your attendance for {date_period} is 20 present days and 2 absences."
        else:
            response_text = "Your attendance this month is 20 present days and 2 absences."

    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
