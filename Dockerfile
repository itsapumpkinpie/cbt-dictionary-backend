FROM python:3.10-alpine
RUN pip3 install pipenv
WORKDIR /app
COPY . .
RUN pipenv requirements > requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD [ "uvicorn", "app.main:app" ]

