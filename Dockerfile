FROM python:3.8
 
WORKDIR /opt/loggerman/
COPY . /app
 
RUN pip install -r /app/requirements.txt
 
ENTRYPOINT python /app/app.py
