import pytesseract
from PIL import Image
import streamlit as st
import fitz
from pathlib import Path
#poetry export -f requirements.txt --output requirements.txt --without-hashes



hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


docker_cwd = Path.cwd()

test_ocr = True
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
test_local_pdf_split = False
#pdf_to_split = r'C:\Users\TomMul\Brightcape BV\ProjectenBrightCape - 210920 - Nunner Uren tool\TEST_DATA_URENTOOL\INPUT\FORMS\form_template_added_training - sample.pdf'
test_web_pdf_split = True

if test_ocr:
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


if test_local_pdf_split:

    st.title("Example pdf split from path")
    doc = fitz.open(pdf_to_split)
    page_ct = 0
    for page in doc:  # iterate through the pages
        print(page)
        # st.text(page)
        pix = page.get_pixmap()  # render page to an image
        o_path = fr'C:\Users\TomMul\Brightcape BV\ProjectenBrightCape - 210920 - Nunner Uren tool\TEST_DATA_URENTOOL\INPUT\FORMS\output_fitz\{page.number} splitted_img.png'
        pix.save(o_path)
        # pix.save("../data/out/page-%i.png" % page.number)  # store image as a PNG

        #POPPLER SOLUTION
        # results = convert_from_path(pdf_to_split,
        #                              # poppler_path=poppler_path
        #                              )
        #


        page_ct = page_ct + 1
        # st.text(f"{results}")
    st.text(f"NR of images - from path {page_ct} ")


if test_web_pdf_split:

    st.title("Example pdf upload & split")
    my_pdf = st.file_uploader("upload your PDF", type=["pdf"])


    if my_pdf :
        st.text("uploaded PDF info:")
        st.text(my_pdf)

        # To read file as bytes:
        bytes_data = my_pdf.read()
        doc = fitz.open(stream = bytes_data, filetype="pdf" )
        print("from upload")

        ct = 0
        import os
        print(f"cwd : {os.getcwd()}")
        for page in doc:  # iterate through the pages
            ct = ct + 1
            print(page)
            st.text(page)
            pix = page.get_pixmap()  # render page to an image
            #o_path = fr'C:\Users\TomMul\Brightcape BV\ProjectenBrightCape - 210920 - Nunner Uren tool\TEST_DATA_URENTOOL\INPUT\FORMS\output_fitz\from_upload {page.number} splitted_img.png'



            o_path = docker_cwd / "data" / "out" / f"{ct} splitted_img.png"
            pix.save(o_path)
            #pix.save("data/out/page-%i.png" % page.number)  # store image as a PNG

        st.text(f"nr of images extracted from PDF : {ct}")

        if st.checkbox("Show forms"):
            nr_forms = ct
            st.text(f"{nr_forms} Forms uploaded, choose a value between 1 and {nr_forms}")


            with st.container():  # create contained for side by side display
                col1, col2 = st.columns([1, 4])
            with col1:  # col1 for selector
                im_id = st.number_input('select img', min_value=1, max_value=nr_forms)
            with col2:  # display the image in second colu
                i_path = docker_cwd / "data" / "out" / f"{im_id} splitted_img.png"
                select_im = Image.open(i_path)
                st.image(select_im, channels="BGR")

            st.text(f"selected path : {i_path}")


