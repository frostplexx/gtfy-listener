FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN pip3 install requests python-dotenv websocket-client
ENV GOTIFY_HOST=
ENV GOTIFY_TOKEN=
ENV NTFY_HOST=
ENV NTFY_USERNAME=
ENV NTFY_PASSWORD=
COPY gtfy.py /usr/bin
CMD ["python3", "/usr/bin/gtfy.py"]
