# Gemini Broski 🤖✨

A personal AI chatbot powered by the Gemini API, built with Python and Flask. (very basic version)

Chat with it on your PC or phone through a clean mobile-style UI.

## How it works 🧠
- **Frontend**: HTML/CSS/JS served by Flask
- **Backend**: Python + Flask
- **AI**: Google Gemini API

## Setup 🛠️

1. Clone the repo
2. Install dependencies: `pip install google-genai flask flask-cors`
3. Create `apikey.txt` in the project folder and paste your Gemini API key inside
4. Run the server: `python ui.py`
5. Open `http://127.0.0.1:5000` in your browser

## Access on phone 📱
Make sure your phone is on the same WiFi as your PC, then open `http://YOUR_PC_IP:5000` in your phone browser.

## Notes 📝
- Free tier Gemini API has daily request limits
- `apikey.txt` is in `.gitignore` — never share your key
