import streamlit as st
import os
import tempfile
import zipfile
from main import process_folder
import logging
import shutil

st.set_page_config(page_title="Image Data Extraction", page_icon="📊")

st.title("Image Data Extraction")

st.write("""
This app extracts tabular data from images and converts it into CSV format using Google's Gemini API.
Upload multiple image files, and download the resulting CSV files.
""")

st.warning("""
**Important Note:**
- Please ensure all uploaded images are correctly oriented (not rotated).
- Supported formats: PNG, JPG, JPEG
- For best results, use clear, high-quality images of documents or tables.
""")

uploaded_files = st.file_uploader("Choose image files", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

if uploaded_files:
    if st.button("Process Images"):
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save uploaded files to temporary directory
            for uploaded_file in uploaded_files:
                file_path = os.path.join(temp_dir, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
            
            with st.spinner("Processing images..."):
                try:
                    results_path = process_folder(temp_dir)
                    
                    if os.path.exists(results_path) and os.listdir(results_path):
                        zip_path = os.path.join(temp_dir, "results.zip")
                        with zipfile.ZipFile(zip_path, 'w') as zipf:
                            for root, _, files in os.walk(results_path):
                                for file in files:
                                    zipf.write(os.path.join(root, file), 
                                               os.path.relpath(os.path.join(root, file), results_path))

                        with open(zip_path, "rb") as f:
                            st.download_button(
                                label="Download Results",
                                data=f,
                                file_name="results.zip",
                                mime="application/zip"
                            )
                        st.success("Processing complete! Click the button above to download your results.")
                    else:
                        st.error("No results were generated. Please check your images and try again.")
                except Exception as e:
                    st.error(f"An error occurred while processing the images: {str(e)}")
                    logging.error(f"Error in process_folder: {str(e)}", exc_info=True)

st.write("---")
st.write("Created with ❤️ using Streamlit and Google's Gemini API")