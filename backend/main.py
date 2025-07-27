# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# import os

# app = FastAPI()

# # Allow frontend (React) to talk to this backend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],  # React dev server
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Upload directory
# UPLOAD_DIR = "uploaded_files"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     file_location = os.path.join(UPLOAD_DIR, file.filename)
#     with open(file_location, "wb") as f:
#         content = await file.read()
#         f.write(content)

#     return {"message": f"{file.filename} uploaded successfully!"}


# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# import os
# import shutil
# import subprocess

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# UPLOAD_DIR = "backend/uploaded_files"
# WHISPER_PATH = "backend/whisper.cpp/main"  # or main.exe on Windows
# MODEL_PATH = "backend/whisper.cpp/models/ggml-base.en.bin"

# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     file_location = os.path.join(UPLOAD_DIR, file.filename)
    
#     with open(file_location, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     return {"message": f"File '{file.filename}' uploaded successfully!"}

# @app.get("/transcribe/{filename}")
# def transcribe(filename: str):
#     file_path = os.path.join(UPLOAD_DIR, filename)

#     if not os.path.exists(file_path):
#         return {"error": "File not found."}

#     command = [
#         WHISPER_PATH,
#         "-m", MODEL_PATH,
#         "-f", file_path,
#         "-otxt"
#     ]

#     try:
#         subprocess.run(command, check=True)
#         transcript_file = file_path + ".txt"

#         with open(transcript_file, "r") as f:
#             transcript = f.read()

#         return {"transcript": transcript}

#     except subprocess.CalledProcessError as e:
#         return {"error": "Transcription failed", "details": str(e)}


# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# import os
# import shutil
# import subprocess

# app = FastAPI()

# # CORS: Allow frontend at localhost:5173 (Vite)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === PATH CONFIGURATION ===
# UPLOAD_DIR = os.path.join("backend", "uploaded_files")
# WHISPER_BIN = os.path.join("backend", "whisper.cpp", "main.exe")  # Windows compiled binary
# MODEL_PATH = os.path.join("backend", "whisper.cpp", "models", "ggml-base.en.bin")

# # === ROUTE: Upload File ===
# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure folder exists
#     file_location = os.path.join(UPLOAD_DIR, file.filename)

#     with open(file_location, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     return {"message": f"File '{file.filename}' uploaded successfully!"}

# # === ROUTE: Transcribe File ===
# @app.get("/transcribe/{filename}")
# def transcribe(filename: str):
#     file_path = os.path.join(UPLOAD_DIR, filename)

#     if not os.path.exists(file_path):
#         return {"error": f"File '{filename}' not found."}

#     # Command to run whisper.cpp transcription
#     command = [
#         WHISPER_BIN,
#         "-m", MODEL_PATH,
#         "-f", file_path,
#         "-otxt"
#     ]

#     try:
#         subprocess.run(command, check=True)

#         # Output transcript will be: <filename>.txt
#         transcript_path = file_path + ".txt"

#         if os.path.exists(transcript_path):
#             with open(transcript_path, "r", encoding="utf-8") as f:
#                 transcript = f.read()
#             return {"transcript": transcript}
#         else:
#             return {"error": "Transcription output file not found."}

#     except subprocess.CalledProcessError as e:
#         return {"error": "Transcription failed", "details": str(e)}

# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# import os
# import shutil
# import subprocess

# app = FastAPI()

# # === CORS ===
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === PATH CONFIGURATION ===
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# UPLOAD_DIR = os.path.join(BASE_DIR, "uploaded_files")
# WHISPER_BIN = os.path.join(BASE_DIR, "whisper.cpp", "main.exe")  # Windows
# MODEL_PATH = os.path.join(BASE_DIR, "whisper.cpp", "models", "ggml-base.en.bin")

# # === ROUTE: Upload File ===
# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     os.makedirs(UPLOAD_DIR, exist_ok=True)
#     file_location = os.path.join(UPLOAD_DIR, file.filename)

#     with open(file_location, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     return {"message": f"File '{file.filename}' uploaded successfully!"}

# # === ROUTE: Transcribe File ===
# @app.get("/transcribe/{filename}")
# def transcribe(filename: str):
#     file_path = os.path.join(UPLOAD_DIR, filename)
#     print("Resolved file path:", file_path)  # ✅ Debug print

#     if not os.path.exists(file_path):
#         return {"error": f"File '{filename}' not found."}

#     command = [
#         WHISPER_BIN,
#         "-m", MODEL_PATH,
#         "-f", file_path,
#         "-otxt"
#     ]

#     try:
#         subprocess.run(command, check=True)

#         transcript_path = file_path + ".txt"

