import streamlit as st
from dotenv import load_dotenv
import os
import base64

load_dotenv()

from utils import generate_wish, save_to_sheets, create_wish_image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_image = get_base64(os.path.join(BASE_DIR, "assets", "invite_bg.jpg"))

st.set_page_config(
    page_title="AI Wedding Wish Generator 💍",
    page_icon="💍",
    layout="centered"
)

# 🎨 Custom background
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{bg_image}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}
[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 240, 245, 0.75);
    z-index: -1;
}}
body {{
    font-size: 18px;
    line-height: 1.6;
    color: #2c2c2c !important;
}}
p, div, span, label {{
    font-size: 18px !important;
    color: #2c2c2c !important;
}}
h1 {{ font-size: 2.5rem; color: #b03060 !important; font-weight: 700; }}
h2 {{ font-size: 2rem; color: #b03060 !important; }}
h3 {{ font-size: 1.5rem; color: #b03060 !important; }}
input, textarea {{ font-size: 16px !important; }}
.stButton > button {{
    background-color: #ff4b6e !important;
    color: white !important;
    border-radius: 12px;
    font-weight: 600;
    border: none;
    padding: 10px 18px;
    font-size: 16px;
}}
.stButton > button:hover {{ background-color: #e8435f !important; }}
label {{ font-weight: 600; }}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align: center; color: #d6336c;'>
💍 Shabu ❤️ Aishu Wedding Wishes
</h1>
<p style='text-align: center;'>
Create a magical AI-powered wish ✨
</p>
""", unsafe_allow_html=True)

with st.container():
    st.markdown("### ✨ Create Your Wish")
    name = st.text_input("Enter your name")

    recipient = st.radio(
        "Send my wishes to ",
        ["👰 Bride", "🤵 Groom", "💑 Couple"]
    )

    mode = st.radio(
        "Choose your wish style",
        ["💌 Emotional", "😂 Funny", "🪔 Traditional", "✍️ My Own Wish"]
    )
    message = mode
    if mode == "✍️ My Own Wish":
        message = st.text_area("Write your message")

if st.button("Generate Magical Wish ✨"):

    if not name or not message:
        st.warning("Please fill all fields")
    else:
        with st.spinner("Creating magic... ✨"):

            output = generate_wish(message, mode, recipient)
            save_to_sheets(name, message, output, mode, recipient)
            image_path = create_wish_image(name, output, recipient)

        # st.success("Done! 🎉")

        if mode != "✍️ My Own Wish":
            st.markdown("## 💖 Your Beautiful Wish")
            st.write(output)

        st.image(image_path, caption="✨ Your Wish Card")

        # 💖 Custom style for download button
        st.markdown("""
        <style>
        /* Fix download button colors */
        .stDownloadButton > button {
            background-color: #ff4b6e !important; /* bright pink background */
            color: white !important;              /* white text */
            border-radius: 12px;
            font-weight: 600;
            border: none;
            padding: 10px 18px;
            font-size: 16px;
        }
        .stDownloadButton > button:hover {
            background-color: #e8435f !important; /* slightly darker pink on hover */
        }
        </style>
        """, unsafe_allow_html=True)

        # Single download button
        with open(image_path, "rb") as file:
            st.download_button(
                label="📥 Download your wish image and share on Instagram or WhatsApp",
                data=file,
                file_name=f"{name}_wish.png",
                mime="image/png"
            )

st.markdown("---")

st.markdown("""
<p style='text-align: center; font-size: 14px;'>
❤️ Loving ThaiAthai ✨
</p>
""", unsafe_allow_html=True)