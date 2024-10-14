# import openai
from openai import OpenAI
import pyaudio
import wave
import tempfile
import os
import pyttsx3
# from your_vector_db_script import query_vector_db, query_openai
from openAI.py import query_openai, query_vector_db



# Set your OpenAI API key
# openai.api_key = 'your_openai_api_key_here'

# Initialize text-to-speech engine
engine = pyttsx3.init()

def record_audio(duration=5, sample_rate=44100, chunk=1024, channels=1):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("Recording...")
    frames = []

    for i in range(0, int(sample_rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    return frames, sample_rate

def save_audio(frames, sample_rate):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        wf = wave.open(temp_audio.name, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        return temp_audio.name

def transcribe_audio(audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        transcript = OpenAI.Audio.transcribe("whisper-1", audio_file)
        
    return transcript.text

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        input("Press Enter to start speaking...")
        frames, sample_rate = record_audio()
        audio_file_path = save_audio(frames, sample_rate)

        try:
            transcription = transcribe_audio(audio_file_path)
            print(f"You said: {transcription}")

            relevant_texts = query_vector_db(transcription)
            context = " ".join(relevant_texts)
            response = query_openai(transcription, context)

            print(f"ChatBot: {response}")
            text_to_speech(response)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        finally:
            os.unlink(audio_file_path)

        if input("Do you want to ask another question? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()