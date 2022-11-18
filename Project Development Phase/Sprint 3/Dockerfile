
FROM python:3.8
WORKDIR /docker-app

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt
COPY DigiCertGlobalRootCA.crt .
COPY ./peta ./peta

CMD ["python","./peta/app.py"]

