FROM python:3

RUN python3 -m pip install markupsafe

WORKDIR /sedaro-nano-main-V2/backend/

ADD . /sedaro-nano-main-V2/backend/

RUN pip install --upgrade pip \
    pip install --upgrade setuptools \
    pip install -r requirements.txt 

EXPOSE 5001

CMD ["python", "application.py"]