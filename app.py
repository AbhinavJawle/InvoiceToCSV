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

with col_controls:
    st.subheader("1. Hochladen")
    
    uploaded_file = st.file_uploader("PDF oder Bild hier ablegen", type=['png', 'jpg', 'jpeg'], label_visibility="collapsed")
    if "use_sample" not in st.session_state:
        st.session_state.use_sample = False

    if st.button("📄 Beispielrechnung laden (Testmodus)"):
        st.session_state.use_sample = True
        
    active_file = None
    if uploaded_file:
        active_file = uploaded_file
        st.session_state.use_sample = False # Reset if user uploads manually
    elif st.session_state.use_sample:
        if os.path.exists("sample_invoice.png"): # Make sure this file exists!
            active_file = "sample_invoice.png"
            st.info("Beispielrechnung wird verwendet.")
        else:
            st.error("Beispieldatei 'sample_invoice.png' nicht im Ordner gefunden.")

    if active_file:
        if not st.session_state.use_sample:
             st.success("Datei geladen, bereit zur Extraktion.")
        
        if st.button("✨ Daten extrahieren", type="primary", use_container_width=True):
            
            
    

with col_preview:
    if active_file:
        st.subheader("Vorschau")
        if isinstance(active_file, str):
            image = Image.open(active_file)
        else:
            image = Image.open(active_file)
            
        st.image(image, use_container_width=True)
    else:
        st.info("👈 Lade eine Rechnung hoch oder klicke auf 'Beispiel laden', um die Vorschau zu sehen.")