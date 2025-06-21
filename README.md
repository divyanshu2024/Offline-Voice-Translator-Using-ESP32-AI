# 🌐 Offline Voice Translator Using ESP32 & AI – Practical Speech Solution

An edge AI solution designed to **bridge language gaps** in low-connectivity areas. This device translates spoken input into another language and speaks it aloud — **completely offline**.

---

## 🧠 Overview

In many rural and network-limited regions, communicating across languages is a challenge. This project introduces a **portable, real-time speech translation system** built on ESP32 and open-source AI tools, capable of translating **English ↔ Hindi ↔ Telugu** without the internet.

---

## 💡 Key Highlights

- ✨ End-to-end translation: STT → Translate → TTS
- 📶 Fully offline using local Flask server
- 💬 Multi-language support with plug-and-play architecture
- 🧩 Compact hardware setup with ESP32, mic, DAC, and speaker

---

## 🔧 Core Technologies

| Layer        | Tool/Component               |
|-------------|------------------------------|
| Microcontroller | ESP32 (MicroPython)         |
| Mic          | INMP441 (I2S Digital)        |
| DAC + Audio  | MAX98357A with 3W speaker    |
| STT Engine   | Vosk (offline)               |
| Translator   | Argos Translate              |
| TTS Engine   | pyttsx3                      |
| Backend      | Flask (Python server)        |

---

## 📁 Resources & Files

All reports, paper, and presentation files are in the [`Documentation/`](./Documentation/) folder.

| 📄 Type              | 📎 File Link |
|----------------------|-------------|
| Detailed Report      | [PROJECT_REPORT[1].docx](./Documentation/PROJECT_REPORT%5B1%5D.docx) |
| Research Write-up    | [ResearchPaper-Team-11.docx](./Documentation/ResearchPaper-Team-11.docx) |
| Presentation Poster  | [aiot poster 2.pptx](./Documentation/aiot%20poster%202.pptx) |
| Final Slide Deck     | [PPT Presentation-(Team-11).pptx](./Documentation/PPT%20Presentation-(Team-11).pptx) |

---

## 🛠️ Setup Diagram

![Hardware Setup](https://github.com/user-attachments/assets/21991b89-627d-40d4-9688-4e84bf2a5bcf)

---

## 🔌 Wiring Table

| Component     | ESP32 Pin | Role                   |
|---------------|------------|------------------------|
| INMP441 Mic   | GPIO 14/15/32 | Speech input          |
| MAX98357A DAC | GPIO 25/26/22 | Audio output          |
| Speaker       | DAC Out    | Translated voice playback |

---

## 📦 Use Cases

- 👩‍🏫 Classrooms in rural India
- 🏥 Hospitals with multilingual patients
- 🛑 Emergency scenarios with language barriers

---

