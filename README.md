# 💻 Smart NLP Terminal – A Natural Language Based GUI Command Prompt
Smart NLP Terminal is a Natural Language Processing-powered desktop application that translates user-friendly text instructions into actual shell commands. It combines a Tkinter-based GUI with a Flask API backend and a trained Naive Bayes model to bridge the gap between everyday language and complex terminal syntax. Built as part of a Software Engineering course project (TCS611), it provides a secure, intuitive, and intelligent alternative to traditional command-line tools — especially for beginners.

> A Software Engineering Project (TCS611)  
> Developed by Team NLPrompt (SE(OS)-VI-T003)

## 📌 Project Overview

**Smart NLP Terminal** is a GUI-based command-line assistant that allows users to run shell commands using plain natural language. It is designed to simplify system-level tasks for non-technical users or those unfamiliar with command-line syntax by translating human-readable input into terminal commands.

## 🚀 Key Features

- 🧠 Natural Language Processing (NLP) to understand user input
- 🖥️ GUI built with Tkinter for real-time interaction
- 🔗 Flask backend to process inputs and predict commands
- 📊 Trained TF-IDF + Multinomial Naive Bayes model
- 🔁 Smart dynamic replacement of filenames/folder names in commands
- 🛡️ Secure command execution with command whitelisting

## 🏗️ Project Architecture

### 1. GUI (Frontend)
- Developed using Tkinter
- Accepts natural language input from user
- Displays terminal output in a console-like interface

### 2. Backend (Flask API)
- Receives user input via POST requests
- Preprocesses text (tokenization, stemming, stopword removal using NLTK)
- Uses TF-IDF + Naive Bayes model to predict shell command
- Executes command securely and returns the output

### 3. Smart Replacement Logic
- Replaces natural language file/folder mentions with actual system paths using regex
- Enhances execution accuracy and flexibility

## 🧪 Testing Summary

| Component               | Status | Notes                                               |
|------------------------|--------|-----------------------------------------------------|
| Unit Tests             | ✅ Pass | `clean()` and `smart_replace()` function as expected |
| API Testing            | ✅ Pass | Flask API returns correct predictions               |
| GUI Functionality      | ✅ Pass | Inputs/outputs work as intended                     |
| Command Execution      | ✅ Pass | Commands run securely with proper substitution      |
| Model Accuracy         | ✅ 96%  | Achieved 96% on custom dataset                      |


## 🧾 Deliverables

- ✅ GUI built using Tkinter
- ✅ Flask API backend
- ✅ Trained NLP model and TF-IDF vectorizer (`model.pkl`, `tfidf.pkl`)
- ✅ `smart_replace()` logic
- ✅ Secure command execution using subprocess
- ✅ Custom dataset for command training
- ✅ End-to-end integration between GUI and backend


## 📂 File Structure

```bash
📦 nlp-smart-terminal/
├── frontend.py           # GUI frontend using Tkinter
├── app.py                # Flask backend API
├── PBL_OS.py             # Training script for TF-IDF + Naive Bayes
├── model.pkl             # Trained ML model
├── tfidf.pkl             # Trained vectorizer
├── dataset.csv           # Custom dataset (commands + NL inputs)
├── README.md             # Project readme

**📈 Future Scope**
🧠 Integrate LLMs for smarter command prediction
📁 Expand dataset for broader command support
🔐 Risk-aware confirmation for critical commands
🧑‍🎨 Improve GUI responsiveness and design
📊 Feedback-based learning to refine predictions

📍 Repository URL: https://github.com/TvesaDev3/NLP_based_command_prompt
