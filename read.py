import pytesseract
from PIL import Image
import streamlit as st

#poetry export -f requirements.txt --output requirements.txt --without-hashes

st.title("Hello!")
st.text("This is an example application that test the ability to create an .exe from an web-application")

st.write("Optical Character Recognition (OCR)")
image = st.file_uploader("upload file", type=["png","jpg"])

if image:
    img = Image.open(image)
    st.image(img, width=350)
    st.info("extracted text")

    text = pytesseract.image_to_string(img, lang="en")
    st.write("{}".format(text))