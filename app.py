import streamlit as st
import os

st.set_page_config(page_title="Business Viral AI Editor", layout="wide")

st.title("🚀 Business Viral AI Editor")
st.subheader("Step 1: Reliable Upload System")

# Ensure a temporary directory exists for video processing
if not os.path.exists("temp_video"):
    os.makedirs("temp_video")

uploaded_file = st.file_uploader("Upload Uncle's Raw Video (MP4)", type=["mp4", "mov"])

if uploaded_file is not None:
    # Check file size (purely for info)
    file_size_mb = uploaded_file.size / (1024 * 1024)
    st.write(f"📁 Video detected: {uploaded_file.name} ({file_size_mb:.2f} MB)")
    
    # SAVE to disk immediately (avoids RAM crashes)
    save_path = os.path.join("temp_video", "raw_input.mp4")
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success("✅ Video safely stored on server. We are ready for Step 2.")
    st.video(save_path)
