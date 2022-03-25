FROM python:3.9.7

WORKDIR /home11

COPY home11/requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY home11/conftest.py .
COPY home11/pytest.ini .
COPY home11/README.md .
COPY home11/pages/ /home11/pages
COPY home11/tests/ /home11/tests

CMD ["pytest", "-v", "-n 2"]
