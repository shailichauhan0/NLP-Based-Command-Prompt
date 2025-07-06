import tkinter as tk
import requests

def execute_command():
    natural_command = entry.get()

    try:
        response = requests.post(
            "http://127.0.0.1:5000/predict",
            json={"input": natural_command}
        )
        result = response.json()
        output.delete(1.0, tk.END)
        output.insert(tk.END, result["output"])
    except Exception as e:
        output.delete(1.0, tk.END)
        output.insert(tk.END, f"Error: {str(e)}")

root = tk.Tk()
root.title("NLP Terminal")

entry = tk.Entry(root, width=100)
entry.pack()

submit_button = tk.Button(root, text="Execute", command=execute_command)
submit_button.pack()

output = tk.Text(root, width=100, height=20, bg="black", fg="white", font=("Courier New", 10))
output.pack()

root.mainloop()
