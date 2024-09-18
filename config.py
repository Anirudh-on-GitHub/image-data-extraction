import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
except:
    load_dotenv()
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

if not GOOGLE_API_KEY:
    raise ValueError("API key not found. Please set 'GOOGLE_API_KEY'.")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = '''Analyze the attached image and extract the following information:
- Identify all columns present in the table within the image.
- Extract the data from each row for all identified columns.
- Return the extracted information in a JSON format where:
  - The keys are the column names (derived from the table headers).
  - Each object in the array represents a complete row of data.
  - Include all rows that have a valid entry in the first column (usually a serial number or ID).

Ensure that the JSON structure accurately reflects the table's layout and content. If there are multiple rows of data, each row should be a separate object in the array
.'''

safe = [
        {
            "category": "HARM_CATEGORY_DANGEROUS",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE",
        },
    ]
