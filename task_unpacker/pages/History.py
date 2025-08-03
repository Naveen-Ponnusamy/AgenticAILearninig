import streamlit as st
import os
import json
from config.settings import SESSION_DIR

st.set_page_config(page_title="📚 Session History")
st.title("📚 Session History")

if not os.path.exists(SESSION_DIR):
    os.makedirs(SESSION_DIR)

session_files = [f for f in os.listdir(SESSION_DIR) if f.endswith(".json")]

if not session_files:
    st.info("No sessions saved yet.")
else:
    session_files.sort(reverse=True)
    selected_file = st.selectbox("Select a session to view:", session_files)

    if selected_file:
        with open(os.path.join(SESSION_DIR, selected_file), "r") as f:
            session_data = json.load(f)

        st.subheader("🎯 Goal")
        st.markdown(session_data.get("input", "No input found"))

        st.subheader("✅ Completed Tasks")
        for task in session_data.get("completed", []):
            st.markdown(f"- [x] {task}")

        st.subheader("🧠 Full Task Response (Raw JSON)")
        st.json(json.loads(session_data.get("response", "{}")))
