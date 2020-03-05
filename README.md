# flaskvstore
Flask KV store api implementation


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
	
## Setup
This is a step-by-step tutorial that details how to configure Flask to run on Docker with exports as Prometheus metrics.

In a virtualenv, install Flask, Gunicorn:

```
 pip install -r requirements.txt
```
- Prometheus: https://github.com/prometheus/statsd_exporter
- Grafana: https://prometheus.io/docs/visualization/grafana/

	


# How to deploy with Docker

After installing Gunicorn and Flask, create a file app.py that return flask APP.

```
 docker build --tag flaskvstore
 docker run --detach -p 5000:5000 flaskvstore
```





