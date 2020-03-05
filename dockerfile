FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip install flask gunicorn simplekv redis
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app", "--statsd-host=STATSD_EXPORTER_HOST:9125", "--statsd-prefix=flaskvstore"]