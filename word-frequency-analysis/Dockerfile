# this is to pull python image
FROM python:latest

# make dir app if doesn't exsist make it and go in it
WORKDIR /app

# copy "requirements.txt" file in app dir 
COPY random_paragraphs.txt  requirements.txt ./

# install the requirements in the requirements file
RUN pip install -r requirements.txt

# copy "script.py" file in app dir 
COPY script.py .

# excute this commnand
CMD python script.py



