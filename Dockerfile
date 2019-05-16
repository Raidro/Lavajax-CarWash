FROM python:3.6-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
