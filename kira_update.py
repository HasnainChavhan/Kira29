import streamlit as st
import edge_tts
import asyncio
import tempfile#learn something alternative check old project kira28-14-5-25

st.title("Kira29.1 -Text-to-Speech") #Kira29.1updated 

text = st.text_area("Enter Text:")

language_voice_map = {  # voices: https://speech.microsoft.com/portal/voicegallery
    'mr': {'male': 'mr-IN-ManoharNeural', 'female': 'mr-IN-AarohiNeural'},
    'hi': {'male': 'hi-IN-MadhurNeural', 'female': 'hi-IN-SwaraNeural'},
     'bn': {'male': 'bn-IN-PrabirNeural', 'female': 'bn-IN-TanishaaNeural'}, 
    'ta': {'male': 'ta-IN-ValluvarNeural', 'female': 'ta-IN-PallaviNeural'},
}

language = st.selectbox("Select Language", list(language_voice_map.keys()))
voice_type = st.selectbox("Select Voice", ['male', 'female'])

voice_id = language_voice_map.get(language, {}).get(voice_type)

async def generate_tts(text, voice):
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
        tmp_path = tmp_file.name
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(tmp_path)
    return tmp_path

if st.button("Generate Audio"):
    if text:
        if voice_id:
            audio_path = asyncio.run(generate_tts(text, voice_id))
            with open(audio_path, "rb") as f:
                st.audio(f.read(), format="audio/mp3")
                st.download_button("Download Audio", f, file_name="speech.mp3", mime="audio/mp3")
        else:
            st.error("Selected voice is not available.")
    else:
        st.warning("enter some text.")
