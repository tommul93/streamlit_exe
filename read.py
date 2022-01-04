import pytesseract
from PIL import Image
import streamlit as st
from pdf2image import convert_from_path, convert_from_bytes


#poetry export -f requirements.txt --output requirements.txt --without-hashes

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#poppler_path = r'C:\Users\TomMul\Downloads\poppler-0.68.0\bin'
#pdf_to_split = r'C:\Users\TomMul\Brightcape BV\ProjectenBrightCape - 210920 - Nunner Uren tool\TEST_DATA_URENTOOL\INPUT\FORMS\form_template_added_training - sample.pdf'


st.title("upload image")
st.text("This is an example application that test the ability to create an .exe from an web-application")

st.write("Optical Character Recognition (OCR)")
image = st.file_uploader("upload file", type=["png","jpg"])

if image:
    img = Image.open(image)
    st.image(img, width=350)
    st.info("extracted text : ")
    text = pytesseract.image_to_string(img, lang="eng")

    # pytesseract.image_to_data(img, output_type=pytesseract.Output.DATAFRAME)
    st.write("{}".format(text))



st.title("Example pdf split from path")

# results = convert_from_path(pdf_to_split,
#                              # poppler_path=poppler_path
#                              )
#
# st.text(f"NR of images - from path {len(results)} ")
# st.text(f"{results}")
st.text(f"empty as of web")



st.title("Example pdf upload & split")
my_pdf = st.file_uploader("upload your PDF", type=["pdf"])


if my_pdf:
    st.text("uploaded PDF info:")
    st.text(my_pdf)

    # To read file as bytes:
    bytes_data = my_pdf.read()
    #st.write(bytes_data)

    my_pdf_upload_splitted = convert_from_bytes(bytes_data,
                                #poppler_path=poppler_path
                                )

    print(f"NR of images {len(my_pdf_upload_splitted)}")
    st.text(f"NR of images - from path {len(my_pdf_upload_splitted)} ")

    for single_page in my_pdf_upload_splitted:
        st.text(f"{single_page}")


