
FROM python:3.6-slim-stretch

RUN apt update
RUN apt install -y python3-dev gcc

ADD requirements.txt requirements.txt
ADD model_corps_mail_bert  model_corps_mail_bert/
ADD api.py api.py

# Install required libraries
RUN pip install -r requirements.txt

# Run it once to trigger resnet download
#RUN python api.py

EXPOSE 8008

# Start the serverCMD ["python", "api.py", "serve"]
