import speech_recognition as sr

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    
    # Load the audio file
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
    
    try:
        # Use Google's Speech Recognition API
        text = recognizer.recognize_google(audio_data)
        print("Transcription:")
        print(text)
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"API error: {e}")
