import os
import json
from datetime import datetime
from config.settings import SESSION_DIR


def save_session(input_text, response, completed_tasks):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_data = {
        "input": input_text,
        "response": response,
        "completed": list(completed_tasks)  # Convert set to list for JSON
    }
    filename = f"session_{now}.json"
    path = os.path.join(SESSION_DIR, filename)
    with open(path, "w") as f:
        json.dump(session_data, f, indent=2)
    return filename


def load_all_sessions():
    if not os.path.exists(SESSION_DIR):
        return []

    sessions = []
    for file in sorted(os.listdir(SESSION_DIR), reverse=True):
        if file.endswith(".json"):
            path = os.path.join(SESSION_DIR, file)
            with open(path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    data["filename"] = file
                    sessions.append(data)
                except json.JSONDecodeError:
                    continue
    return sessions


def load_session(filename):
    file_path = os.path.join(SESSION_DIR, filename)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None
def list_sessions():
    return [session["filename"] for session in load_all_sessions()]
