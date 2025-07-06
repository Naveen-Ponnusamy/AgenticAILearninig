import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Feedback Survey", layout="centered")

st.title("📝 Feedback Survey Form")
st.markdown("Please take a moment to provide your feedback.")

# Form
with st.form("survey_form"):
    name = st.text_input("Name", max_chars=50)
    email = st.text_input("Email", max_chars=100)
    rating = st.slider("Rate your experience (1 = Poor, 5 = Excellent)", 1, 5, 3)
    suggestion = st.text_area("Any suggestions or comments?")
    
    submitted = st.form_submit_button("Submit")

# CSV file to store results
csv_file = "survey_responses.csv"

if submitted:
    if not name or not email:
        st.error("Name and Email are required.")
    else:
        # Create dataframe
        new_data = pd.DataFrame([[name, email, rating, suggestion]],
                                columns=["Name", "Email", "Rating", "Suggestion"])
        
        # Append to CSV
        if os.path.exists(csv_file):
            existing_data = pd.read_csv(csv_file)
            updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        else:
            updated_data = new_data

        updated_data.to_csv(csv_file, index=False)
        st.success("Thank you! Your response has been recorded.")

# Show existing responses
if os.path.exists(csv_file):
    with st.expander("📊 View All Responses"):
        df = pd.read_csv(csv_file)
        st.dataframe(df)
