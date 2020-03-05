# flaskvstore
Flask Key-Value Store API implementation


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is simple key-value application, complete with tests, local deployment and documentation.


## Functionalities
  * Get Value
  * Get all Keys and Values
  * Set a value
  * Existence value check
  * Delete a value
  * Delete all values
  * Expiry time to put values
  * Wildcard keys for geting all values
  * Logging
  * HTTP Status
	
## Technologies
Project is created with:
* Flask
* Redis
* Docker
* Gunicorn

Project is instrumented with:
- Prometheus : https://prometheus.io/docs/prometheus/latest/getting_started/
- Statsd Exporter: https://github.com/prometheus/statsd_exporter
- Grafana: https://prometheus.io/docs/visualization/grafana/
	
## Setup
This is a step-by-step tutorial that details how to configure the project.
In a virtualenv, install requirements:

```
 pip install -r requirements.txt
```

In app.py set your redis host.


```python

 REDIS_HOST = 'YOUR_REDIS_HOST'
 
```

In Dockerfile set your STATSD_EXPORTER_HOST

```
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app", "--statsd-host=STATSD_EXPORTER_HOST:9125", "--statsd-prefix=flaskvstore"]
 
```



### Deploy with Docker

After installing Gunicorn and Flask, create a file app.py that return flask APP.

```
 docker build --tag flaskvstore
 docker run --detach -p 5000:5000 flaskvstore
```

Setup your statsd configuration  with following statsd.conf file:  

```
mappings:
  - match: flaskvstore.gunicorn.request.status.*
    help: "http response code"
    name: "http_response_code"
    labels:
      status: "$1"
      job: "flaskvstore_gunicorn_response_code"

```

Add following job to scrape_configs in prometheus.yml file. 
Set your STATSD_EXPORTER_HOST: 

```
scrape_configs:
  - job_name: 'flaskvstore_gunicorn'
    static_configs:
      - targets: ['STATSD_EXPORTER_HOST:9102']

```


## Functionality Details

#### Get Value
#### Get all Keys and Values
#### Set a value
#### Existence value check
#### Delete a value
#### Delete all values
#### Expiry time to put values
#### Wildcard keys for geting all values
#### Logging
#### HTTP Status




