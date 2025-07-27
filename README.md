# 🤖 Gemini Pro Chat

**Gemini Pro Chat** is an AI-powered chatbot interface built with **Google’s Gemini API** and **Streamlit**, capable of responding to text and image prompts using large language models like Gemini 1.5 Flash and Gemini Pro Vision. It features a sleek UI with chat history, model selection, image uploads, and more.

![Screenshot](Screenshot%202025-07-27%20154923.png)

---

## 🚀 Features

- 🧠 Text-based chatting using Gemini 1.5 Flash  
- 🖼️ Image prompt support with Gemini Pro Vision  
- 📋 Persistent Chat History with clickable summaries  
- 🧪 Model selection (Gemini 1.5 Flash, Pro, Ultra)  
- 🧰 Beautiful UI with custom CSS styling  
- 🌐 Powered by Google Generative AI via `google.generativeai`  

---

## 🧪 Tech Stack

### 💻 Frontend
- **Streamlit** for UI
- **Custom CSS** (inside Python) for layout and style
- **Markdown** and **HTML** for chat bubble rendering

### 🧠 Backend
- **Python**
- **Gemini API (Google Generative AI)** via `google.generativeai`
- **LangChain / Gemini SDK**
- **Pillow (PIL)** for image processing

---

## 📁 Project Structure
- Gemini-Pro-Chat/
- ├── app.py # Main Streamlit application
- ├── Screenshot 2025-07-27 154923.png # UI Screenshot for README
- ├── requirements.txt # Python dependencies
- └── README.md # Project documentation


---

## 💡 How to Use

### 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Gemini-Pro-Chat.git
   cd Gemini-Pro-Chat

---

## 🤖 How It Works
- User types a message and optionally uploads an image
- The selected Gemini model responds with a smart reply
- Gemini Pro Vision handles images with prompts
- Chat history is maintained using Streamlit session state
- All responses are rendered beautifully using Markdown & custom HTML

## 🔮 Future Improvements
- 🗂️ Chat history export/download
- 💬 Voice-to-text input
- 🌍 Multilingual support
- ☁️ Deployment on Streamlit Cloud or Render

## 🙌 Acknowledgements
- 🤖 Google Gemini API
- 🎨 Streamlit for the front-end
- 🧑‍🏫 Mr. Lokesh Sir for continuous support

---