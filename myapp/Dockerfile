from python:2.7.10

COPY requirements.txt /app/requirements.txt
COPY myapp.py /app/myapp.py

RUN pip install -r /app/requirements.txt

CMD ["python","/app/myapp.py"]


