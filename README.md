# 💻 Smart NLP Terminal – A Natural Language Based GUI Command Prompt

Smart NLP Terminal is a Natural Language Processing-powered desktop application that translates user-friendly text instructions into actual shell commands. It combines a Tkinter-based GUI with a Flask API backend and a trained Naive Bayes model to bridge the gap between everyday language and complex terminal syntax.

> 💪 Developed as part of the **Software Engineering Project (TCS611)**
> 👥 Team NLPrompt – Team ID: SE(OS)-VI-T003

---

## 📌 Project Overview

**Smart NLP Terminal** is a GUI-based command-line assistant that allows users to run shell commands using plain natural language. It is designed to simplify system-level tasks for non-technical users or those unfamiliar with command-line syntax by translating human-readable input into terminal commands.

---

## 🚀 Key Features

* 🧠 Natural Language Processing (NLP) to understand user input
* 🖥️ GUI built with Tkinter for real-time interaction
* 🔗 Flask backend to process inputs and predict commands
* 📊 Trained TF-IDF + Multinomial Naive Bayes model
* 🔀 Smart dynamic replacement of filenames/folder names in commands
* 🛡️ Secure command execution with command whitelisting

---

## 🏗️ Architecture Overview

### 🖥️ 1. GUI (Frontend)

* Built with **Tkinter**
* Accepts user input in natural language
* Displays terminal output in a console-style interface

### 🧠 2. Backend (Flask API)

* Receives natural language via POST request
* Cleans, stems, and vectorizes text using **NLTK** and **TF-IDF**
* Predicts corresponding shell command with a trained **Naive Bayes** model
* Safely executes command using Python `subprocess`/`os`

### 🔀 3. Smart Replacement Logic

* Detects filenames/folders from input using regex
* Dynamically inserts them into generated shell commands

---

## 📂 File Structure

```
📆 nlp-smart-terminal/
├── frontend.py           # GUI frontend using Tkinter
├── app.py                # Flask backend API
├── PBL_OS.py             # Training script for model and vectorizer
├── model.pkl             # Trained Naive Bayes model
├── tfidf.pkl             # Trained TF-IDF vectorizer
├── dataset.csv           # Custom dataset (natural text ↔ shell command)
├── README.md             # This documentation
```

---

## ✅ Testing Summary

| Component         | Status | Notes                                         |
| ----------------- | ------ | --------------------------------------------- |
| Unit Tests        | ✅ Pass | `clean()` and `smart_replace()` function well |
| API Testing       | ✅ Pass | Flask returns valid predictions               |
| GUI Functionality | ✅ Pass | Tkinter displays input/output properly        |
| Command Execution | ✅ Pass | Commands executed securely and successfully   |
| Model Accuracy    | ✅ 96%  | On validation set from dataset                |

---

## 🛠️ How to Run the Project

### 🔹 1. Start the Flask API

```bash
python app.py
```

> Runs at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### 🔹 2. Run the GUI Interface

In a **new terminal**, run:

```bash
python frontend.py
```

### 💬 Example Natural Language Commands

* `create a folder called projects`
* `delete test.txt`
* `list all files`
* `change directory to Downloads`

### 💡 Example Input/Output

**Input:**
`create a file called report.txt`

**Output:**
`File 'report.txt' created successfully.`

---

## 📈 Future Scope

* 🧠 Integrate LLMs for smarter command prediction
* 📁 Expand dataset for broader shell command coverage
* 🔐 Add confirmation popups for risky commands
* 👨‍🎨 Enhance GUI design and responsiveness
* 📊 Collect feedback for model improvement over time

---

## 📍 Repository

🔗 GitHub Repository: [NLP\_based\_command\_prompt](https://github.com/TvesaDev3/NLP_based_command_prompt)

---

## 👩‍💼 Developed By – Team NLPrompt

| Name           | ID        | Role        |                                                                 
| -------------- | --------- | ----------- |
| Shaili Chauhan | 22022108  | Team Lead   | 
| Tvesa Gupta    | 220221227 | Backend Dev | 
| Aryan Singhal  | 220211967 | ML/NLP Dev  |
| Aryan Parashar | 22021519  | GUI + API   | 
