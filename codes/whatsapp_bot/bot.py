from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    """Handle incoming messages from WhatsApp."""
    incoming_msg = request.values.get('Body', '').lower().strip()
    rsp = MessagingResponse()
    response = rsp.message()
    
    if incoming_msg.lower() == 'hello':
        response.body("Hello! How can I assist you today?")
    elif incoming_msg.lower() == 'bye':
        response.body("Goodbye! Have a great day!")
    else:
        response.body("I'm not sure how to respond to that. Please try 'hello' or 'bye'.")

    return str(response)

if __name__ == "__main__":
    app.run()