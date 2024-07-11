import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def generate(input):
    if api_key:
        formatted_question = f"{input}"
        
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(formatted_question)
        
        
        content_parts = response.parts

        formatted_responses = []
        for part in content_parts:
            
            cleaned_text = part.text.replace('*', '')
            formatted_responses.append(cleaned_text)

        return ' '.join(formatted_responses)  
    else:
        return "API key is not configured properly."


st.title("SkyTrade AI - Air-rights encyclopedia ")
st.write("Provide the details of your legal case to get IPC suggestions and explanations.")

pre = "Consider the air rights questions below "
post = " suggest the answer and also what right is involved"

case_description = st.text_area("Explain your case here")

if st.button("Generate Suggestion"):
    if case_description:
        prompt = pre + case_description + post
        gen = generate(prompt)
        st.write("### Suggested IPCs and Explanation")
        st.write(gen)
    else:
        st.write("Please enter the details of your case.")
