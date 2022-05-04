FROM python:3.10.4

COPY src/requirements.txt /src/requirements.txt
WORKDIR /src
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm 

COPY src /src


CMD ["python", "main.py"]
