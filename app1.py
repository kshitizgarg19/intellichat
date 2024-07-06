from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama  # Adjust import if the class name is different
import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image

# Load environment variables from .env file
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Define prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question: {question}")
])

# Streamlit setup
st.set_page_config(page_title="IntelliChat", page_icon=":robot_face:", layout="wide")
st.title("IntelliChat")
st.write("Welcome to IntelliChat, your intelligent assistant powered by llama and LangChain.")

# Input area
input_text = st.text_input("Enter a topic or question:")

# LLaMA3 setup
llm = Ollama(model="llama3")  # Instantiate the correct class
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Perform interaction if input is provided
if input_text:
    st.write(chain.invoke({"question": input_text}))

# Sidebar with additional info and styling
st.sidebar.title("About This Project")
st.sidebar.info("""
- This project is built using **llama** and **LangChain**.
- It aims to provide intelligent responses to user queries using advanced large language models.
""")

# Social media links with icons
st.sidebar.markdown("### Connect with me:")
col1, col2 = st.sidebar.columns([1, 6])
with col1:
    st.image("https://img.icons8.com/fluent/48/000000/linkedin.png", width=30)
with col2:
    st.markdown("[LinkedIn](https://www.linkedin.com/in/kshitiz-garg-898403207/)")
col1, col2 = st.sidebar.columns([1, 6])
with col1:
    st.image("https://img.icons8.com/fluent/48/000000/github.png", width=30)
with col2:
    st.markdown("[GitHub](https://github.com/kshitizgarg19)")

# Footer with developer info
st.markdown("""
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            color: black;
            text-align: center;
            padding: 10px;
        }
        .footer a {
            text-decoration: none;
        }
    </style>
    <div class="footer">
        Developed and maintained by <a href="https://www.linkedin.com/in/kshitiz-garg-898403207/" target="_blank">Kshitiz Garg</a>. 
        
    </div>
    """, unsafe_allow_html=True)