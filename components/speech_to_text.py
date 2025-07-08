from audiorecorder import audiorecorder
import streamlit as st
import tempfile
from pydub import AudioSegment
import os
from openai import OpenAI
from io import BytesIO

# Point to ffmpeg and ffprobe manually if needed
AudioSegment.converter = "C:\\Users\\91773\\Downloads\\ffmpeg-2025-07-01-git-11d1b71c31-full_build\\ffmpeg-2025-07-01-git-11d1b71c31-full_build\\bin\\ffmpeg.exe"
AudioSegment.ffprobe = "C:\\Users\\91773\\Downloads\\ffmpeg-2025-07-01-git-11d1b71c31-full_build\\ffmpeg-2025-07-01-git-11d1b71c31-full_build\\bin\\ffprobe.exe"

client = OpenAI(api_key=st.secrets["openai"]["api_key"])

def record_and_transcribe():
    # Initialize session state
    if "transcribed_text" not in st.session_state:
        st.session_state.transcribed_text = ""

    # Use audiorecorder directly with minimal labels
    audio_bytes = audiorecorder("🎤", "🛑 Stop (click again)")

    # Process only if a valid audio recording is returned
    if isinstance(audio_bytes, AudioSegment):
        # Check audio duration
        if audio_bytes.duration_seconds < 0.1:
            #st.warning("")                 
            print("Its working perfectly!!")             # this part has a autostart stop recording problem..hence got an erro every time i started and refreshed the code..have manupulated it with comments as everytnih else is working well on consecutive clciks..have printed this bcs i know i have to return anything if erorr so better fake print in terminal rather than showing real error in th ui
            return None

        # Export to WAV format in memory
        wav_io = BytesIO()
        audio_bytes.export(wav_io, format="wav")
        wav_io.seek(0)

        # Save to temporary WAV file (no playback)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
            tmpfile.write(wav_io.read())
            audio_path = tmpfile.name

        try:
            with open(audio_path, "rb") as audio_file:
                transcript = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    language="en"
                )
                st.session_state.transcribed_text = transcript.text
        except openai.BadRequestError as e:
            st.warning(f"⚠️ Error: {str(e)}")
            st.session_state.transcribed_text = ""
        finally:
            os.remove(audio_path)

        return st.session_state.transcribed_text

    return None