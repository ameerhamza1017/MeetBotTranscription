# 🤖 Google Meet Bot – Auto Join, Record & Transcribe

This Python bot automates joining Google Meet sessions, records system audio, and transcribes the conversation into text.  
It’s designed for **professionals, students, and teams** who need to archive or analyze meeting discussions efficiently.

---

## ✨ Features

- 🔐 **Auto Login** – Logs into Google using provided credentials.  
- 📞 **Auto Join Meet** – Joins the specified Google Meet link as a logged-in user or guest.  
- 🎙 **System Audio Recording** – Captures all meeting audio using FFmpeg and VB-Audio Virtual Cable.  
- 📝 **Speech-to-Text Transcription** – Transcribes recorded audio with OpenAI Whisper for highly accurate results.  
- 💾 **Output Files** – Saves audio as `meeting_audio.wav` and optionally saves transcription as `meeting_transcript.txt`.  
- 🛡 **Privacy First** – Turns off microphone and camera before joining.  

---

## 🛠 Tech Stack

| Technology               | Purpose                       |
|--------------------------|---------------------------------|
| **Python 3.11+**         | Core programming language      |
| **Selenium + UCDriver**  | Automate browser actions       |
| **FFmpeg**               | Record system audio            |
| **OpenAI Whisper**       | Transcribe audio to text       |
| **VB-Audio Virtual Cable** | Route system audio (Windows) |

---

## 📂 Outputs

- 🎧 **Audio Recording**: `meeting_audio.wav`  
- 📜 **Transcription (optional)**: `meeting_transcript.txt`  
- 📄 **Real-time printed transcript** in terminal  

---

## 🚀 How It Works

1. 🎙 Starts FFmpeg to record system audio.  
2. 🌐 Launches Chrome (via undetected-chromedriver).  
3. 🔐 Logs into Google and joins the specified Meet link.  
4. 🎧 Records the full meeting audio.  
5. 📝 Transcribes the recording using OpenAI Whisper.  
6. 💾 Saves and prints the transcription.  

---

## ⚡ Requirements

- ✅ Python 3.9+  
- ✅ FFmpeg installed and added to PATH  
- ✅ VB-Audio Virtual Cable (for system audio capture on Windows)  
- ✅ OpenAI Whisper (`pip install openai-whisper`)  
