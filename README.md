# LLM Projects

This repository contains **multiple projects built using Large Language Models (LLMs)**, including text-based and vision-enabled applications with Google Gemini API.  

---

## 🔹 Project Overview

### 1. Gemini Text Q&A
- A Streamlit application that allows users to ask questions and get answers from the Gemini LLM.
- Features:
  - Text input for prompts
  - Interactive responses
  - Uses `gemini-2.5-flash` model for text generation

### 2. Gemini Image Analysis
- A Streamlit application for analyzing images with optional prompts.
- Features:
  - Upload images in JPG, JPEG, PNG formats
  - Get descriptions or insights about images
  - Works with `gemini-2.5-flash-image` model
  - Supports optional user prompt for guided analysis

---

## ⚡ Technologies Used
- **Python 3.10+**
- **Streamlit** — for interactive UI
- **Pillow (PIL)** — for image handling
- **dotenv** — for managing API keys securely
- **Google Generative AI SDK** — for interacting with Gemini models

---

## 🔒 Environment Setup

1. Clone the repository:
```   
git clone https://github.com/Sushantm15/LLM-Projects.git
cd LLM-Projects
```
2.Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

3.Install dependencies:
```
pip install -r requirements.txt
```

4.Add your Gemini API key in a .env file:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

🚀 How to Run

*Text Q&A App*:
```
streamlit run app.py
```

*Image Analysis App*:
```
streamlit run vision.py
```
📁 Folder Structure
```
LLM-Projects/
│
├─ text_app.py           # Gemini Text Q&A project
├─ image_app.py          # Gemini Image Analysis project
├─ .env                  # API key (ignored by git)
├─ requirements.txt      # Python dependencies
└─ README.md             # Project documentation
```
👤 Author
```
Sushant More
GitHub: https://github.com/Sushantm15
```

📄 License

This project is licensed under the MIT License.
