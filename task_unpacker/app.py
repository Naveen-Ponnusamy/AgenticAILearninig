import streamlit as st
import os
import json
import re
from datetime import datetime
from core.pdf_utils import generate_task_pdf
from io import BytesIO
from core.unpack_llm import unpack_tasks
from core.history import save_session
from config.settings import UPLOAD_DIR
from langchain_community.chat_models import ChatOpenAI


# Streamlit Page Setup
st.set_page_config(page_title="TaskUnpacker", layout="centered")
st.title("🧠 TaskUnpacker")
st.markdown("Upload a file or enter a vague goal to get a structured, actionable task list.")

# File or Text Input
input_text = None
uploaded_file = st.file_uploader("📄 Upload .pdf / .docx / .txt", type=["pdf", "docx", "txt"])
manual_input = st.text_area("✍️ Or paste your task/goal here", height=200)

if uploaded_file:
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        input_text = f.read()

elif manual_input:
    input_text = manual_input.strip()

# Main Button
if input_text and st.button("🧩 Unpack Task"):
    with st.spinner("Analyzing and unpacking tasks..."):
        try:
            parsed = unpack_tasks(input_text)
            st.session_state["result"] = parsed
            st.session_state["input_text"] = input_text
            st.session_state["completed"] = set()
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Display Results
if "result" in st.session_state:
    result = st.session_state["result"]
    st.subheader("🧠 Suggested Tasks")
    st.markdown(f"**🎯 Goal:** {result.get('goal_summary', 'N/A')}")

    completed_tasks = st.session_state.get("completed", set())

    for category in result.get("categories", []):
        with st.expander(f"📂 {category['name']}"):
            for task in category.get("tasks", []):
                key = f"{category['name']}::{task['task']}"
                checked = st.checkbox(f"✅ {task['task']}", key=key)
                if checked:
                    completed_tasks.add(key)
                else:
                    completed_tasks.discard(key)
                st.caption(f"Effort: {task['effort']} | Impact: {task['impact']}")
                if task.get("why_suggested"):
                    st.markdown(f"💡 *Why*: {task['why_suggested']}")
                if task.get("depends_on"):
                    st.markdown(f"🔗 *Depends on*: {', '.join(task['depends_on'])}")
                st.markdown("---")

    # Save session
    if st.button("💾 Save Progress"):
        try:
            save_session(
                input_text=st.session_state["input_text"],
                response=json.dumps(st.session_state["result"], indent=2),
                completed_tasks=list(completed_tasks)
            )
            st.success("✅ Session saved!")
        except Exception as e:
            st.error(f"❌ Save failed: {str(e)}")
                # PDF Download Button
    st.markdown("### 📄 Download Task Report")

    # PDF Download Button (only show when session state has valid data)
if "input_text" in st.session_state and "result" in st.session_state:
    buffer = BytesIO()
    generate_task_pdf(parsed_data=st.session_state["result"], output_stream=buffer)
    st.download_button(
    label="📥 Download PDF Report",
    data=buffer.getvalue(),
    file_name="task_report.pdf",
    mime="application/pdf"
    )



