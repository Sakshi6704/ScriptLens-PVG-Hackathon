import streamlit as st

st.title("🏠 Home")

st.markdown("""
Welcome to **OCR & Text Summarizer App**!

This app lets you:
- 📷 Extract text from **images** or **PDFs**
- 🧠 Summarize long content automatically
- 💬 Save time reading lengthy documents
""")

st.divider()
st.subheader("Navigate")

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/2_Summarize.py", label="🧠 Go to Summarizer", icon="📝")

with col2:
    st.page_link("pages/3_About.py", label="ℹ️ Learn About App", icon="📘")
