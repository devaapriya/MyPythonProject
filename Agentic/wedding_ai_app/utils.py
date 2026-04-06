import os
from openai import OpenAI
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import textwrap
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_wish(message, mode, recipient):

    if recipient == "👰 Bride":
        context = "for the bride"
    elif recipient == "🤵 Groom":
        context = "for the groom"
    else:
        context = "for the couple"

    if mode == "💌 Emotional":
        prompt = f"Write a heartfelt emotional wedding wish in 2-3 lines {context}: {message}"

    elif mode == "😂 Funny":
        prompt = f"Write a light funny wedding wish in 2-3 lines {context}: {message}"

    elif mode == "🪔 Traditional":
        prompt = f"Write a traditional Indian wedding blessing in 2-3 lines {context}: {message}"

    else:
        return message  # no AI

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

import json

def save_data(name, message, output, mode, recipient):

    entry = {
        "name": name,
        "input": message,
        "output": output,
        "mode": mode,
        "recipient": recipient
    }

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)
        
def save_to_sheets(name, message, output, mode, recipient):

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    # creds = ServiceAccountCredentials.from_json_keyfile_name(
    #     "credentials.json", scope
    # )

    creds_dict = st.secrets["gcp_service_account"]

    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

    gsclient = gspread.authorize(creds)

    sheet = gsclient.open("Wishes").sheet1

    sheet.append_row([
        name,
        message,
        output,
        mode,
        recipient,
        str(datetime.now())
    ])

def create_wish_image(name, message, recipient):

    # Select background
    if recipient == "👰 Bride":
        bg_path = "assets/bride.jpg"
    elif recipient == "🤵 Groom":
        bg_path = "assets/groom.jpg"
    else:
        bg_path = "assets/couple.jpg"

    img = Image.open(bg_path).convert("RGBA")
    img = img.resize((800, 1000))

    # Overlay (dark for readability)
    overlay = Image.new('RGBA', img.size, (0, 0, 0, 130))
    img = Image.alpha_composite(img, overlay)

    draw = ImageDraw.Draw(img)

    # Font
    try:
        font = ImageFont.truetype("arial.ttf", 32)
    except:
        font = ImageFont.load_default()

    # Wrap text
    wrapped_text = textwrap.fill(message, width=35)

    final_text = f"{wrapped_text}\n\n— {name}"

    # Get text size
    bbox = draw.multiline_textbbox((0, 0), final_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Bottom-center position
    x = (800 - text_width) // 2
    y = 1000 - text_height - 80  # padding from bottom

    draw.multiline_text(
        (x, y),
        final_text,
        fill=(255, 255, 255),
        font=font,
        align="center"
    )

    file_path = f"{name}_wish.png"
    img.convert("RGB").save(file_path)

    return file_path