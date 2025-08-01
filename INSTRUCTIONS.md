# Instructions to Run Locally 🚀

## Prerequisites
- Python 3.8 or higher
- Git

## Setup Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jain-anshika/Capston-Gemini-ChatBot.git
   cd Capston-Gemini-ChatBot
   ```

2. **Create and Activate Virtual Environment** (Optional but Recommended)
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/MacOS
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables**
   - Copy `.env.example` to create a new `.env` file
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Add your API key to the `.env` file

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

6. **Access the Application**
   - Open your browser and go to http://localhost:8501
   - The chat interface should now be visible and ready to use

## Troubleshooting

1. **API Key Issues**
   - Make sure you have copied your API key correctly
   - Ensure there are no spaces before or after the API key in the .env file

2. **Package Installation Issues**
   - Try upgrading pip: `python -m pip install --upgrade pip`
   - Install packages one by one if there are conflicts

3. **Port Already in Use**
   - If port 8501 is busy, Streamlit will automatically try the next available port
   - Check your terminal for the correct URL

## Security Notes
- Never commit your `.env` file
- Keep your API key secret and don't share it
- Regularly rotate your API key if possible
