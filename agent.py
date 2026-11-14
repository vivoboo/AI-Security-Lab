# AI Security Lab - Agent Module

# Fake data for local testing only
FAKE_FILES = {
    "notes.txt": "This is a fake project notes file.",
    "security.txt": "AI security testing uses safe mock data.",
    "demo.txt": "SECRET-FLAG-123"
}

# Explicit allowlist
APPROVED_FILES = {
    "notes.txt",
    "security.txt"
}


def read_fake_file(filename):

    if filename not in APPROVED_FILES:
        return {
            "status": "BLOCKED",
            "message": "File access denied."
        }

    if filename not in FAKE_FILES:
        return {
            "status": "BLOCKED",
            "message": "File not found."
        }

    return {
        "status": "ALLOWED",
        "filename": filename,
        "content": FAKE_FILES[filename]
    }


def mock_email(recipient, message, approved=False):

    if not approved:
        return {
            "status": "BLOCKED",
            "message": "Approval required.",
            "sent": False
        }

    return {
        "status": "SIMULATED",
        "recipient": recipient,
        "message": message,
        "sent": False
    }


def mock_http_request(url, approved=False):

    if not approved:
        return {
            "status": "BLOCKED",
            "message": "Approval required.",
            "real_request": False
        }

    return {
        "status": "SIMULATED",
        "url": url,
        "response": "Fake HTTP 200 OK",
        "real_request": False
    }