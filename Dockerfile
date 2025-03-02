FROM python:3.10-slim

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]