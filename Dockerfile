#QUESTIONS?
#CMD to build docker --> docker build -t urentool_nunner  (from the src directtory?)
#Dockerfile in root van src (is dat src?) of is SRC_NUNNER_URENTOOl?
FROM python:3.8.2-slim
RUN apt-get update
#update (supporting) tesseract-ocr :
RUN apt-get --assume-yes install libtesseract-dev
RUN apt-get --assume-yes install libleptonica-dev
RUN apt-get --assume-yes install liblept5:
RUN apt-get --assume-yes install tesseract-ocr

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


COPY . /app
#COPY src /app/src
#COPY settings /app/settings

#CMD ["python", "-u", "./__main__.py"]  #initial version, should have another start

#CMD ["python", "-u", "./src/app.py"]
CMD ["streamlit", "run", "./src/app.py"]



