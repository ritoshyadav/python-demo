FROM python:3.7
WORKDIR /usr/src/app
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt
COPy . . 
CMD ["python", "app.py"]
