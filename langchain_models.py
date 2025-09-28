
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

st.title("Translate text to English")
language = "English"
result = ""
user_input = st.text_area("Enter text to translate:")
language = st.text_input("Enter language to translate to:")
if st.button("Translate"):
    model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")   
    result = model.invoke(user_input+"\n Translate it in "+language)
    st.write(result.content)
    st.write("\n\n\nSummarized text:")
    result = model.invoke(result.content+"\n Summarize it")
    st.write(result.content)
