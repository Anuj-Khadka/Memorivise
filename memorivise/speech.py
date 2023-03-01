import speech_recognition as sr
from flask import flash

def transcribe():
    # Create a Recognizer object
    r = sr.Recognizer()

    # Specify the audio file path
    audio_file = "/home/algae/Public/Memorivise/Neovim in 100 Seconds.wav"

    # Load the audio file into a AudioFile object
    # with sr.AudioFile(audio_file) as source:
    # audio = r.record(source)  # Read the entire audio file and store it in a variable

    # Use the microphone as source
    with sr.Microphone() as source:
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        flash("Speak something...", category="success")
        print("Speak something...")
        # Listen for audio and store it in a variable
        audio = r.listen(source, timeout=5.0)

    try:
        # Use Google Speech Recognition to transcribe the audio
        text = r.recognize_google(audio)

        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        cantHear = "Oops! Could not understand audio."
        return cantHear
    except sr.RequestError as e:
        err = f"Error: {e}"
        return err
