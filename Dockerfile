FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 1080
CMD ["python", "app.py"]