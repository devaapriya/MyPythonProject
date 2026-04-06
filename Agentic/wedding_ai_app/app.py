import streamlit as st

st.set_page_config(page_title="Test App", layout="centered")

st.title("💍 Wedding AI App (Test)")

name = st.text_input("Enter your name")

message = st.text_area("Write your message")

if st.button("Submit"):
    if name and message:
        st.success(f"Thanks {name}! 🎉")
        st.write("Your message:")
        st.write(message)
    else:
        st.warning("Please fill all fields")