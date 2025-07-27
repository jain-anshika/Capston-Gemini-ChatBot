import streamlit as st
from PIL import Image
import google.generativeai as genai
import os
from streamlit_chat import message
from datetime import datetime
import time

# Configure the page
st.set_page_config(
    page_title="Gemini Pro Chat",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Gemini API
def configure_gemini():
    os.environ['GOOGLE_API_KEY'] = "AIzaSyDuAM0UE9hd1unNr4ucOQqaVfHVdvspgws"
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Text generation function
def send_text_request(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    response = model.generate_content(prompt)
    return response.text

# Image analysis function
def image_analysis_request(image, prompt=None):
    model = genai.GenerativeModel("gemini-pro-vision")
    if prompt is None:
        prompt = "Analyze this image"
    response = model.generate_content([prompt, image])
    return response.text

# Initialize the app
def main():
    configure_gemini()
    
    # Custom CSS
    st.markdown("""
    <style>
        /* Main container */
        .main {
            background-color: #f5f5f5;
        }
        
        /* Chat container */
        .chat-container {
            height: calc(100vh - 200px);
            overflow-y: auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        /* User message */
        .user-message {
            background-color: #e3f2fd;
            padding: 12px 16px;
            border-radius: 18px 18px 0 18px;
            margin: 8px 0;
            max-width: 80%;
            margin-left: auto;
        }
        
        /* Bot message */
        .bot-message {
            background-color: #f1f1f1;
            padding: 12px 16px;
            border-radius: 18px 18px 18px 0;
            margin: 8px 0;
            max-width: 80%;
            margin-right: auto;
        }
        
        /* Input area */
        .stTextInput>div>div>input {
            border-radius: 20px;
            padding: 12px 16px;
        }
        
        /* Sidebar */
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Sidebar
    with st.sidebar:
        st.title("Chat Settings")
        st.markdown("---")
        
        # Model selection
        model_name = st.selectbox(
            "Select Model",
            ["Gemini 1.5 Flash", "Gemini Pro", "Gemini Ultra"],
            index=0
        )
        
        st.markdown("---")
        st.markdown("### Chat History")
        
        # Display conversation history
        for i, msg in enumerate(st.session_state.messages):
            if msg["role"] == "user":
                st.button(
                    f"🗨️ {msg['content'][:30]}...",
                    key=f"hist_{i}",
                    on_click=None,
                    help=msg["content"]
                )
        
        st.markdown("---")
        st.markdown("Created with [Gemini API](https://ai.google.dev/)")
    
    # Main chat area
    st.title("🤖 Gemini Pro Chat")
    st.caption("Powered by Google's Gemini AI")
    
    # Chat container
    chat_container = st.container()
    
    # Display chat messages
    with chat_container:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(
                    f'<div class="user-message">👤 {msg["content"]}</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f'<div class="bot-message">🤖 {msg["content"]}</div>',
                    unsafe_allow_html=True
                )
    
    # Input area at bottom
    with st.form("chat_input", clear_on_submit=True):
        col1, col2 = st.columns([6, 1])
        
        with col1:
            user_input = st.text_input(
                "Type your message...",
                key="input",
                label_visibility="collapsed"
            )
        
        with col2:
            submitted = st.form_submit_button("Send", use_container_width=True)
        
        # Image upload in form
        uploaded_file = st.file_uploader(
            "Attach image",
            type=["jpg", "jpeg", "png"],
            label_visibility="collapsed"
        )
    
    # Handle user input
    if submitted and user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Display user message immediately
        with chat_container:
            st.markdown(
                f'<div class="user-message">👤 {user_input}</div>',
                unsafe_allow_html=True
            )
        
        # Get AI response
        with st.spinner("Gemini is thinking..."):
            try:
                if uploaded_file is not None:
                    image = Image.open(uploaded_file)
                    response = image_analysis_request(image, user_input)
                    
                    # Display image
                    with chat_container:
                        st.image(image, caption="Uploaded Image", width=300)
                else:
                    response = send_text_request(user_input)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
                
                # Display assistant response
                with chat_container:
                    st.markdown(
                        f'<div class="bot-message">🤖 {response}</div>',
                        unsafe_allow_html=True
                    )
                
                # Auto-scroll to bottom
                st.markdown(
                    "<script>window.scrollTo(0, document.body.scrollHeight);</script>",
                    unsafe_allow_html=True
                )
            
            except Exception as e:
                error_msg = f"Sorry, I encountered an error: {str(e)}"
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
                with chat_container:
                    st.markdown(
                        f'<div class="bot-message">⚠️ {error_msg}</div>',
                        unsafe_allow_html=True
                    )

if __name__ == "__main__":
    main()