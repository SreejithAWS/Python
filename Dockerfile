From python:slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8020
CMD [ "python", "main.py" ]
