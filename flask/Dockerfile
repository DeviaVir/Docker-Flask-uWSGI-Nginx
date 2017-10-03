FROM python:3.6

COPY requirements.txt /usr/src/
RUN pip install -r /usr/src/requirements.txt
ENTRYPOINT ["python"]
CMD ["/usr/src/site/run.py"]
