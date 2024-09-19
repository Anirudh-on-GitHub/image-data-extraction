# Image Data Extraction App

## Overview

This **Image Data Extraction App** allows users to upload image files containing tabular data, such as forms or tables, and extracts the data into a structured CSV format using **Google's Gemini API**.

Whether you want to use the app online via **Streamlit** or run it locally on your own machine, this README will guide you through both methods.

---

## Features

- Upload multiple image files simultaneously (PNG, JPG, JPEG).
- Extract tabular data from images using Google Gemini API.
- Convert extracted data to CSV format for download.
- Easy-to-use interface built with **Streamlit**.
- Configurable API key handling to ensure security.

---

## Deployment Options

### Option 1: Use on Streamlit (Hosted Version)

You can use the app directly via the Streamlit link below:

[Streamlit App Link](https://tablevision.streamlit.app/) 

### Option 2: Run Locally

You can also clone the project and run the app on your own machine. Below are the steps for setting it up.

---

## Getting Started (Local Deployment)

### Prerequisites

- **Python 3.8+**
- **Streamlit**
- **Google's Gemini API Access** (requires an API key)
  
### Installation

1. **Clone the repository**
2. **Create a virtual environment**
3. **Install the required dependencices**
   ``` pip install -r requirements.txt```
4. **Set up the environment variable:**
   Create a .env file in the root directory and add your Google Gemini API Key
   ``` GOOGLE_API_KEY=your_api_key_here ```
5. **Run the streamlit app**
   ``` streamlit run app.py```
   The app will open in your web browser at http://localhost:8501

## Using the App
### On Streamlit
- Simply open the Streamlit App and follow the instructions to upload your image files.
- After processing, you can download the results in a ZIP archive containing the CSV files.
  
### Locally
- After running the app locally, follow the same steps as in the Streamlit version: upload images, process, and download results.

## API Configuration and Security
To ensure the security of your Google API key, the key is stored in a .env file, which is never exposed in the code. You need to make sure that the .env file is listed in .gitignore to prevent it from being committed to the repository.
