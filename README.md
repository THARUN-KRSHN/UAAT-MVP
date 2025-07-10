# UAAT – Understand, Analyze & Assist Tutor 🧠📚

**UAAT** is an AI-powered educational assistant that simplifies and explains handwritten notes using OCR and GPT-based logic. Students can choose between:

- ✏️ **Standard Mode** – Explains only the content on the uploaded page  
- 🌐 **Deep Mode** – Explains the content *plus* related external knowledge for a comprehensive learning experience

## 📁 Project Structure

UAAT-MVP/
├── frontend/ # React-based UI
├── backend/ # Flask-based backend API
│ ├── ai/ # GPT prompt logic (Standard + Deep Mode)
│ ├── ocr/ # OCR logic using Google Vision
│ ├── tts/ # Text-to-speech conversion
│ ├── avatar/ # (Optional) Avatar generation
│ └── main.py # Main Flask app
├── .gitignore
├── .env.example
└── README.md


---

## 👥 Team Members & Branches

| Member       | Role                      | Branch Name           |
|--------------|---------------------------|------------------------|
| **Tharun**   | Project Lead + AI Prompt Engineer | `ai-prompt-tharun`      |
| **Udhay**    | Frontend Developer        | `frontend-udhay`       |
| **Abhirami** | Backend API Developer     | `backend-abhirami`     |
| **Anjana**   | OCR + TTS Developer       | `ocr-media-anjana`     |

---

## 🚀 Development Workflow

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/UAAT-MVP.git
   cd UAAT-MVP
2. Create and Switch to Your Feature Branch
    git checkout -b your-branch-name
3. Work Inside Your Folder
    frontend/ → React app
    backend/ai/ → GPT logic
    backend/ocr/ → OCR logic
    backend/tts/ → Text-to-Speech
    backend/ → Flask API (main.py)
4. Commit Your Changes
    git add .
    git commit -m "✨ Added [your feature here]"
5. Push to GitHub
    git push origin your-branch-name
6. Create Pull Request
Go to GitHub → Click "Compare & Pull Request" → Assign reviewer → Merge to main once approved.
