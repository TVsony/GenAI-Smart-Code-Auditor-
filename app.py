import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch API key from .env
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API key not found. Ensure the .env file contains a valid GOOGLE_API_KEY.")
    st.stop()

# Configure Google Generative AI with the API key
genai.configure(api_key=api_key)

# Streamlit app configuration
st.set_page_config(
    page_title="Smart Code Auditor",
    page_icon="⚙️",
    layout="centered",
    initial_sidebar_state="auto",
)

# Custom CSS styling for better visibility
st.markdown(
    """
    <style>
        .stApp { ... }
        .header-title { ... }
        textarea { ... }
        button[kind="primary"] { ... }
        .subheader { ... }
        .report-title { ... }
        .footer { ... }
        .sidebar .sidebar-content { ... }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar configuration
st.sidebar.title("Smart Code Auditor Features")
st.sidebar.markdown(
    """
    - **<span style='color:white;'>Bug Detection</span>**: ...
    - **<span style='color:white;'>Code Insights</span>**: ...
    - **<span style='color:white;'>Time-Saving</span>**: ...
    """,
    unsafe_allow_html=True,
)

# Main header
st.markdown('<div class="header-title">Smart Code Auditor ⚙️</div>', unsafe_allow_html=True)
# st.write("Paste your Python script below, and the AI will provide a detailed analysis of potential bugs and improvements.")

# Input area for user code
code_input = st.text_area("🔍 Enter your Python code here:")

# Code review button
if st.button("Analyze Code"):
    if code_input.strip():
        with st.spinner("Analyzing your code..."):
            try:
                model = genai.GenerativeModel("models/gemini-1.5-flash")  # Adjust as needed
                session = model.start_chat(history=[])
                feedback = session.send_message(f"Review this Python code:\n{code_input}")
                
                # Display results
                st.markdown('<div class="subheader">📝 Code Analysis Report</div>', unsafe_allow_html=True)
                st.markdown('<div class="report-title">Bug Report:</div>', unsafe_allow_html=True)
                st.write(feedback.text)  # Adjust this if the API response format differs
            except Exception as error:
                st.error(f"An error occurred while reviewing your code: {error}")
    else:
        st.error("⚠️ Please provide some Python code before submitting.")

# Footer
st.markdown('<div class="footer">Please see below output </div>', unsafe_allow_html=True)
