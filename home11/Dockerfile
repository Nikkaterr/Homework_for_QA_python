FROM python:3.9.7

WORKDIR /home11

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY conftest.py .
COPY pytest.ini .
COPY README.md .
COPY ./pages/ /home11/pages
COPY ./tests/ /home11/tests

CMD ["pytest", "-v", "-n 2"]