#         if os.path.exists(transcript_path):
#             with open(transcript_path, "r", encoding="utf-8") as f:
#                 transcript = f.read()
#             return {"transcript": transcript}
#         else:
#             return {"error": "Transcription output file not found."}

#     except subprocess.CalledProcessError as e:
#         return {"error": "Transcription failed", "details": str(e)}


# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# import os
# import subprocess
# import requests

# app = FastAPI()

# # === CORS CONFIG ===
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],  # Vite dev server
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === PATH CONFIGURATION ===
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# UPLOAD_DIR = os.path.join(BASE_DIR, "uploaded_files")
# # WHISPER_BIN = os.path.join("backend", "whisper.cpp", "build", "bin", "Release", "main.exe")  # compiled binary
# WHISPER_BIN = r"F:\Prasaath\01_New_Learnings\ai-meeting-platform\backend\whisper.cpp\build\bin\Release\whisper-cli.exe"
# MODEL_PATH = os.path.join(BASE_DIR, "whisper.cpp", "models", "ggml-base.en.bin")

# # Ensure upload folder exists
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# # === ROUTE: Upload File ===
# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     file_location = os.path.join(UPLOAD_DIR, file.filename)

#     with open(file_location, "wb") as f:
#         content = await file.read()
#         f.write(content)

#     return {"message": f"{file.filename} uploaded successfully!"}

# @app.get("/transcribe/{filename}")
# def transcribe(filename: str):
#     file_path = os.path.join(UPLOAD_DIR, filename)
#     print(f"Input file path: {file_path}")

#     if not os.path.exists(file_path):
#         return {"error": f"File '{filename}' not found."}

#     # === Handle .mp4 input by converting to .mp3 ===
#     ext = os.path.splitext(filename)[1].lower()
#     if ext == ".mp4":
#         mp3_path = file_path.rsplit(".", 1)[0] + ".mp3"
#         ffmpeg_path = r"C:\ffmpeg\ffmpeg.exe"
#         ffmpeg_command = [ffmpeg_path, "-y", "-i", file_path, "-vn", "-ar", "16000", "-ac", "1", "-b:a", "128k", mp3_path]
#         try:
#             subprocess.run(ffmpeg_command, check=True)
#             file_path = mp3_path  # update path to transcribe the .mp3
#         except subprocess.CalledProcessError as e:
#             return {"error": "Audio extraction failed", "details": str(e)}

#     # === Transcribe with whisper.cpp ===
#     command = [
#         WHISPER_BIN,
#         "-m", MODEL_PATH,
#         "-f", file_path,
#         "-otxt"
#     ]

#     try:
#         subprocess.run(command, check=True)

#         transcript_path = file_path + ".txt"
#         if os.path.exists(transcript_path):
#             with open(transcript_path, "r", encoding="utf-8") as f:
#                 transcript = f.read()
#             return {"transcript": transcript}
#         else:
#             return {"error": "Transcription output not found."}

#     except subprocess.CalledProcessError as e:
#         return {"error": "Transcription failed", "details": str(e)}


# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# import os
# import subprocess
# import requests

# app = FastAPI()

# # === CORS CONFIG ===
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],  # Vite dev server
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === PATH CONFIGURATION ===
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# UPLOAD_DIR = os.path.join(BASE_DIR, "uploaded_files")
# WHISPER_BIN = r"F:\Prasaath\01_New_Learnings\ai-meeting-platform\backend\whisper.cpp\build\bin\Release\whisper-cli.exe"
# MODEL_PATH = os.path.join(BASE_DIR, "whisper.cpp", "models", "ggml-base.en.bin")
# FFMPEG_PATH = r"C:\ffmpeg\ffmpeg.exe"

# # Ensure upload folder exists
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# # === ROUTE: Upload File ===
# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     file_location = os.path.join(UPLOAD_DIR, file.filename)

#     with open(file_location, "wb") as f:
#         content = await file.read()
#         f.write(content)

#     return {"message": f"{file.filename} uploaded successfully!"}

# # === ROUTE: Transcribe File ===
# @app.get("/transcribe/{filename}")
# def transcribe(filename: str):
#     file_path = os.path.join(UPLOAD_DIR, filename)
#     print(f"Input file path: {file_path}")

#     if not os.path.exists(file_path):
#         return {"error": f"File '{filename}' not found."}

#     # === Convert .mp4 to .mp3 ===
#     ext = os.path.splitext(filename)[1].lower()
#     if ext == ".mp4":
#         mp3_path = file_path.rsplit(".", 1)[0] + ".mp3"
#         ffmpeg_command = [
#             FFMPEG_PATH, "-y",
#             "-i", file_path,
#             "-vn", "-ar", "16000", "-ac", "1", "-b:a", "128k",
#             mp3_path
#         ]
#         try:
#             subprocess.run(ffmpeg_command, check=True)
#             file_path = mp3_path  # Use extracted audio
#         except subprocess.CalledProcessError as e:
#             return {"error": "Audio extraction failed", "details": str(e)}

