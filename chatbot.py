# AI Security Lab - Chatbot Module

def get_chatbot_response(user_message, model="Demo"):

    # Check empty message
    if not user_message.strip():
        return "Please enter a message."

    message = user_message.lower()

    # Basic chatbot responses
    if "hello" in message or "hi" in message:
        return "Hello! Welcome to AI Security Testing Lab."

    elif "security" in message:
        return (
            "AI Security protects AI systems "
            "from risks such as prompt injection, "
            "data leakage and unsafe tool usage."
        )

    elif "owasp" in message:
        return (
            "OWASP provides security guidance "
            "for Large Language Models and "
            "Agentic AI applications."
        )

    elif "python" in message:
        return (
            "Python is used in this project "
            "for chatbot development and security testing."
        )

    elif "model" in message:
        return (
            "Current selected model: " + model
        )

    else:
        return (
            "I received your message: "
            + user_message
            + ". This is the local demo chatbot. "
            "Real AI model integration is pending."
        )