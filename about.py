import streamlit as st

st.title("ℹ️ About This App")

st.markdown("""
**Version:** 1.0  
**Developer:** Sakshi  

### 🧩 How It Works
1. The app uses **Tesseract OCR** to extract text from images or PDFs.  
2. It summarizes text using **NLTK** for concise results.  

### 🧠 Future Plans
- Add transformer-based summarization (BART, T5)
- Multi-language support
- Export to PDF or text files

---
Made with ❤️ using **Python**, **OpenCV**, **NLTK**, and **Streamlit**.
""")

st.divider()
st.subheader("Navigate")

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/1_Home.py", label="🏠 Home", icon="🏡")

with col2:
    st.page_link("pages/2_Summarize.py", label="🧠 Summarize", icon="📝")