#     # === Run whisper.cpp ===
#     command = [
#         WHISPER_BIN,
#         "-m", MODEL_PATH,
#         "-f", file_path,
#         "-otxt"
#     ]

#     try:
#         subprocess.run(command, check=True)
#         transcript_path = file_path + ".txt"

#         if os.path.exists(transcript_path):
#             with open(transcript_path, "r", encoding="utf-8") as f:
#                 transcript = f.read()
#             return {"transcript": transcript}
#         else:
#             return {"error": "Transcription output not found."}

#     except subprocess.CalledProcessError as e:
#         return {"error": "Transcription failed", "details": str(e)}

# # === ROUTE: Insight Extraction via Ollama ===
# @app.post("/extract_insights")
# async def extract_insights(data: dict):
#     transcript = data.get("transcript")
#     if not transcript:
#         return {"error": "Transcript not provided."}

#     prompt = f"""
#     Given this meeting transcript, extract the following:
#     1. A brief summary.
#     2. Key discussion points.
#     3. Action items with responsible people (if any).
    
#     Transcript:
#     {transcript}
#     """

#     try:
#         response = requests.post(
#             "http://localhost:11434/api/generate",
#             json={
#                 "model": "llama3",  # Adjust model name if needed
#                 "prompt": prompt,
#                 "stream": False
#             }
#         )
#         response.raise_for_status()
#         result = response.json()
#         return {"insights": result.get("response", "No insights generated.")}
#     except Exception as e:
#         return {"error": "Insight extraction failed", "details": str(e)}


from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
import subprocess
import requests

app = FastAPI()

# === CORS CONFIG ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === PATH CONFIGURATION ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploaded_files")
WHISPER_BIN = r"F:\Prasaath\01_New_Learnings\ai-meeting-platform\backend\whisper.cpp\build\bin\Release\whisper-cli.exe"
MODEL_PATH = os.path.join(BASE_DIR, "whisper.cpp", "models", "ggml-base.en.bin")
FFMPEG_PATH = r"C:\ffmpeg\ffmpeg.exe"

# Ensure upload folder exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

# === ROUTE: Upload File ===
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_location, "wb") as f:
        content = await file.read()
        f.write(content)

    return {"message": f"{file.filename} uploaded successfully!"}

# === ROUTE: Transcribe File ===
@app.get("/transcribe/{filename}")
def transcribe(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    print(f"Input file path: {file_path}")

    if not os.path.exists(file_path):
        return {"error": f"File '{filename}' not found."}

    # === Convert .mp4 to .mp3 ===
    ext = os.path.splitext(filename)[1].lower()
    if ext == ".mp4":
        mp3_path = file_path.rsplit(".", 1)[0] + ".mp3"
        ffmpeg_command = [
            FFMPEG_PATH, "-y",
            "-i", file_path,
            "-vn", "-ar", "16000", "-ac", "1", "-b:a", "128k",
            mp3_path
        ]
        try:
            subprocess.run(ffmpeg_command, check=True)
            file_path = mp3_path  # Use extracted audio
        except subprocess.CalledProcessError as e:
            return {"error": "Audio extraction failed", "details": str(e)}

    # === Run whisper.cpp ===
    command = [
        WHISPER_BIN,
        "-m", MODEL_PATH,
        "-f", file_path,
        "-otxt"
    ]

    try:
        subprocess.run(command, check=True)
        transcript_path = file_path + ".txt"

        if os.path.exists(transcript_path):
            with open(transcript_path, "r", encoding="utf-8") as f:
                transcript = f.read()
            return {"transcript": transcript}
        else:
            return {"error": "Transcription output not found."}

    except subprocess.CalledProcessError as e:
        return {"error": "Transcription failed", "details": str(e)}

# === ROUTE: Insight Extraction via Ollama ===
@app.post("/extract_insights")
async def extract_insights(data: dict):
    transcript = data.get("transcript")
    if not transcript:
        return {"error": "Transcript not provided."}

    prompt = f"""
    Given this meeting transcript, extract the following:
    1. A brief summary.
    2. Key discussion points.
    3. Action items with responsible people (if any).
    
    Transcript:
    {transcript}
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        result = response.json()
        return {"insights": result.get("response", "No insights generated.")}
    except Exception as e:
        return {"error": "Insight extraction failed", "details": str(e)}
