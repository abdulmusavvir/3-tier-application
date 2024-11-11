FROM python:3.9
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN ls /usr/local/lib/python3.9/site-packages
COPY app.py .
CMD ["python3","app.py"]
