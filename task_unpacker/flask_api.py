from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import json
from io import BytesIO
from datetime import datetime
from langchain_community.chat_models import ChatOpenAI
from core.unpack_llm import unpack_tasks
from core.history import save_session, list_sessions, load_session
from core.pdf_utils import generate_task_pdf

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests (from lovable.ai frontend)

UPLOAD_DIR = "uploads"
SESSION_DIR = "sessions"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(SESSION_DIR, exist_ok=True)

@app.route("/history", methods=["GET"])
def history_alias():
    return get_sessions()

@app.route("/unpack", methods=["POST"])
def unpack():
    data = request.json
    input_text = data.get("input")

    if not input_text:
        return jsonify({"error": "No input provided"}), 400

    try:
        parsed = unpack_tasks(input_text)
        return jsonify(parsed)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/save-session", methods=["POST"])
def save():
    data = request.json
    input_text = data.get("input")
    response = data.get("response")
    completed = data.get("completed", [])

    if not input_text or not response:
        return jsonify({"error": "Missing input or response"}), 400

    try:
        filename = save_session(input_text, response, completed)
        return jsonify({"message": "Session saved", "filename": filename})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/sessions", methods=["GET"])
def get_sessions():
    try:
        sessions = list_sessions()
        return jsonify(sessions)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/session/<session_id>", methods=["GET"])
def get_session(session_id):
    try:
        session = load_session(session_id)
        return jsonify(session)
    except FileNotFoundError:
        return jsonify({"error": "Session not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/pdf/<session_id>", methods=["GET"])
def download_pdf(session_id):
    try:
        session = load_session(session_id)
        parsed_data = json.loads(session["response"]) if isinstance(session["response"], str) else session["response"]
        buffer = BytesIO()
        generate_task_pdf(parsed_data=parsed_data, output_stream=buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name=f"{session_id}.pdf", mimetype="application/pdf")
    except FileNotFoundError:
        return jsonify({"error": "Session not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug=True)
