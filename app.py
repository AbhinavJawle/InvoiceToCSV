import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import json
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="InvoiceToCSV", page_icon="⚡", layout="wide")

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("❌ API-Key fehlt! Bitte überprüfe deine .env Datei.")
    st.stop()

st.title("⚡ InvoiceToCSV")
st.markdown("Extrahiere strukturierte Daten aus Rechnungen in Sekunden.")
st.markdown("---")

col_controls, col_preview = st.columns([1, 1], gap="medium")

