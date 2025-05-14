import streamlit as st
import edge_tts
import asyncio
import tempfile #learn somethind alternative check old project kira28   14-5-25

st.title("Kira29")
text = st.text_area("Enter Text:")
language_voice_map = {
    'mr': {'male': 'mr-IN-ManoharNeural'}
}
language = st.selectbox("Select Language", list(language_voice_map.keys()), index=0)
voice_type = st.selectbox("Select Voice", ['male','Nantar Add kru'])                 #Kira29
 
voice_id = language_voice_map.get(language, {}).get(voice_type)

async def generate_tts(text, voice):
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
        tmp_path = tmp_file.name
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(tmp_path)
    return tmp_path
if st.button("generate audio"):
    if text:
        if voice_id:
            audio_path = asyncio.run(generate_tts(text, voice_id))
            with open(audio_path, "rb") as f:
                st.audio(f.read(), format="audio/mp3")
                st.download_button("Download Audio", f, file_name="speech.mp3", mime="audio/mp3")
        else:
            st.error("voice is not available.")
    else:
        st.warning("enter some text again.")
