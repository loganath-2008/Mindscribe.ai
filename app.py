import streamlit as st
import ollama

# 1. Simple Page Title
st.set_page_config(page_title="MindScribe AI", layout="wide")
st.title("📝 MindScribe AI")
st.write("Simplify notes and generate practice quizzes instantly.")

# 2. Text Input Box
user_notes = st.text_area("Paste lecture notes here:", height=200)

col1, col2 = st.columns(2)

# 3. Summary Feature
with col1:
    if st.button("✨ Simplify Notes", use_container_width=True):
        if not user_notes.strip():
            st.warning("Please paste some notes first!")
        else:
            with st.spinner("Simplifying..."):
                res = ollama.chat(model='gemma3:1b', messages=[
                    {'role': 'user', 'content': f"Simplify these notes into clear bullet points and bold key terms:\n\n{user_notes}"}
                ])
                st.success("### 📖 Summary")
                st.write(res['message']['content'])

# 4. MCQ Feature
with col2:
    if st.button("🧠 Generate Quiz", use_container_width=True):
        if not user_notes.strip():
            st.warning("Please paste some notes first!")
        else:
            with st.spinner("Generating quiz..."):
                res = ollama.chat(model='gemma3:1b', messages=[
                    {'role': 'user', 'content': f"Generate 3 MCQs with options A,B,C,D based on this text. List answers at the bottom:\n\n{user_notes}"}
                ])
                st.success("### 📝 Practice Quiz")
                st.write(res['message']['content'])