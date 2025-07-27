Follow these steps to set up the AI Meeting Intelligence Platform:

1. Clone the repository and navigate into the project folder.
2. Create and activate a Python virtual environment in `backend/`:
   python -m venv venv
   venv\Scripts\activate  (on Windows)
3. Install FastAPI dependencies:
   pip install fastapi uvicorn requests python-multipart
4. Download and build whisper.cpp:
   - Clone whisper.cpp into `backend/whisper.cpp`
   - Run CMake build for whisper-cli.exe in Release mode
5. Place the Whisper model (`ggml-base.en.bin`) in `backend/whisper.cpp/models/`
6. Install FFmpeg and configure its path (e.g., C:\ffmpeg\ffmpeg.exe)
7. Start the FastAPI server from backend:
   uvicorn main:app --reload
8. Frontend setup (Vite + React):
   cd frontend
   npm install
   npm run dev
9. Ensure Ollama is installed and running:
   ollama serve
   ollama pull llama3
