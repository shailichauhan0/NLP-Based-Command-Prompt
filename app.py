from flask import Flask, request, jsonify
import pickle
import subprocess
import os
import re
import nltk 
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

nltk.download('stopwords')
stop = set(stopwords.words('english'))
st = PorterStemmer()

# Load your trained model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tfidf.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

app = Flask(__name__)

# -------- Helper Functions -------- #

def clean(text):
    text = text.lower()
    words = [st.stem(i) for i in text.split() if i not in stop]
    return " ".join(words)

def extract_full_file_names(text):
    return re.findall(r'\b[\w\-.]+\.(?:txt|log|md|pdf|sh|cpp|py|csv|json|xml|html)\b', text)

def smart_replace(natural_input, generated_command):
    gen_cmd = generated_command.strip()

    # List of no-argument commands
    no_arg_commands = ["ls", "ls -l", "ls -a", "cd ..", "pwd", "tree"]
    if gen_cmd in no_arg_commands:
        return gen_cmd

    # Extract real file/folder names from user input
    real_files = extract_full_file_names(natural_input)
    folder_matches = re.findall(r'\bfolder\s+([\w\-]+)', natural_input)

    # Find default names in predicted command
    default_names = re.findall(
        r'\b[\w\-]+\.(?:txt|md|log|pdf)|\bmyfolder\b|\bfoldername\b|\b[a-zA-Z_]*folder\b',
        gen_cmd
    )

    # Merge potential replacements
    replacements = folder_matches + real_files

    # Replace in predicted command
    for default, real in zip(default_names, replacements):
        gen_cmd = gen_cmd.replace(default, real, 1)

    return gen_cmd

# -------- Flask Route -------- #

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        user_input = data['input']

        print("Received user input:", user_input)

        cleaned_input = clean(user_input)
        print("Cleaned input:", cleaned_input)

        transformed_input = vectorizer.transform([cleaned_input])
        raw_command = model.predict(transformed_input)[0]
        print("Raw predicted command:", raw_command)

        predicted_command = smart_replace(user_input, raw_command)
        print("After smart_replace:", predicted_command)

        # Execute command
        if predicted_command == "jupyter notebook":
            subprocess.Popen(["jupyter", "notebook"])
            return jsonify({"output": "Launching Jupyter Notebook..."})
        elif predicted_command.startswith("cd"):
            try:
                os.chdir(predicted_command.split(" ", 1)[1])
                return jsonify({"output": f"Changed directory to {os.getcwd()}"})
            except Exception as e:
                return jsonify({"output": f"Error: {str(e)}"})
        else:
            print(f"Executing final command: {predicted_command}")
            result = subprocess.run(predicted_command, shell=True, capture_output=True, text=True)
            print("Command output:", result.stdout)
            print("Command errors:", result.stderr)
            return jsonify({"output": result.stdout or result.stderr})
    except Exception as e:
        print("Exception:", str(e))
        return jsonify({"output": f"Error: {str(e)}"})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
