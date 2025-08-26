import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"API error: {e}"

def browse_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.wav *.aiff *.flac")],
        title="Select an Audio File"
    )
    if file_path:
        transcription = transcribe_audio(file_path)
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, transcription)

# GUI setup
root = tk.Tk()
root.title("Audio Transcriber")
root.geometry("500x400")

# Browse button
browse_button = tk.Button(root, text="Browse Audio File", command=browse_file)
browse_button.pack(pady=20)

# Text box to display transcription
text_box = tk.Text(root, wrap=tk.WORD, height=15, width=60)
text_box.pack(pady=10)

# Run GUI
root.mainloop()
