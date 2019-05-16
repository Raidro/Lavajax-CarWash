FROM python:3.6-alpine
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["app.py"]
