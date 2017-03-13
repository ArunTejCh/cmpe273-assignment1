FROM python:2.7.12
MAINTAINER Your Name "aruntejbombay@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
