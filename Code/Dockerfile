From python:3.11

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD clean.py .
ADD predict.py .
ADD upload.py .
ADD layout.py .
ADD main.py .
ENTRYPOINT python main.py


