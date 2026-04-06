import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from utils import generate_wish, save_data, save_to_sheets, create_wish_image
import urllib.parse


st.set_page_config(page_title="Test App", layout="centered")

st.title("💍 Wedding Wish AI App (Test)")

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
if mode == "✍️ My Own Wish" :
    message = st.text_area("Write your message")

if st.button("Generate Wish ✨"):

    if not name or not message:
        st.warning("Please fill all fields")
    else:
        with st.spinner("Creating magic... ✨"):

            output = generate_wish(message, mode, recipient)
            # save_data(name, message, output, mode, recipient)
            save_to_sheets(name, message, output, mode, recipient)
            image_path = create_wish_image(name, output, recipient)


        st.success("Done! 🎉")

        # st.write(f"👤 {name}")
        # st.write(f"🎯 {recipient}")
        # st.write(f"🎨 {mode}")

        if mode != "✍️ My Own Wish":
            st.subheader("💖 Your AI Wish")
            st.write(output)

        st.image(image_path, caption="✨ Your Wish Card")

        # with open(image_path, "rb") as file:
        #     st.download_button(
        #         label="📥 Download Image",
        #         data=file,
        #         file_name=f"{name}_wish.png",
        #         mime="image/png"
        #     )

        st.markdown("### 💖 Share your wish")
        st.markdown("###### 📸 On Whatsapp / Upload to Instagram Story ✨")

        # Encode text for WhatsApp
        encoded_text = urllib.parse.quote(output)

        whatsapp_url = f"https://wa.me/?text={encoded_text}"

        # st.info("📸 Share on Whatsapp / Upload to Instagram Story ✨")

        # Buttons layout
        col1, col2 = st.columns(2)

        with col1:
            # st.link_button("📤 Share on WhatsApp", whatsapp_url)
            st.image("./assets/whatsapp.png", width=80)
            st.link_button("Share on WhatsApp", whatsapp_url)

        with col2:
            st.image("./assets/instagram.png", width=80)
            with open(image_path, "rb") as file:
                st.download_button(
                    "Download for Instagram",
                    data=file,
                    file_name=f"{name}_wish.png",
                    mime="image/png"
                )