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
        st.session_state.use_sample = False 
    elif st.session_state.use_sample:
        if os.path.exists("sample_invoice.png"): 
            active_file = "sample_invoice.png"
            st.info("Beispielrechnung wird verwendet.")
        else:
            st.error("Beispieldatei 'sample_invoice.png' nicht im Ordner gefunden.")

    if active_file:
        if not st.session_state.use_sample:
             st.success("Datei geladen, bereit zur Extraktion.")
        
        if st.button("✨ Daten extrahieren", type="primary", use_container_width=True):
            
            with st.spinner("KI liest das Dokument..."):
                try:
                    if isinstance(active_file, str):
                        image = Image.open(active_file)
                    else:
                        image = Image.open(active_file)

                    try:
                        model = genai.GenerativeModel('models/gemini-flash-latest')
                    except:
                        model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

                    prompt = """
                    Extract invoice line items into JSON. Detect the currency symbol (e.g. $, €, ₹).
                    Output format:
                    {
                        "vendor": "string",
                        "date": "string",
                        "currency_symbol": "string",
                        "items": [
                            {"description": "string", "quantity": int, "price": float, "total": float}
                        ]
                    }
                    """
                    
                    response = model.generate_content(
                        [prompt, image],
                        generation_config={"response_mime_type": "application/json"}
                    )
                    
                    data = json.loads(response.text)
                    items = data.get("items", [])
                    vendor = data.get("vendor", "Unbekannt")
                    currency = data.get("currency_symbol", "")
                    inv_date = data.get("date", "Unbekannt")

                    st.divider()
                    st.subheader("2. Extrahierte Daten")
                    
                    c1, c2 = st.columns(2)
                    c1.info(f"**Lieferant:** {vendor}")
                    c2.info(f"**Datum:** {inv_date}")

                    if items:
                        df = pd.DataFrame(items)
                        
                        df_display = df.copy()
                        df_display['price'] = df_display['price'].apply(lambda x: f"{currency}{x:.2f}")
                        df_display['total'] = df_display['total'].apply(lambda x: f"{currency}{x:.2f}")

                        df_display = df_display.rename(columns={
                            "description": "Beschreibung",
                            "quantity": "Menge",
                            "price": "Einzelpreis",
                            "total": "Gesamt"
                        })

                        st.dataframe(df_display, use_container_width=True, hide_index=True)
                        
                        df['currency'] = currency 
                        df_csv = df.rename(columns={
                            "description": "Beschreibung",
                            "quantity": "Menge",
                            "price": "Einzelpreis",
                            "total": "Gesamt",
                            "currency": "Währung"
                        })
                        
                        csv = df_csv.to_csv(index=False).encode('utf-8')
                        
                        st.download_button(
                            label="📥 Als CSV herunterladen",
                            data=csv,
                            file_name=f"{vendor}_daten.csv",
                            mime="text/csv",
                            use_container_width=True
                        )
                    else:
                        st.warning("Keine Positionen gefunden.")
                        
                except Exception as e:
                    st.error(f"Fehler: {e}")
    

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